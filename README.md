# 🤖 AI Duplicate Question Detection System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/NLP-Sentence--BERT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Model-LightGBM-yellow?style=for-the-badge">
  <img src="https://img.shields.io/badge/Accuracy-86.7%25-brightgreen?style=for-the-badge">
</p>

An NLP-powered web application that detects whether two questions are semantically similar using **Sentence-BERT embeddings** and a **LightGBM classifier**.

The system evolved through multiple NLP approaches, achieving **86.7% accuracy** using transformer-based semantic features.

---

## 🚀 Live Demo
🔗 YouTube Link:https://youtu.be/GsTny0eWJr8?si=I5u-xDOjtX3LovQ8 


---

## 📌 Problem Statement

Online Q&A platforms like Quora often receive duplicate questions that are phrased differently but have the same meaning.

Example:
Q1: How can I learn Python?
Q2: What is the best way to study Python?


Although the wording differs, the intent is the same.  
This project detects such duplicate questions using machine learning and NLP.

---

## 🧠 How the System Works

User Input
↓
Sentence-BERT Embeddings
↓
Cosine Similarity + Feature Vector
↓
LightGBM Classifier
↓
Duplicate / Not Duplicate


### Step-by-step pipeline
1. User enters two questions.
2. Sentence-BERT converts each question into a **768-dimensional embedding**.
3. Cosine similarity between embeddings is calculated.
4. Embeddings and similarity score form a **1537-feature vector**.
5. LightGBM classifier predicts:
   - Duplicate
   - Not Duplicate
6. Result is displayed with a confidence score.

---

## 🔬 Model Development Journey

| Approach | Model | Accuracy |
|----------|-------|----------|
| Bag-of-Words | Random Forest | 78.6% |
| TF-IDF | Random Forest | 80.0% |
| Sentence-BERT + Feature Engineering | LightGBM | **86.7%** |

### Why accuracy improved
- **BoW:** Only counts words
- **TF-IDF:** Weighs important words
- **Sentence-BERT:** Understands sentence meaning

Progression:
Lexical similarity → Semantic similarity


---

## ✨ Key Features

- Semantic similarity using Sentence-BERT
- LightGBM classifier for high accuracy
- Real-time predictions with confidence score
- Interactive analytics dashboard
- Prediction history tracking
- Secure login system
- Modern SaaS-style UI

---

## 🛠 Tech Stack

### Machine Learning & NLP
- Python
- Sentence-Transformers (Sentence-BERT)
- LightGBM
- Scikit-learn
- NumPy
- Pandas

### Frontend & Deployment
- Streamlit
- Plotly (analytics dashboard)
- GitHub
- Streamlit Cloud

---

## 📂 Project Structure

AI-Duplicate-Detection-Powered-by-NLP/
│
├── app.py
├── helper.py
├── model.pkl
├── users.json
├── requirements.txt
│
├── pages/
│ ├── 1_Predict.py
│ ├── 2_History.py
│ └── 3_Analytics.py
│
└── notebooks/


---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/ayu-sh87/AI-Duplicate-Detection-Powered-by-NLP.git
cd AI-Duplicate-Detection-Powered-by-NLP

2. Install dependencies
pip install -r requirements.txt

3.Run the app
streamlit run app.py

📊 Dataset
Source: Quora Question Pairs dataset
Contains pairs of questions with duplicate labels
Human-annotated (may contain some noise)

📈 Future Improvements
Cross-validation and hyperparameter tuning
Transformer-based deep learning classifier
Real user feedback for accuracy tracking
Docker-based deployment
REST API for integration

📸 Screenshots
Add screenshots of your app here
Example:

screenshots/predict.png
screenshots/analytics.png

👨‍💻 Author
Ayush Singh
GitHub: https://github.com/ayu-sh87
LinkedIn: (Add your LinkedIn link)
⭐ Support
If you like this project:
Give it a ⭐ on GitHub
Share it on LinkedIn










