"""
Vector database for storing and retrieving design patterns using LanceDB
"""
import lancedb
import pyarrow as pa
import yaml
from typing import List, Dict, Any
import os
import numpy as np

class VectorStore:
    def __init__(self, config_path: str = "config.yaml"):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)

        persist_dir = self.config['vector_db']['persist_directory']
        os.makedirs(persist_dir, exist_ok=True)

        self.db = lancedb.connect(persist_dir)
        self.table_name = self.config['vector_db']['collection_name']
        self.dimension = self.config['embeddings']['dimension']

        # Create table if it doesn't exist
        if self.table_name not in self.db.table_names():
            self._create_table()

        self.table = self.db.open_table(self.table_name)
        print(f"Vector store initialized with {self.count()} patterns")

    def _create_table(self):
        """Create the patterns table with schema"""
        schema = pa.schema([
            pa.field("id", pa.string()),
            pa.field("content", pa.string()),
            pa.field("category", pa.string()),
            pa.field("name", pa.string()),
            pa.field("tags", pa.string()),
            pa.field("vector", pa.list_(pa.float32(), self.dimension)),
        ])
        self.db.create_table(self.table_name, schema=schema)

    def add_pattern(
        self,
        pattern_id: str,
        content: str,
        embedding: List[float],
        metadata: Dict[str, Any]
    ):
        """Add a design pattern to the vector store"""
        data = [{
            "id": pattern_id,
            "content": content,
            "category": metadata.get("category", ""),
            "name": metadata.get("name", ""),
            "tags": metadata.get("tags", ""),
            "vector": embedding,
        }]
        self.table.add(data)

    def add_patterns_batch(
        self,
        pattern_ids: List[str],
        contents: List[str],
        embeddings: List[List[float]],
        metadatas: List[Dict[str, Any]]
    ):
        """Add multiple design patterns"""
        data = []
        for i in range(len(pattern_ids)):
            data.append({
                "id": pattern_ids[i],
                "content": contents[i],
                "category": metadatas[i].get("category", ""),
                "name": metadatas[i].get("name", ""),
                "tags": metadatas[i].get("tags", ""),
                "vector": embeddings[i],
            })
        self.table.add(data)

    def search(
        self,
        query_embedding: List[float],
        top_k: int = 5,
        filter_metadata: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """Search for similar design patterns"""
        query = self.table.search(query_embedding).limit(top_k)

        if filter_metadata and "category" in filter_metadata:
            query = query.where(f"category = '{filter_metadata['category']}'")

        results = query.to_pandas()

        # Format results to match expected structure
        return {
            'ids': [results['id'].tolist()],
            'documents': [results['content'].tolist()],
            'metadatas': [[{
                'category': row['category'],
                'name': row['name'],
                'tags': row['tags']
            } for _, row in results.iterrows()]],
            'distances': [results['_distance'].tolist()] if '_distance' in results.columns else [[]]
        }

    def get_pattern(self, pattern_id: str) -> Dict[str, Any]:
        """Get a specific pattern by ID"""
        result = self.table.search().where(f"id = '{pattern_id}'").limit(1).to_pandas()
        if len(result) == 0:
            return None
        row = result.iloc[0]
        return {
            'id': row['id'],
            'content': row['content'],
            'metadata': {
                'category': row['category'],
                'name': row['name'],
                'tags': row['tags']
            }
        }

    def count(self) -> int:
        """Get total number of patterns"""
        return len(self.table)

    def clear(self):
        """Clear all patterns from the collection"""
        self.db.drop_table(self.table_name)
        self._create_table()
        self.table = self.db.open_table(self.table_name)
