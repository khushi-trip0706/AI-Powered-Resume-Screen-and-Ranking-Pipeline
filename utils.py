import math
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(pdf_file):
    """Extracts text content page-by-page from an uploaded PDF file."""
    try:
        reader = PdfReader(pdf_file)
        extracted_text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_text += page_text + " "
        return extracted_text.strip()
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def calculate_match_score(resume_text, job_description):
    """
    Vectorizes raw text assets and computes raw Cosine Similarity.
    Applies a mathematical scaling factor to translate sparse document 
    vectors into intuitive, human-readable match percentages.
    """
    if not resume_text.strip() or not job_description.strip():
        return 0.0
        
    documents = [resume_text, job_description]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Calculate the similarity matrix grid
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    # CRITICAL FIX: Extract the exact row 0, column 0 coordinate value directly from the matrix
    raw_similarity = float(similarity_matrix[0][0])
    
    if raw_similarity <= 0:
        return 0.0
        
    # --- HR COMPATIBILITY SCALING ENGINE ---
    # Using square root handles the sparse nature of natural language documents,
    # cleanly mapping technical overlaps into highly readable hiring scores.
    boosted_score = math.sqrt(raw_similarity) * 100
    
    # Guarantee boundary ceiling protection
    final_score = min(boosted_score, 100.0)
    
    return round(final_score, 2)
