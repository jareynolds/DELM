"""
RAG (Retrieval Augmented Generation) pipeline for design patterns
"""
import yaml
from typing import List, Dict, Any, Optional
from .embeddings import EmbeddingService
from .vector_store import VectorStore
from .model import DesignLLM

class RAGPipeline:
    def __init__(self, config_path: str = "config.yaml"):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)

        print("Initializing RAG Pipeline...")
        self.embeddings = EmbeddingService(config_path)
        self.vector_store = VectorStore(config_path)
        self.llm = DesignLLM(config_path)

        self.top_k = self.config['rag']['top_k']
        self.similarity_threshold = self.config['rag']['similarity_threshold']

        print("RAG Pipeline ready!")

    def retrieve(
        self,
        query: str,
        category: Optional[str] = None,
        top_k: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """Retrieve relevant design patterns for a query"""

        # Generate embedding for query
        query_embedding = self.embeddings.embed(query).tolist()

        # Build filter if category specified
        filter_metadata = {"category": category} if category else None

        # Search vector store
        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k or self.top_k,
            filter_metadata=filter_metadata
        )

        # Format results
        patterns = []
        if results['documents'] and results['documents'][0]:
            for i, doc in enumerate(results['documents'][0]):
                pattern = {
                    'id': results['ids'][0][i],
                    'content': doc,
                    'metadata': results['metadatas'][0][i] if results['metadatas'] else {},
                    'distance': results['distances'][0][i] if results['distances'] else 0
                }
                patterns.append(pattern)

        return patterns

    def build_context(self, patterns: List[Dict[str, Any]]) -> str:
        """Build context string from retrieved patterns"""

        if not patterns:
            return "No specific design patterns found. Use general best practices."

        context_parts = []
        for i, pattern in enumerate(patterns, 1):
            metadata = pattern.get('metadata', {})
            category = metadata.get('category', 'general')
            name = metadata.get('name', f'Pattern {i}')

            context_parts.append(f"""
--- {name} ({category}) ---
{pattern['content']}
""")

        return "\n".join(context_parts)

    def generate(
        self,
        prompt: str,
        generation_type: str = "component",
        category: Optional[str] = None
    ) -> Dict[str, Any]:
        """Full RAG pipeline: retrieve patterns and generate output"""

        # Retrieve relevant patterns
        patterns = self.retrieve(prompt, category=category)

        # Build context from patterns
        context = self.build_context(patterns)

        # Generate based on type
        if generation_type == "component":
            output = self.llm.generate_ui_component(prompt, context)
        elif generation_type == "styles":
            output = self.llm.generate_styles(prompt, context)
        elif generation_type == "layout":
            output = self.llm.generate_layout(prompt, context)
        else:
            output = self.llm.generate(prompt, system_prompt=f"Context:\n{context}")

        return {
            'output': output,
            'patterns_used': len(patterns),
            'pattern_ids': [p['id'] for p in patterns]
        }

    def add_pattern(
        self,
        pattern_id: str,
        content: str,
        category: str,
        name: str,
        tags: List[str] = None
    ):
        """Add a new design pattern to the knowledge base"""

        embedding = self.embeddings.embed(content).tolist()
        metadata = {
            'category': category,
            'name': name,
            'tags': ','.join(tags) if tags else ''
        }

        self.vector_store.add_pattern(
            pattern_id=pattern_id,
            content=content,
            embedding=embedding,
            metadata=metadata
        )

        print(f"Added pattern: {name} ({pattern_id})")
