# College Admission Agent (RAG-Based)

This project is a Retrieval-Augmented Generation (RAG) based AI assistant designed to simplify the college admission process. It uses a knowledge base of admission FAQs to provide accurate, real-time responses to student queries in natural language.

## Features
- Ask questions about admission policies, deadlines, fee structures, and eligibility.
- Uses Retrieval-Augmented Generation (RAG) for accurate responses.
- Real-time interaction using a local web UI.
- Powered by IBM Cloud and Large Language Models (LLMs).
- Lightweight and easy to deploy.

## Technologies Used
- Python (Flask)
- IBM Cloud & Watson/Granite Models
- Retrieval-Augmented Generation (RAG)
- HTML, CSS, JavaScript (Frontend)

## How It Works
1. User asks a question in natural language.
2. The system searches the `admission_faq.json` file to find the most relevant answer.
3. The selected context is sent to an LLM (via IBM Granite or other) to generate a refined answer.
4. The result is displayed to the user.
