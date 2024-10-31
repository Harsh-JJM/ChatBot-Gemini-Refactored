# Import necessary libraries
import os  # For operating system operations like file handling
import re  # For regular expression operations
import fitz  # PyMuPDF for PDF processing
from dotenv import load_dotenv  # To load environment variables from .env file
from langchain_community.vectorstores import FAISS  # Vector database for storing embeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter  # For splitting text into chunks
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # Google's AI embeddings
import google.generativeai as genai  # Google's Generative AI tools

# Initialize environment and configurations
load_dotenv()  # Load environment variables from .env file

# Configure Google Generative AI with API key
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Define constant values used throughout the script
EMBEDDING_MODEL = "models/embedding-001"  # Model used for creating embeddings
CHUNK_SIZE = 720  # Size of each text chunk for processing
OVERLAP_SIZE = 150  # Overlap between chunks to maintain context
DATA_FOLDER = "Data"  # Folder containing PDF files to process


def get_pdf_text(pdf_file_path):
    """
    Extract text content from a PDF file.
    
    Args:
        pdf_file_path (str): Path to the PDF file
        
    Returns:
        str: Extracted text from the PDF
    """
    print(f"LOG: Extracting text from {pdf_file_path}")
    text = ""
    try:
        # Open PDF file using PyMuPDF
        pdf_file = fitz.open(pdf_file_path)
        # Iterate through each page and extract text
        for page_num in range(pdf_file.page_count):
            page = pdf_file.load_page(page_num)
            text += page.get_text()
        pdf_file.close()
    except Exception as e:
        print(f"Error reading {pdf_file_path}: {e}")
    
    return text


def get_clean_text(text):
    """
    Clean the extracted text by removing unwanted characters and formatting.
    
    Args:
        text (str): Raw text extracted from PDF
        
    Returns:
        str: Cleaned text ready for processing
    """
    print("LOG: Cleaning extracted text")
    # Remove numbers at the beginning of each line (often page numbers or line numbers)
    text = re.sub(r'^\d+\s*', '', text, flags=re.MULTILINE)
    # Remove escape sequences like \n, \t, etc.
    text = re.sub(r'\\[^\s]+', '', text)
    # Remove non-ASCII characters that might cause processing issues
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    
    return text.strip()


def get_text_chunks(text):
    """
    Split cleaned text into smaller, manageable chunks for processing.
    
    Args:
        text (str): Cleaned text to be split
        
    Returns:
        list: List of text chunks ready for vectorization
    """
    print("LOG: Splitting text into chunks")
    # Create text splitter with defined chunk size and overlap
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=OVERLAP_SIZE)
    # Split text into chunks
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    """
    Create and save a FAISS vector store from the text chunks.
    
    Args:
        text_chunks (list): List of text chunks to be vectorized
    """
    print("LOG: Creating FAISS vector store")
    # Initialize Google's AI embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)
    # Create vector store from text chunks
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    # Save the vector store locally for future use
    vector_store.save_local("faiss_local")
    print("LOG: FAISS vector store saved")


def process_pdfs_in_folder(folder_path):
    """
    Main processing pipeline that handles the entire workflow from PDF to vector store.
    
    Args:
        folder_path (str): Path to folder containing PDF files
    """
    all_text = ""  # Initialize empty string to store combined text from all PDFs

    # Iterate through each file in the specified folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):  # Process only PDF files
            file_path = os.path.join(folder_path, filename)
            print(f"LOG: Processing file: {file_path}")
            
            # Extract text from PDF
            raw_text = get_pdf_text(file_path)
            
            if raw_text:
                # Clean the extracted text
                clean_text = get_clean_text(raw_text)
                # Add cleaned text to collective text with spacing
                all_text += clean_text + "\n\n"
            else:
                print(f"LOG: No text found in {file_path}, skipping...")

    # Process combined text if any valid content was extracted
    if all_text:
        # Split combined text into chunks
        text_chunks = get_text_chunks(all_text)
        # Create and save vector store
        get_vector_store(text_chunks)
    else:
        print("LOG: No valid text found in any PDF, FAISS store creation skipped.")


# Main execution block
if __name__ == "__main__":
    print("LOG: Starting PDF processing pipeline")
    # Check if the data folder exists before processing
    if os.path.exists(DATA_FOLDER):
        process_pdfs_in_folder(DATA_FOLDER)
    else:
        print(f"LOG: Folder '{DATA_FOLDER}' not found. Please ensure it exists and contains PDF files.")
    print("LOG: Pipeline execution completed")