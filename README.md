# JJM Chatbot with PDF Processing Pipeline

A comprehensive solution for processing PDF documents and creating a multilingual chatbot using Google's Generative AI. This project includes a PDF processing pipeline and a Streamlit-based chatbot interface.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Understanding the Flow](#understanding-the-flow)
  - [PDF Processing Pipeline](#pdf-processing-pipeline)
  - [Chatbot Application](#chatbot-application)
- [Configuration](#configuration)
- [Usage](#usage)
- [Features](#features)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Overview

This project consists of two main components:
1. A PDF processing pipeline that extracts and vectorizes text from PDF documents
2. A multilingual chatbot interface that answers questions based on the processed documents

## Prerequisites

- Python 3.7+
- Google Cloud API key
- PDF documents for training
- Sufficient storage space for vector database

## Project Structure

```
project/
│   .env                    # Environment variables
│   app.py                 # Streamlit chatbot application
│   processing_pipeline.py # PDF processing script
│   requirements.txt       # Python dependencies
│   suggested_questions.json # Predefined Q&A pairs
│
└───Data/
    └── # Place your PDF files here
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file with your Google API key:
```env
GOOGLE_API_KEY=your_api_key_here
```

4. Place your PDF files in the `Data` folder

## Understanding the Flow

### PDF Processing Pipeline

The processing pipeline follows these steps:

[![](https://mermaid.ink/img/pako:eNp9k01zmzAQhv_KjnK1T-6lHDpDbAdjE09T0vYgcpBhAY1BYiRRl8b57xUCf6UfHDSr3efdXa3QK0llhsQjeSUPacmUgedFIsB-Po2N3b_AdPoJ7mkouOGs4r8Q_KZ5GZh7F5zTSLIMvmFqpILYLngTXwzxJ-FDxLUZY8M6d8SSfmfcQG7lXzUqCEXTnrjFQFyLls71QD8rmaLW8NSi6kb8wcUCGiNTafm3pgJHrGiAAhUzCF9QN1JovGls5aiQzktM92fElrIzMKdiYQ8dAymzM3GENX1WTOiqT81zEIgZZjeCrQRf6AOqI2ws3IFfGVSCGf4DYV4yLkZ845pYX_e1dq6ILrhuKta9bz5y4cfL4eK2KFAbbpkReXTI9pwh5jWvmOqneMNt_xy8bneFYk0JCYmYKFpWIIyXwEWRkIFybQ4miuwf-lO1cRLv5MHFXF3M8GJurvKPuU1X2X8Tcl5V3l3-MZ9oo-QevbvZbDba0wPPTOl9aH5ea5ajZrf7v4ZMSI2qZjyzD-a1z5AQU2KNCfGsmTG178_wZjnWGhl3IiWeUS1OiJJtURIvZ5W2u7bJ7NUsOLPDqEfv22-7cBWt?type=png)](https://mermaid.live/edit#pako:eNp9k01zmzAQhv_KjnK1T-6lHDpDbAdjE09T0vYgcpBhAY1BYiRRl8b57xUCf6UfHDSr3efdXa3QK0llhsQjeSUPacmUgedFIsB-Po2N3b_AdPoJ7mkouOGs4r8Q_KZ5GZh7F5zTSLIMvmFqpILYLngTXwzxJ-FDxLUZY8M6d8SSfmfcQG7lXzUqCEXTnrjFQFyLls71QD8rmaLW8NSi6kb8wcUCGiNTafm3pgJHrGiAAhUzCF9QN1JovGls5aiQzktM92fElrIzMKdiYQ8dAymzM3GENX1WTOiqT81zEIgZZjeCrQRf6AOqI2ws3IFfGVSCGf4DYV4yLkZ845pYX_e1dq6ILrhuKta9bz5y4cfL4eK2KFAbbpkReXTI9pwh5jWvmOqneMNt_xy8bneFYk0JCYmYKFpWIIyXwEWRkIFybQ4miuwf-lO1cRLv5MHFXF3M8GJurvKPuU1X2X8Tcl5V3l3-MZ9oo-QevbvZbDba0wPPTOl9aH5ea5ajZrf7v4ZMSI2qZjyzD-a1z5AQU2KNCfGsmTG178_wZjnWGhl3IiWeUS1OiJJtURIvZ5W2u7bJ7NUsOLPDqEfv22-7cBWt)

### Chatbot Application

The chatbot application follows this flow:

[![](https://mermaid.ink/img/pako:eNqNkjtvwyAUhf_KFV2TKV3qoVLqR_NqVMlVF9yBmOsYBYOFcZuo6X8vxo7iDJXqAR04Hwfuxd8k1xxJQAqpv_KSGQtvUabAfXOaWjf_gOn0EZ7oRjMOsfoURqsKlYV3ZgTbSWw-ev7JgyENS8wPEDHLINGSoxn8fgw76twbEB9FY5szRPTV6BybBl6j5JLXk1s9pJwhppFoaslOEBujb2Mjf3hCE20AWV52QVAIiTdU4qlnGh-tYbkrFY92AJ69taChRKbGxsIbSxrqaicUjq1-XHpgRdNaCgtCWQ1h2arDpY6V99c0NMgsQlztkHOh9hd_7f2N67Y26PZDMl-m6c0RG4-80JR9Irxj7kjw-EC9eH9LY8WHlbhfGYc07W5vWF1CRroaYGi5u0lGesL34SoXV7nsJSr-R-L4UuArFVqNc1dXub7KzSh3yLQniTDv3k4Gd8VDMWms0QcM7maz2aCnX4LbMrivj-M923_uIRNSoamY4O63_-4SMmJLrDAjgZOcmUN38R_Hsdbq9KRyEljT4oQY3e5LEhRMNm7W1tw9aCSYa0LVIz-_EDj-BA?type=png)](https://mermaid.live/edit#pako:eNqNkjtvwyAUhf_KFV2TKV3qoVLqR_NqVMlVF9yBmOsYBYOFcZuo6X8vxo7iDJXqAR04Hwfuxd8k1xxJQAqpv_KSGQtvUabAfXOaWjf_gOn0EZ7oRjMOsfoURqsKlYV3ZgTbSWw-ev7JgyENS8wPEDHLINGSoxn8fgw76twbEB9FY5szRPTV6BybBl6j5JLXk1s9pJwhppFoaslOEBujb2Mjf3hCE20AWV52QVAIiTdU4qlnGh-tYbkrFY92AJ69taChRKbGxsIbSxrqaicUjq1-XHpgRdNaCgtCWQ1h2arDpY6V99c0NMgsQlztkHOh9hd_7f2N67Y26PZDMl-m6c0RG4-80JR9Irxj7kjw-EC9eH9LY8WHlbhfGYc07W5vWF1CRroaYGi5u0lGesL34SoXV7nsJSr-R-L4UuArFVqNc1dXub7KzSh3yLQniTDv3k4Gd8VDMWms0QcM7maz2aCnX4LbMrivj-M923_uIRNSoamY4O63_-4SMmJLrDAjgZOcmUN38R_Hsdbq9KRyEljT4oQY3e5LEhRMNm7W1tw9aCSYa0LVIz-_EDj-BA)

## Configuration

Key configuration options in `processing_pipeline.py`:
```python
EMBEDDING_MODEL = "models/embedding-001"
CHUNK_SIZE = 720
OVERLAP_SIZE = 150
```

Key configuration options in `app.py`:
```python
LLM_MODEL = "gemini-1.5-flash"
CHAIN_TYPE = "stuff"
```

## Usage

1. First, process your PDF documents:
```bash
python processing_pipeline.py
```

2. Run the chatbot application:
```bash
streamlit run app.py
```

3. Access the chatbot interface at `http://localhost:8501`

## Features

- **PDF Processing**
  - Bulk PDF processing
  - Text cleaning and normalization
  - Efficient chunking and vectorization

- **Chatbot Interface**
  - Multilingual support (10 languages)
  - Similar question suggestions
  - Context-aware responses
  - User-friendly interface

- **Advanced Features**
  - Vector similarity search
  - Multiple response strategies
  - Translation capabilities
  - Session state management

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request


© JJM - IIM Bangalore Cell 2024
