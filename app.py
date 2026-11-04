import streamlit as st
from utils import extract_text_from_pdf, calculate_match_score

# Apply global page layout attributes
st.set_page_config(page_title="AI Resume Screen Dashboard", page_icon="📊", layout="wide")

st.title("📊 AI-Powered Resume Screen & Ranking Pipeline")
st.markdown("---")

# Segment interface space into functional workspace columns
col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("📝 Job Requirements Configuration")
    job_description = st.text_area(
        "Paste target Job Description requirements here:", 
        placeholder="e.g., Seeking a Python Backend Engineer with expertise in ML modeling, VS Code, Git, and data pipeline construction...",
        height=250
    )
    
    st.subheader("📁 Candidate Profile Batch Upload")
    uploaded_files = st.file_uploader(
        "Upload candidate resumes (PDF format only):", 
        type=["pdf"], 
        accept_multiple_files=True
    )

with col2:
    st.subheader("🏆 Weighted Compatibility Leaderboard")
    
    # Action pipeline execution block
    if st.button("Execute Pipeline Screening", type="primary"):
        if not job_description.strip():
            st.warning("⚠️ Please provide a valid target job description.")
        elif not uploaded_files:
            st.warning("⚠️ Please upload at least one candidate resume PDF file.")
        else:
            leaderboard_data = []
            
            # Setup programmatic visual progression tracking indicator
            progress_bar = st.progress(0)
            
            for index, file in enumerate(uploaded_files):
                # Phase 1: Extract string metrics from files
                resume_text = extract_text_from_pdf(file)
                
                # Phase 2: Compute weighted alignment matrix scores
                score = calculate_match_score(resume_text, job_description)
                
                # Phase 3: Track metrics inside collection array
                leaderboard_data.append({
                    "Rank": 0,  # Fixed: Replaced semicolon with a proper comma
                    "Candidate / Filename": file.name,
                    "Weighted Similarity Match": f"{score}%",
                    "_raw_score": score  # Internal sorting variable prefix
                })
                
                # Smooth interactive updates to status element
                progress_bar.progress((index + 1) / len(uploaded_files))
            
            # Sort raw dictionary mapping values based on vector weight scores
            leaderboard_data.sort(key=lambda x: x["_raw_score"], reverse=True)
            
            # Populate official human-readable ranking positions and clean private keys
            for position, entry in enumerate(leaderboard_data, start=1):
                entry["Rank"] = f"#{position}"
                del entry["_raw_score"]
                
            st.success("✅ Semantic parsing and weighted scoring matrix operations finished successfully!")
            
            # Print tabular layout data directly to screen dashboard
            st.table(leaderboard_data)
