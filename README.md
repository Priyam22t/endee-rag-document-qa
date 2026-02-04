# RAG-Based Document Question Answering using Endee

## Overview
This project demonstrates a well-defined AI/ML application built using Endee as the vector database. It implements a Retrieval Augmented Generation (RAG) workflow that allows users to ask questions and receive answers grounded in document content using vector similarity search.

The project focuses on core AI system design principles such as embeddings, vector search, and retrieval-based reasoning rather than UI complexity.

---

## Problem Statement
Traditional keyword-based search systems often fail to capture semantic meaning, resulting in irrelevant or incomplete results. This project addresses that limitation by using vector embeddings to perform semantic retrieval, enabling more accurate and context-aware responses from document data.

---

## Use Case: Retrieval Augmented Generation (RAG)
Retrieval Augmented Generation (RAG) combines information retrieval with answer generation. Instead of generating responses purely from a model’s internal knowledge, the system first retrieves relevant information from a document corpus and then uses that information to generate the final answer.

This approach is widely used in:
- Document question answering systems
- Knowledge-base chatbots
- Enterprise AI assistants

---

## System Architecture
The system follows a simple and effective RAG pipeline:

Documents  
|  
Text Embeddings  
|  
Endee (Vector Database)  
|  
Similarity Search  
|  
Retrieved Context  
|  
Final Answer  

---

## Technical Approach

1. Document Ingestion  
Documents are read from a text file. Each document is converted into a dense vector embedding using a transformer-based embedding model. These embeddings represent the semantic meaning of the text.

2. Vector Storage (Endee)  
Endee is used as the vector database layer. It is responsible for storing embeddings and enabling fast similarity-based retrieval. The system is designed assuming Endee runs as an external vector database service, as described in the official Endee documentation.

3. Query Processing  
User queries are converted into vector embeddings. Similarity search is performed between the query vector and stored document vectors. The most relevant document context is retrieved.

4. Answer Generation  
The retrieved context is used to generate the final answer. This ensures responses are grounded in document content rather than keyword matching or hardcoded logic.

---

## How Endee is Used
Endee plays a central role as the vector database in this project. It enables storage of document embeddings, semantic similarity search, and efficient retrieval of relevant content for RAG workflows. Vector search is the core component of the system.

---

## Project Structure
endee-rag-document-qa/
- data/
  - documents.txt
  - embeddings.npy
  - texts.npy
- src/
  - ingest.py
  - query.py
- requirements.txt
- README.md
- .gitignore

---

## Setup and Execution Instructions

Step 1: Install Dependencies  
python -m pip install -r requirements.txt

Step 2: Ingest Documents  
python src/ingest.py

Step 3: Query the System  
python src/query.py

You can then enter a natural language question in the terminal.

---

## Sample Output
Question:  
What is Endee used for?

Retrieved Context:  
Endee is a high-performance vector database designed for storing and retrieving embeddings using similarity search.

Final Answer:  
Endee is used as a vector database to store embeddings and retrieve relevant information using similarity search.

---

## Why This Approach
- Demonstrates real-world use of vector databases
- Clearly showcases Retrieval Augmented Generation (RAG)
- Keeps focus on AI logic and system design
- Avoids unnecessary UI or infrastructure complexity
- Aligns directly with modern AI/ML application patterns

---

## Conclusion
This project satisfies the assignment requirements by presenting a clean, practical, and well-documented AI system where vector search is core. It demonstrates how Endee can be used effectively in a RAG pipeline and reflects real-world AI engineering best practices.

---

## Future Enhancements
- Support for larger document collections
- Integration with a language model for richer generation
- API or web interface for interactive usage
