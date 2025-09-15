# ⚖️ CaseBrief AI Backend (Django)

This is the **dedicated AI and machine learning backend** for the CaseBrief application.
Built with **Python** and **Django**, it exposes powerful REST APIs to perform complex analysis on legal documents.

---

## ✨ Core AI Features

This backend powers CaseBrief’s intelligent capabilities:

* **Conversational AI (RAG)**
  Retrieval-Augmented Generation (RAG) model for context-aware legal Q\&A.

* **Automated Text Summarization**
  Generate concise and structured summaries of lengthy case documents.

* **Judgment Prediction**
  Predict likely outcomes based on case file content.

* **Legal Statute Extraction**
  Identify and explain relevant statutes within uploaded documents.

---

## 🚀 Technology Stack

* **Framework:** Django & Django REST Framework
* **AI/ML Libraries:** LangChain, NLTK, Scikit-learn
* **LLM Integration:** Groq (for high-speed inference)
* **Embeddings:** Hugging Face models

---

## ⚙️ Getting Started

### 🔑 Prerequisites

* [Python](https://www.python.org/) & pip installed
* API keys for the AI services you intend to use (e.g., **Hugging Face**, **Groq**)

---

### 📥 Installation & Setup

1. **Navigate to the Backend Directory**

   ```bash
   cd sihbackend/DjangoBackend
   ```

2. **Create & Activate a Virtual Environment**

   ```bash
   # Create environment
   python -m venv venv

   # Activate (macOS/Linux)
   source venv/bin/activate

   # Activate (Windows)
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the `DjangoBackend` directory:

   ```env
   HUGGINGFACEHUB_API_TOKEN=your_hugging_face_api_token
   GROQ_API_KEY=your_groq_api_key
   ```

5. **Run Database Migrations**

   ```bash
   python manage.py migrate
   ```

---

### ▶️ Running the Server

Start the Django development server:

```bash
python manage.py runserver
```

The AI backend will now be running at:
👉 [http://localhost:8000](http://localhost:8000)

---

## 📌 Notes

* Ensure your **frontend** and **Node.js backend** are properly configured to connect to this Django AI backend.
* Keep your `.env` file **private** and never commit API keys to version control.

---

## 📜 License

This project is licensed under the **MIT License**.
