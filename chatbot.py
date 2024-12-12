from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

# Load environment variables from .env file
load_dotenv()

# Access the API key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

st.header("Chatbot")

# Upload a PDF file
with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF file and start asking questions", type="pdf")

# Extract text from PDF
if file is not None:
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
        #st.write(text)

# Break it into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    # st.write(chunks)

# Generating embeddings
    # embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    embeddings = OpenAIEmbeddings()

# Creating vector storev - FAISS (Facebook AI Similarity Search)
    vector_store = FAISS.from_texts(chunks, embeddings)

# Get User question
    user_question = st.text_input("Type your question here")

# Do similarity search
    if user_question:
        match = vector_store.similarity_search(user_question)
        # st.write(match)

        # Define the LLM
        llm = ChatOpenAI(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0,
            max_tokens=1000,
            model_name="gpt-3.5-turbo"
        )

# Output results
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents=match, question=user_question)
        st.write(response)
