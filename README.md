---
title: Finance_Agent
app_file: app.py
sdk: gradio
sdk_version: 5.34.2
---
# Finance-AI-Agent

# 💼 Finance AI Agent

A prototype conversational AI agent that understands and answers finance-related questions using your company's documents. Built for enterprise-style use cases, the agent can process structured and unstructured data (CSV, PDF, image files), extract insights, and provide conversational answers via a chat interface.

---

## 🚀 Features

- 💬 Natural language interface powered by a large language model (LLM)
- 🔍 Retrieval-Augmented Generation (RAG) over company files
- 📁 Supports questions based on:
  - Scanned financial documents (Image)
  - PDFs (basic support)
- 🧠 Embeds documents into a vector store for semantic search
- ⚙️ Local and cloud deployment support with Gradio UI

---

## ⚠️ Important Notes

> 📌 **This is a prototype. The agent only answers questions based on the files currently uploaded in the repository.**
>
> ✅ A full-fledged database or knowledge base is not yet integrated.
>
> 🚫 If you ask questions that are not related to the example documents, the agent may respond with:  
> `"I don't know the answer based on the provided context."`

---

## 📁 Files Included

- `main.py`: Core agent logic and LLM interaction
- `vector.py`: Document processing and vector database (Chroma) setup
- `app.py` or `gradio_app.py`: Gradio interface to interact with the agent
- `batch1-0484.jpeg`: Example scanned documents
- `batch1-0483.pdf`: Example PDF file

---

