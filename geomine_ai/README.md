
# ⛏️ GeoMine AI: Air-Gapped Geological Reporting System

![Smart India Hackathon 2026](https://img.shields.io/badge/SIH_2026-PS_SIH26023-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Prototype_Active-success?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-100%25_Air--Gapped-red?style=for-the-badge)
![Tech Stack](https://img.shields.io/badge/Tech-Streamlit%20|%20Ollama%20|%20FAISS-blue?style=for-the-badge)

**GeoMine AI** is an on-premise, multi-modal Retrieval-Augmented Generation (RAG) platform developed for the **Central Mine Planning and Design Institute (CMPDI)**, **NLC India Limited**, and the **Ministry of Coal**. 

Built by team **The Rookiez** for Smart India Hackathon 2026, this system solves the critical bottleneck of manual geological data retrieval. It ingests decades of highly fragmented, unstructured mining archives (PDFs, handwritten notes, contour maps, and Excel bore-hole logs) and allows high-level officials to generate instant, highly accurate, officially formatted reports using localized AI—ensuring zero data leakage to the internet.

---

## ✨ Core Features & Innovations

*   **🛡️ 100% Data Sovereignty (Air-Gapped Architecture):** 
    Powered by a locally hosted Large Language Model (Llama-3 via Ollama) and local FAISS vector databases. No sensitive government mining data ever leaves the Ministry's hardware.
*   **⚖️ The Contradiction Engine:** 
    Automatically cross-references historical data (e.g., a 1990 surface projection vs. a 2015 core drill assay) and flags numerical discrepancies. Requires a human administrator to reconcile conflicts before official reports are generated, preventing AI hallucinations.
*   **🏛️ Parliamentary Question (PQ) Auto-Framer:** 
    Detects when a query is for a high-level government inquiry and automatically formats the AI's response to match the exact Lok Sabha/Rajya Sabha Starred Question template.
*   **👁️ Multi-Modal Ingestion Pipeline:** 
    Processes unstructured text via `PyMuPDF`, tabular strata data via `Pandas`, and complex spatial contour maps via Computer Vision (`EasyOCR`), converting them into unified, mathematically searchable vectors.
*   **🗺️ Interactive GIS Mapping:** 
    Integrates `Folium` to provide live, offline geospatial visualization of mining blocks and proved reserves (e.g., NLC Neyveli Mine-I).
*   **💬 Secure AI Chat Assistant:** 
    A conversational UI allowing officials to interrogate mining archives conversationally, maintaining context and citing ground-truth RAG sources.
*   **🔐 Hierarchical Maker-Checker Workflow & Telemetry:** 
    Role-based access control where Junior Geologists draft reports, but only Chief Secretaries can export them. Includes downloadable, encrypted system audit logs.

---

## 🛠️ Technology Stack

| Component | Technology Used |
| :--- | :--- |
| **Frontend Framework** | Streamlit |
| **Local LLM Engine** | Ollama (Llama-3-8B-Instruct) |
| **Vector Database** | FAISS (Facebook AI Similarity Search) |
| **Data Ingestion** | PyMuPDF, EasyOCR, Pandas |
| **Geospatial Mapping** | Folium, Streamlit-Folium |
| **API & Routing** | Python `requests` (Localhost routing only) |

---

## 🚀 Installation & Local Setup

Because this system is designed for air-gapped environments, all dependencies and models must be downloaded locally before deployment.

### 1. Clone the Repository
```bash
git clone [https://github.com/SREEVELANM/geomine_ai.git](https://github.com/SREEVELANM/geomine_ai.git)
cd geomine_ai/geomine_ai


### 2. Install Python Dependencies

Ensure you have Python 3.9+ installed. Create a virtual environment (recommended) and install the required packages:

```bash
pip install -r requirements.txt

```

*(If `requirements.txt` is missing, manually run: `pip install streamlit pandas folium streamlit-folium numpy requests`)*

### 3. Install and Start Ollama (Local LLM)

GeoMine AI requires a local instance of Ollama to function as the AI brain.

1. Download Ollama from [ollama.com](https://ollama.com/?utm_source=gemini).
2. Open a separate terminal window and pull the Llama-3 model:

```bash
ollama run llama3

```

*Keep this terminal window running in the background. It serves as the local API on port `11434`.*

### 4. Launch the Dashboard

In your primary terminal, launch the Streamlit application:

```bash
streamlit run app.py

```

The GeoMine AI dashboard will automatically open in your default browser at `http://localhost:8501`.

---

## 🧭 Navigation Breakdown

1. **Intelligence & GIS Map:** The primary interface for querying data. Toggle the PQ Auto-Framer and view geographical representations of the queried mining blocks.
2. **Multi-Modal Ingestion:** The upload zone for ingesting new historical archives. Processes PDFs, spreadsheets, and images, instantly adding them to the FAISS index.
3. **Contradiction Engine:** The reconciliation dashboard where administrators resolve flagged discrepancies between legacy surveys and modern calibrations.
4. **Secure AI Chat Assistant:** A free-form chatbot for interactive, multi-turn conversations regarding the ingested geological data.
5. **System Telemetry:** Real-time monitoring of vector chunk count, LLM latency, data leakage risk, and downloadable secure CSV audit logs.

---

## 👥 Team

**The Rookiez**
*Participating in Smart India Hackathon (SIH 2026)*

* **Theme:** Smart Automation
* **Category:** Software
* **Problem Statement:** AI-Powered Geological Reporting System (SIH26023)

---

*Disclaimer: The data used in this prototype (reserves, block names, mock PDFs) is for demonstration purposes only and does not represent classified internal metrics of CMPDI or NLC India Limited.*

```

```
