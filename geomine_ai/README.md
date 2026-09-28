# GeoMine AI - AI-Powered Geological Reporting System
**Smart India Hackathon (SIH26023) | Central Mine Planning & Design Institute (CMPDI)**

GeoMine AI is an air-gapped, multi-modal Retrieval-Augmented Generation (RAG) platform engineered to unlock decades of unsearchable geological maps, borehole logs, and mining archives.

## Key Features
- **100% Data Sovereignty:** Offline inference via local Ollama (Llama-3) and FAISS vector databases.
- **Parliamentary Question (PQ) Auto-Framer:** Automatically structures geological data into official Ministry of Coal Lok Sabha/Rajya Sabha Starred Question formats.
- **The Contradiction Engine:** Automatically surfaces and resolves cross-decade numerical variances between legacy surface projections and modern core-drilling logs.
- **Multi-Modal Processing:** Ingests PDFs, spreadsheets, and spatial contour maps via PyMuPDF and EasyOCR.

## Quickstart
```bash
pip install -r requirements.txt
streamlit run app.py