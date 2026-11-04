# AI-Powered Resume Screen & Ranking Pipeline 📊💼

An enterprise-ready, locally hosted human resources technology pipeline that automates candidate screening. By replacing legacy, easily-gamed keyword-matching architectures with mathematical **Natural Language Processing (NLP)**, this system reads unstructured candidate data and scores portfolios against target job requirements with contextual precision.

Developed entirely in **Python**, utilizing **Streamlit** for the interface and **scikit-learn** for vector-space algorithms.

---

## 🚀 Core Features

- **Messy Data Ingestion:** Programmatically processes and strips unstructured textual data from raw `.pdf` uploads.
- **Semantic Vector Mapping:** Implements a `TfidfVectorizer` pipeline to extract important terms while discarding irrelevant linguistic noise.
- **Advanced Proximity Evaluation:** Uses **Cosine Similarity** matrices to calculate the geometric distance between resume metrics and job descriptions.
- **HR Scaled Scoring Engine:** Applies a non-linear mathematical adjustment to sparse document vectors, converting raw metrics into intuitive, human-readable match percentages.
- **Real-Time Leaderboard Dashboard:** Displays a clean, dynamically sorted applicant tracking system leaderboard directly inside a web interface.

---

## 🏛️ System Architecture

```text
[Resume PDF Uploads] ➔ [PyPDF Data Extraction] ➔ [TF-IDF Vector Space Mapping] ➔ [Cosine Similarity Engine] ➔ [HR Scaled Ranking Matrix] ➔ [Streamlit UI Leaderboard]
```

---

## 🧰 Tech Stack

- **Core Language:** Python 3.11+
- **Frontend Dashboard:** Streamlit
- **Text & PDF Parsing:** PyPDF
- **Mathematical ML Framework:** scikit-learn (Numpy/SciPy backend)

---

## 💻 Getting Started Locally

Follow these instructions to run this project seamlessly on your local machine using **Command Prompt (CMD)** inside Windows.

### 1. Clone the Directory Setup
Ensure your local project directory structure matches this exactly:
```text
AI-Powered Resume Screen & Ranking Pipeline/
│
├── requirements.txt      # Structural external dependencies
├── utils.py              # Text extraction and vector calculation engine
├── app.py                # Streamlit live frontend application script
└── README.md             # Project documentation portfolio overview
```

### 2. Configure the Isolated Virtual Environment
Open your terminal inside the project directory and build your clean dependencies container:
```cmd
python -m venv venv
```

### 3. Install Target Requirements Blueprint
Run this specific command to point your project directly to the local Python binary and download the packages:
```cmd
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 4. Boot Up the Live Dashboard Application
Launch your programmatic local server environment using:
```cmd
.\venv\Scripts\python.exe -m streamlit run app.py
```
*Your system will automatically launch a web interface profile at `http://localhost:8501`.*

---

## 🧠 Data Engineering Insights

### The Sparsity Challenge & HR Scaling Solution
In natural language documentation, two completely different text files share very few identical words, creating a highly **sparse matrix**. A raw mathematical similarity calculation might score a strong candidate profile at an underwhelming **21%**. 

To align data engineering metrics with human recruitment expectations, this pipeline utilizes an **HR Compatibility Scaling Engine** driven by a non-linear scaling adjustment:

$$\text{Final Score} = \min(\sqrt{\text{Raw Cosine Similarity}} \times 100, 100.0)$$

This adjustment shifts sparse coordinate tracking into realistic, user-friendly distributions (e.g., boosting a raw `21.05%` mathematical overlap to a readable `45.88%` match rating) without altering candidate ranking order.
