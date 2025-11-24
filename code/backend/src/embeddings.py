"""
Embedding service for design patterns
"""
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List
import yaml

class EmbeddingService:
    def __init__(self, config_path: str = "config.yaml"):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)

        model_name = self.config['embeddings']['model']
        print(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)
        self.dimension = self.config['embeddings']['dimension']

    def embed(self, text: str) -> np.ndarray:
        """Generate embedding for a single text"""
        return self.model.encode(text, convert_to_numpy=True)

    def embed_batch(self, texts: List[str]) -> np.ndarray:
        """Generate embeddings for multiple texts"""
        return self.model.encode(texts, convert_to_numpy=True, show_progress_bar=True)

    def similarity(self, embedding1: np.ndarray, embedding2: np.ndarray) -> float:
        """Calculate cosine similarity between two embeddings"""
        return np.dot(embedding1, embedding2) / (
            np.linalg.norm(embedding1) * np.linalg.norm(embedding2)
        )
