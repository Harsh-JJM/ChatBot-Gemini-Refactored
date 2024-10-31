# Import required libraries
import streamlit as st  # For creating web interface
import os  # For handling environment variables and file operations
from dotenv import load_dotenv  # For loading environment variables
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # For creating text embeddings
import google.generativeai as genai  # For accessing Google's generative AI models
from langchain_community.vectorstores import FAISS  # Vector store for similarity search
from langchain.chains.question_answering import load_qa_chain  # For building QA pipeline
from langchain_google_genai import ChatGoogleGenerativeAI  # For chat completions
from langchain.prompts import PromptTemplate  # For creating structured prompts
from googletrans import Translator  # For language translation
from sklearn.feature_extraction.text import TfidfVectorizer  # For text vectorization
from sklearn.metrics.pairwise import cosine_similarity  # For calculating text similarity
import json  # For handling JSON data

# Initialize environment and API configurations
load_dotenv()  # Load environment variables from .env file
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])  # Configure Google AI with API key

# Define constant values used throughout the application
EMBEDDING_MODEL = "models/embedding-001"  # Model for creating embeddings
LLM_MODEL = "gemini-1.5-flash"  # Large Language Model for chat
CHUNK_SIZE = 720  # Size of text chunks for processing
OVERLAP_SIZE = 150  # Overlap between chunks
CHAIN_TYPE = "stuff"  # Type of QA chain

# Load predefined questions and answers from JSON file
with open("suggested_questions.json", 'r') as file:
    qna_list = json.load(file)

# Initialize Google Translator for multi-language support
translator = Translator()

# Utility Functions
def load_css(file_path):
    """
    Load and apply custom CSS styling to the Streamlit interface.
    
    Args:
        file_path (str): Path to CSS file
    """
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def translate_text(text, target_language):
    """
    Translate text to specified target language.
    
    Args:
        text (str): Text to translate
        target_language (str): Target language code (e.g., 'en', 'hi')
    
    Returns:
        str: Translated text
    """
    if target_language == 'en':
        return text
    translation = translator.translate(text=text, dest=target_language)
    return translation.text

# Vector Store Operations
def load_faiss_vector_store():
    """
    Load FAISS vector store from local storage with embeddings.
    
    Returns:
        FAISS: Loaded vector store object
    """
    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)
    return FAISS.load_local("faiss_local", embeddings, allow_dangerous_deserialization=True)

# Conversation Chain Building
def build_conversational_chain(version=1):
    """
    Create QA chain with different prompting strategies based on version.
    
    Args:
        version (int): Version of the chain template (1 or 2)
    
    Returns:
        Chain: Configured QA chain
    """
    # Version 1: Strict context adherence with lower temperature
    if version == 1:
        template = """
        Answer the question as detailed as possible from the provided context. If the answer is not in the provided context, 
        say 'Answer is not available in the context'.
        Context:\n{context}\n
        Question:\n{question}\n
        Answer:
        """
        temperature = 0.3
    # Version 2: More flexible responses with higher temperature
    else:
        template = """
        Go through the entire text and answer the question in detail. Format the answer in paragraphs and points.
        Context:\n{context}\n
        Question:\n{question}\n
        Answer:
        """
        temperature = 0.6
    
    # Create and return the QA chain
    model = ChatGoogleGenerativeAI(model=LLM_MODEL, temperature=temperature)
    prompt = PromptTemplate(template=template, input_variables=["context", "question"])
    return load_qa_chain(model, chain_type=CHAIN_TYPE, prompt=prompt)

# Question Suggestion System
def suggest_similar_questions(user_question, qna_list, top_n=4):
    """
    Find similar questions from QnA list using TF-IDF and cosine similarity.
    
    Args:
        user_question (str): User's input question
        qna_list (list): List of predefined Q&A pairs
        top_n (int): Number of suggestions to return
    
    Returns:
        list: Top N similar questions
    """
    questions = [qna["question"] for qna in qna_list]
    vectorizer = TfidfVectorizer().fit_transform(questions + [user_question])
    vectors = vectorizer.toarray()
    
    user_vector = vectors[-1]
    question_vectors = vectors[:-1]
    
    cosine_similarities = cosine_similarity([user_vector], question_vectors).flatten()
    related_docs_indices = cosine_similarities.argsort()[-top_n:][::-1]
    
    return [questions[i] for i in related_docs_indices]

def get_answer_from_qna_list(qna_list, question):
    """
    Retrieve answer for a given question from QnA list.
    
    Args:
        qna_list (list): List of Q&A pairs
        question (str): Question to find answer for
    
    Returns:
        str: Answer to the question or not found message
    """
    for item in qna_list:
        if item.get("question") == question:
            return item.get("answer")
    return "Question not found."

# Query Processing
def process_user_query(user_question, language):
    """
    Process user question and generate response using vector store and QA chain.
    
    Args:
        user_question (str): User's input question
        language (str): Target language code
    """
    # Load vector store and perform similarity search
    faiss_store = load_faiss_vector_store()
    docs = faiss_store.similarity_search(user_question)
    
    # Try first chain version
    chain = build_conversational_chain(version=1)
    response = chain({"input_documents": docs, "question": user_question})
    
    # If no answer found, try second chain version
    if "answer is not available in the context" in response["output_text"].lower():
        chain = build_conversational_chain(version=2)
        response = chain({"input_documents": docs, "question": user_question})
    
    # Translate response and display
    output_text = translate_text(response["output_text"], language)
    with st.chat_message("assistant"):
        st.markdown(output_text)
    
    # Generate and store similar question suggestions
    suggestions = suggest_similar_questions(user_question, qna_list)
    st.session_state.suggested_questions = suggestions

# Main Application
def main():
    """
    Main function to run the Streamlit application interface.
    Handles:
    - Language selection
    - User input processing
    - Similar question suggestions
    - Multi-language support
    """
    # Setup sidebar configuration
    st.sidebar.header("Settings")
    st.sidebar.title("Jal Jeevan Mission Chatbot")
    
    # Language selection dropdown
    language = st.sidebar.selectbox(
        "Select Language",
        ("English", "Hindi", "Kannada", "Tamil", "Telugu", "Bengali", "Marathi", "Gujarati", "Malayalam", "Punjabi")
    )
    
    # Language code mapping
    language_code = {
        "English": "en", "Hindi": "hi", "Kannada": "kn", "Tamil": "ta", "Telugu": "te", 
        "Bengali": "bn", "Marathi": "mr", "Gujarati": "gu", "Malayalam": "ml", "Punjabi": "pa"
    }

    # Initialize session state for suggested questions
    if "suggested_questions" not in st.session_state:
        st.session_state.suggested_questions = []

    # Main chat interface
    user_question = st.text_input("Enter your query for Chatbot")
    if user_question:
        st.info(f"Processing query for chatbot: '{user_question}'")
        process_user_query(user_question, language_code[language])

    # Display suggested questions section
    if st.session_state.suggested_questions:
        st.write("Here are some relevant questions you might find helpful:")
        if language_code[language] == "en":
            # English language handling
            selected_question = st.selectbox("Select a Question", st.session_state.suggested_questions)
            if selected_question:
                answer = get_answer_from_qna_list(qna_list, selected_question)
                st.markdown(answer)
        else:
            # Non-English language handling
            translated_questions = [translate_text(que, language) for que in st.session_state.suggested_questions]
            translated_qna = {translate_text(que, language): translate_text(get_answer_from_qna_list(qna_list, que), language) 
                            for que in st.session_state.suggested_questions}
            
            selected_question = st.selectbox("Select a Question", translated_questions)
            if selected_question:
                st.markdown(translated_qna[selected_question])

    # Add footer to sidebar
    st.sidebar.markdown("© JJM - IIM Bangalore Cell 2024")

# Application entry point
if __name__ == "__main__":
    main()