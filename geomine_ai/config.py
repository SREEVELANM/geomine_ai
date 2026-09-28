import os

AIR_GAP_MODE = True
ALLOW_EXTERNAL_API = False
SECURITY_CLASSIFICATION = "RESTRICTED - MINISTRY OF COAL INTERNAL"

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
DEFAULT_MODEL = "llama3:8b-instruct-q4_0"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

CHUNK_SIZE = 512
CHUNK_OVERLAP = 64
SUPPORTED_EXTENSIONS = [".pdf", ".xlsx", ".csv", ".png", ".jpg", ".jpeg"]

FAISS_INDEX_DIR = "./data/faiss_index"