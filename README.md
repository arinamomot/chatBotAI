# ChatBotAI Implementation Guide

This guide explains how to set up and implement a chatbot using OpenAI's API with additional tools for creating an interactive interface and handling embeddings.

<img width="1498" alt="Screenshot 2024-12-12 at 16 25 35" src="https://github.com/user-attachments/assets/2c45aa84-477e-4e59-8c10-e6247ec1b1db" />


---

## Prerequisites

1. **Generate OpenAI API Key**  
   - Visit [OpenAI API Keys](https://platform.openai.com/api-keys) to generate your API key.  

2. **Set Up OpenAI Account**  
   - Access the [OpenAI Dashboard](https://platform.openai.com) and upgrade your account to a paid plan. Add a minimum of $5 to your balance to increase usage limits.

3. **Install Python**  
   Ensure Python 3 is installed on your machine.

---

## Installation Steps

### 1. Create and Activate a Virtual Environment
1. Create a virtual environment:
   ```bash
   python3 -m venv myenv
   ```
2. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```
   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```

### 2. Install Required Libraries
Run the following command to install the necessary packages:
```bash
pip install python-dotenv tiktoken streamlit pypdf2 langchain faiss-cpu
```

- **`python-dotenv`**: Manages environment variables.
- **`tiktoken`**: Tokenizes inputs for OpenAI models.
- **`streamlit`**: Creates UI for the chatbot.
- **`pypdf2`**: Reads PDF source files.
- **`langchain`**: Interface for using OpenAI services.
- **`faiss-cpu`**: Provides a vector store for embedding storage.

---

## Writing the Chatbot Code

1. Write the chatbot code (e.g., `chatbot.py`). Ensure the following elements are included:
   - OpenAI API integration.
   - Input and output handling for user queries.
   - Optional: Embedding storage for advanced query capabilities using FAISS.

---

## Running the Chatbot

1. Run the chatbot application using Streamlit:
   ```bash
   streamlit run /path/to/chatbot.py
   ```
   Replace `/path/to/chatbot.py` with the actual path to your chatbot script.

---

## Example Questions

Here are some sample questions you can ask the chatbot:

You can use the [U.S. Constitution PDF](https://constitutioncenter.org/media/files/constitution.pdf) as a knowledge base for queries.

- **General Queries:**
  - "Who can be the president of USA?"
  - "Can you summarize the process of election of the president of USA?"

- **Custom Queries:**
  - Adjust questions based on the embeddings or content processed by your chatbot.

---

## Additional Notes

- Ensure the API key is securely stored using `.env`.
- Regularly monitor your OpenAI usage to avoid exceeding limits.
- Experiment with the chatbot by enhancing its interface and adding new features.

For further details, refer to the [Streamlit Documentation](https://docs.streamlit.io/) and [LangChain Documentation](https://docs.langchain.com/).

---
