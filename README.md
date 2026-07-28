# 🤖 DocQuery AI

An AI-powered Document Intelligence Assistant that enables users to upload PDF documents and ask natural language questions using Retrieval-Augmented Generation (RAG). The application retrieves relevant document context using semantic search and generates accurate responses with Google Gemini, while providing page-level source citations.

---

## 🚀 Features

- 📄 Upload and process PDF documents
- 🤖 Ask questions in natural language
- 🔍 Semantic search using FAISS vector database
- 🧠 Google Gemini powered responses
- 📑 Page-level source citations
- 💾 Persistent vector database
- ⚡ Duplicate document detection using file hashing
- 💬 Clean Streamlit chat interface
- 🛡️ Error handling and retry mechanism

---

## 🏗️ System Architecture

```text
                 User
                   │
                   ▼
            Streamlit Frontend
                   │
                   ▼
            PDF Upload & Processing
                   │
                   ▼
          Text Extraction (PyPDF)
                   │
                   ▼
      Recursive Text Chunking
                   │
                   ▼
 SentenceTransformer Embeddings
                   │
                   ▼
           FAISS Vector Store
                   │
         Semantic Similarity Search
                   │
                   ▼
            Google Gemini LLM
                   │
                   ▼
      Answer + Source Page Citation
```

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Frontend | Streamlit |
| LLM | Google Gemini |
| Framework | LangChain |
| Embeddings | Sentence Transformers |
| Vector Database | FAISS |
| PDF Processing | PyPDF |
| Environment | Python Dotenv |
| Future Backend | FastAPI |

---

## 📂 Project Structure

```text
AI-Document-Assistant/
│
├── backend/
│   ├── chatbot.py
│   ├── config.py
│   ├── embeddings.py
│   ├── hash_utils.py
│   ├── metadata.py
│   ├── pdf_reader.py
│   ├── rag.py
│   ├── retriever.py
│   ├── text_splitter.py
│   ├── utils.py
│   └── vector_store.py
│
├── tests/
├── vectorstore/
├── app.py
├── requirements.txt
├── README.md
└── .env.example
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Ishitapatel1402/AI-Document-Assistent.git
```

Move into the project

```bash
cd AI-Document-Assistent
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_API_KEY
MODEL_NAME=gemini-2.5-flash
```

Run the application

```bash
streamlit run app.py
```

---


## 🎯 Future Enhancements

- Multi-document support
- OCR support for scanned PDFs
- Conversation memory
- Hybrid Search (BM25 + FAISS)
- Streaming LLM responses
- User Authentication
- Docker deployment
- FastAPI backend
- Cloud storage integration

---

## 👩‍💻 Author

**Ishita Patel**

- GitHub: https://github.com/Ishitapatel1402


---
