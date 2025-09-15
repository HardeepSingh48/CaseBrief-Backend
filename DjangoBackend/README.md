CaseBrief AI Backend (Django)
This is the dedicated AI and machine learning backend for the CaseBrief application. Built with Python and Django, this service exposes a powerful set of REST APIs to perform complex analysis on legal documents.

✨ Core AI Features
This server is the engine behind CaseBrief's intelligent capabilities:

Conversational AI (RAG): Powers the AI chat feature using a Retrieval-Augmented Generation (RAG) model to provide accurate, context-aware answers based on user documents.

Automated Text Summarization: Generates concise and structured summaries of lengthy legal texts.

Judgment Prediction: Analyzes the content of a case file to predict the likely outcome.

Legal Statute Extraction: Identifies and explains relevant legal statutes mentioned within a document.

🚀 Technology Stack
Framework: Django & Django Rest Framework

AI/ML Libraries: LangChain, NLTK, Scikit-learn

LLM Integration: Groq for high-speed inference.

Embeddings: Hugging Face models for text embeddings.

⚙️ Getting Started
Prerequisites
Python and pip

Access to API keys for the AI services you intend to use (e.g., Hugging Face, Groq).

Installation & Setup
Navigate to the Directory:

cd sihbackend/DjangoBackend

Create and Activate a Virtual Environment:
It is highly recommended to use a virtual environment for Python projects.

# Create the environment
python -m venv venv

# Activate it (macOS/Linux)
source venv/bin/activate

# On Windows, use:
# .\venv\Scripts\activate

Install Dependencies:
Install all the required Python packages from the requirements.txt file.

pip install -r requirements.txt

Configure Environment Variables:
Create a .env file in the DjangoBackend directory to store your secret API keys.

HUGGINGFACEHUB_API_TOKEN=your_hugging_face_api_token
GROQ_API_KEY=your_groq_api_key

Run Database Migrations:
Apply the necessary database schema for the Django application.

python manage.py migrate

Running the Server
Start the Django development server.

python manage.py runserver

The AI server will now be running and ready to process requests, typically on http://localhost:8000.