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

[![](https://mermaid.ink/img/pako:eNp1kstuwjAQRX9l5HX5ARaVSh68AkJKxcZhMcQDsUhs5DgUVPrvdZxQwqJZWNdzj689o3yzXAtiY3Yo9VdeoLHwGWYK3PfBU-v2OxiN3mHCE40CInWRRquKlIUtGon7kupdx088GPCgoPwEIVqEWJeCTO93a9BS986A6CprW98h5Bujc6pr2ITxI68j17pPuUPEQ1mfS7xBZIx-jQ395TGPtQHCvGiD4CBLeqFiT015dLUGc9cqXW0PTL0140FJqIbGzBtzHuhqLxUNrW6de2DB03MpLUhlNQRFo06PPhbeX_LAEFqCqNqTEFIdH_7S-4mbtjbkzkP8MU_TlysSj6x4iheCLeWOBI_31Mr7ax4p0VeirjIMqZv90eC5gIy1PUA_cveSjHWEn8NTzp5y3klS4p_E4aPAdyq1GuYunnL5lMlfLntjFZkKpXA_43dbzpgtqKKMjZ0UaE5t3I_jsLE6vamcja1p6I0Z3RwLNj5gWbtdcxZuzKFE97Sqr_78AlRj2yw?type=png)](https://mermaid.live/edit#pako:eNp1kstuwjAQRX9l5HX5ARaVSh68AkJKxcZhMcQDsUhs5DgUVPrvdZxQwqJZWNdzj689o3yzXAtiY3Yo9VdeoLHwGWYK3PfBU-v2OxiN3mHCE40CInWRRquKlIUtGon7kupdx088GPCgoPwEIVqEWJeCTO93a9BS986A6CprW98h5Bujc6pr2ITxI68j17pPuUPEQ1mfS7xBZIx-jQ395TGPtQHCvGiD4CBLeqFiT015dLUGc9cqXW0PTL0140FJqIbGzBtzHuhqLxUNrW6de2DB03MpLUhlNQRFo06PPhbeX_LAEFqCqNqTEFIdH_7S-4mbtjbkzkP8MU_TlysSj6x4iheCLeWOBI_31Mr7ax4p0VeirjIMqZv90eC5gIy1PUA_cveSjHWEn8NTzp5y3klS4p_E4aPAdyq1GuYunnL5lMlfLntjFZkKpXA_43dbzpgtqKKMjZ0UaE5t3I_jsLE6vamcja1p6I0Z3RwLNj5gWbtdcxZuzKFE97Sqr_78AlRj2yw)

### Chatbot Application

The chatbot application follows this flow:

[![](https://mermaid.ink/img/pako:eNp1ks9SpDAQxl-lK2d9gTlYhYMyzOCULq4egoeW9EBKSKgkrDXr-O6GwPxzVw6pTn-_7v5o-GClFsRmbNPo97JG4-AxLhT4J-K58_cXuLy8gmueKukkNvIvQdR1LyNzHcQ5zzQKeKLSaQO5P-hMj0f9QUWQSesmbTzngbjhzygdbHz5b0sGUtX1ey4eidOim5C65fdGl2QtPPRkthN-G7SE54SmrP9nKgnEgiekyKAj-EW208rSmbFFoFI-r6l8OyB-lN-B2w9LB2iXaC0OxA6W_NGgss3QWm5AEQkSZwVrDZGy72R2sPLwFqLGkVHo5B-CeY1STfgqmFie-lqGVMZjabsGt9_NZ0G-O75c3lcVWSc9MyF3AVkfOuSylQ2aYYtn3Prfxdv-tTLY1VCwDFXVY0UwfQSpqoKNVLA5hqTED_X7adMmvpUnx3BxDNNjuDrpzy5YS6ZFKfyP_DEIBXM1tVSwmQ8Fmreh96fnsHc636qSzZzp6YIZ3Vc1m22wsf7Wd8KvLJboTbZT9vMLSYTzKQ?type=png)](https://mermaid.live/edit#pako:eNp1ks9SpDAQxl-lK2d9gTlYhYMyzOCULq4egoeW9EBKSKgkrDXr-O6GwPxzVw6pTn-_7v5o-GClFsRmbNPo97JG4-AxLhT4J-K58_cXuLy8gmueKukkNvIvQdR1LyNzHcQ5zzQKeKLSaQO5P-hMj0f9QUWQSesmbTzngbjhzygdbHz5b0sGUtX1ey4eidOim5C65fdGl2QtPPRkthN-G7SE54SmrP9nKgnEgiekyKAj-EW208rSmbFFoFI-r6l8OyB-lN-B2w9LB2iXaC0OxA6W_NGgss3QWm5AEQkSZwVrDZGy72R2sPLwFqLGkVHo5B-CeY1STfgqmFie-lqGVMZjabsGt9_NZ0G-O75c3lcVWSc9MyF3AVkfOuSylQ2aYYtn3Prfxdv-tTLY1VCwDFXVY0UwfQSpqoKNVLA5hqTED_X7adMmvpUnx3BxDNNjuDrpzy5YS6ZFKfyP_DEIBXM1tVSwmQ8Fmreh96fnsHc636qSzZzp6YIZ3Vc1m22wsf7Wd8KvLJboTbZT9vMLSYTzKQ)

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
