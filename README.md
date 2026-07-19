# 📚 Internal Knowledge Base RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built with **LangChain**, **FastAPI**, and **Next.js** that answers questions from a predefined set of internal documents (PDFs/Markdown files).

The chatbot retrieves relevant document chunks from a **Pinecone Vector Database** and generates accurate responses using either **Google Gemini** or an **Ollama** local model.

---

# 🚀 Features

- 📄 Load PDF and Markdown documents
- ✂️ Intelligent document chunking using LangChain Text Splitters
- 🔎 Semantic search with Pinecone Vector Database
- 🤖 Dual LLM support
  - Google Gemini
  - Ollama (Local)
- 🔀 Runtime model switching
- 💬 Conversation-aware responses
- 🧠 Last 10 messages included as conversational context
- 📑 Source document citations
- ⚡ FastAPI backend
- 🎨 Next.js frontend
- 🔗 REST API integration

---

# 🛠 Tech Stack

## Frontend

- Next.js 16
- React
- TypeScript
- Axios
- Tailwind CSS

## Backend

- FastAPI
- LangChain
- Google Gemini
- Ollama
- Pinecone
- HuggingFace Endpoint Embeddings
- Pydantic

---

# 📂 Project Structure

```
rag-chatbot/
│
├── backend/
│   │
│   ├── app/
│   │   ├── config/
│   │   ├── loaders/
│   │   ├── splitters/
│   │   ├── embeddings/
│   │   ├── vectorstores/
│   │   ├── retrievers/
│   │   ├── models/
│   │   ├── prompts/
│   │   ├── chains/
│   │   ├── services/
│   │   ├── router/
│   │   ├── schemas/
│   │   ├── scripts/
│   │   └── main.py
│   │
│   ├── documents/
│   ├── .env
│   └── requirements.txt
│
└── frontend/
    │
    ├── app/
    │   ├── components/
    │   ├── hooks/
    │   ├── services/
    │   ├── types/
    │   ├── page.tsx
    │   └── layout.tsx
    │
    ├── public/
    └── package.json
```

---

# 🧠 RAG Pipeline

```
                Documents
         (PDF / Markdown Files)
                    │
                    ▼
         LangChain Document Loaders
                    │
                    ▼
          Recursive Text Splitter
                    │
                    ▼
      HuggingFace Embedding Model
                    │
                    ▼
          Pinecone Vector Database
                    │
────────────────────────────────────────
               User Question
                    │
                    ▼
         Retrieve Top-3 Similar Chunks
                    │
                    ▼
      Previous 10 Chat Messages
                    │
                    ▼
         ChatPromptTemplate
                    │
                    ▼
      Gemini / Ollama (Toggle)
                    │
                    ▼
          StrOutputParser
                    │
                    ▼
              Final Response
```

---

# ⚙️ Environment Variables

Create a `.env` file inside the backend.

```env
GOOGLE_API_KEY=

PINECONE_API_KEY=

PINECONE_INDEX_NAME=rag-chatbot

MODEL_PROVIDER=gemini

GEMINI_MODEL=gemini-3.1-flash-lite

HUGGINGFACE_API_KEY=

REPO_ID=

OLLAMA_MODEL=llama3.2
```

---

# 📦 Backend Installation

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the server.

```bash
uvicorn app.main:app --reload
```

Backend runs at

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

---

# 💻 Frontend Installation

Install packages.

```bash
npm install
```

Run the development server.

```bash
npm run dev
```

Frontend runs at

```
http://localhost:3000
```

---

# 📚 Document Ingestion

Documents are stored inside

```
backend/documents/
```

Supported formats:

- PDF
- Markdown

Run the ingestion script.

```bash
python -m app.scripts.test_ingest
```

The pipeline:

```
Documents
    │
    ▼
Loaders
    │
    ▼
Chunking
    │
    ▼
Embeddings
    │
    ▼
Pinecone
```

Documents are indexed **once** during setup.

No document upload functionality is provided to end users.

---

# 💬 Chat Flow

```
User Question
      │
      ▼
Frontend
      │
      ▼
FastAPI
      │
      ▼
Retriever
      │
      ▼
Top-3 Context Chunks
      │
      ▼
Prompt Template
      │
      ▼
Gemini / Ollama
      │
      ▼
Answer
      │
      ▼
Frontend
```

---

# 🤖 Supported Models

### Google Gemini

```
gemini-3.1-flash-lite
```

### Ollama

Example:

```
llama3.2
```

The frontend allows switching between both models.

---

# 🧩 LangChain Components Used

- Document Loaders
- Recursive Character Text Splitter
- HuggingFace Embeddings
- Pinecone Vector Store
- Retriever
- ChatPromptTemplate
- MessagesPlaceholder
- Runnable Chains
- StrOutputParser
- Gemini Chat Model
- Ollama Chat Model

---

# 💬 Conversation Handling

This project does **not** persist chat history.

Instead:

- Chat history exists only in the frontend.
- The last **10 messages** are sent with every request.
- The backend injects them into the prompt for conversational continuity.

No database is used for storing conversations.

---

# 📡 API

## POST

```
/v1/chat
```

### Request

```json
{
  "question": "How many sick leaves are allowed?",
  "provider": "gemini",
  "history": [
    {
      "role": "user",
      "content": "Hello"
    },
    {
      "role": "assistant",
      "content": "Hi! How can I help you?"
    }
  ]
}
```

---

### Response

```json
{
  "answer": "Employees are entitled to 12 sick leaves per year.",
  "sources": [
    {
      "source": "HR Policy.pdf",
      "page": 4
    }
  ]
}
```

---

# 🔍 Retrieval Strategy

- Cosine Similarity
- Top K = 3
- Pinecone Serverless Index
- 768-dimensional embeddings

---

# 📝 AI Usage Log

AI tools were used to assist with:

- Project architecture
- API design
- LangChain pipeline
- Prompt engineering
- FastAPI development
- Next.js development
- TypeScript interfaces
- Debugging
- Documentation

---

# 📌 Future Improvements

- Streaming responses
- Authentication
- Persistent chat history
- Admin document upload
- Multi-user support
- Hybrid search
- Reranking
- Citation highlighting

---

# 👨‍💻 Author

**Name:** *Your Name*

---

# 📄 License

This project is intended for educational purposes.
