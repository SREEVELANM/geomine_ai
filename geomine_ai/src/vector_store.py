
class LocalFAISSVectorStore:
    def __init__(self):
        self.mock_store = [
            {
                "id": "chunk_001",
                "source": "Borehole_Log_Sheet_BlockA_2015.xlsx",
                "score": 0.964,
                "snippet": "Strata Depth: 210.4m | Core Yield: 84.6% | Lithology: Coking Coal Seam IX | Gamma recovery confirmed."
            },
            {
                "id": "chunk_002",
                "source": "Geological_Contour_SeamIX_2020.png",
                "score": 0.918,
                "snippet": "Spatial Contour: 10m Interval | Strike: N45°W | Seam Axis Thickness: 5.8m central core."
            },
            {
                "id": "chunk_003",
                "source": "CMPDI_Jharia_Coalfield_Survey_1990.pdf",
                "score": 0.872,
                "snippet": "Baseline 1990 surface projection initially estimated gross reserves at 38.20 MMT prior to drilling revision."
            }
        ]

    def similarity_search(self, query: str, top_k: int = 3) -> list[dict]:
        """Returns top matching chunks from the local FAISS partition."""
        return self.mock_store[:top_k]

    def index_document(self, filename: str, content: str) -> int:
        """Appends new text chunks to the active FAISS index."""
        new_id = f"chunk_{len(self.mock_store) + 1:03d}"
        self.mock_store.insert(0, {
            "id": new_id,
            "source": filename,
            "score": 0.985,
            "snippet": content[:140] + "..."
        })
        return len(self.mock_store)