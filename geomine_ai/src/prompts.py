
# Parliamentary Question (PQ) Framing Directive
PQ_SYSTEM_PROMPT = """You are an AI Geological Secretary serving the Ministry of Coal, Government of India.
Your objective is to produce precise, authoritative answers adhering strictly to official Indian Parliamentary format.

Mandatory Directives:
1. Always format output using the official Lok Sabha / Rajya Sabha Starred Question layout.
2. Structure sections explicitly into: (a) Reserve & Yield Assessment, and (b) Stratigraphic & Cross-Validation Notes.
3. Cite verified borehole assay numbers, depth intervals, and coal grades (e.g., Grade W-II Coking Coal).
4. Never extrapolate unverified assumptions beyond the retrieved air-gapped context.
"""

def build_pq_user_prompt(target_block: str, query: str, context_chunks: list[str]) -> str:
    """Combines retrieved vector chunks into an official PQ draft query."""
    formatted_context = "\n---\n".join(context_chunks)
    return f"""PARLIAMENTARY INQUIRY REGARDING: {target_block}
OFFICIAL QUERY: {query}

GROUND-TRUTH ARCHIVAL PASSAGES:
{formatted_context}

Draft the starred question reply precisely adhering to Ministry of Coal norms."""

# Contradiction Detection Prompt
CONTRADICTION_PROMPT = """Analyze the two historical mining records provided below.
Flag whether there is a numerical or geological anomaly between the legacy baseline and modern assay.

Record 1: {record_a}
Record 2: {record_b}

Output format:
- Conflict Status: [DETECTED / CONSISTENT]
- Variance Delta: [Quantify difference in MMT or thickness]
- Recommendation: [Suggested reconciliation priority]
"""