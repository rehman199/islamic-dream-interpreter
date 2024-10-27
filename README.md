# Islamic Dream Interpretation App

This application offers dream interpretations based on Islamic teachings, drawing on *Dictionary of Dreams* by Imam Ibn Sirin, one of the earliest and most respected scholars in Islamic dream interpretation. Built using **Streamlit**, it provides a user-friendly interface to input dreams and receive contextually relevant interpretations, along with related guidance from authentic hadith.

## Features

- **Authentic Dream Interpretation**: Provides interpretations based on the Islamic perspective from Imam Ibn Sirin’s *Dictionary of Dreams*.
- **Interactive Chat Interface**: Simple and intuitive interface powered by Streamlit’s `st.chat_message`, allowing users to have a natural conversation.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/dream-interpretation-app.git
    cd dream-interpretation-app
    ```

2. **Install dependencies**:
    Make sure you have Python 3.8+ installed. You can install required libraries by running:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    - Create a `.env` file in the project root.
    - Add your API keys, database configurations, and any other required environment variables.

## Usage

1. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```
2. **Open the app**:
    After running, open your browser and navigate to `http://localhost:8501`.

3. **Input Dream Description**:
    Enter a brief description of your dream and submit. The app will fetch context-based interpretations and display them in the chat format.

## Configuration

- **Vector Database**: Set up a vector database (Qdrant) for efficient retrieval of context from Imam Ibn Sirin’s *Dictionary of Dreams*.
  
   Update the vector database configurations in `.env` if applicable.

## Dependencies

- **Python 3.8+**
- **Streamlit** for frontend interface
- **Qdrant** for vector-based retrieval (for the RAG model)

Install all dependencies using the `requirements.txt` file.

## Acknowledgements

- [Imam Ibn Sirin’s Dictionary of Dreams](https://archive.org/details/IbnSirinDictionaryOfDreams/page/n3/mode/2up) for the foundational content on Islamic dream interpretation (used in the RAG model as vector embeddings).
- The Streamlit team for providing an intuitive, interactive platform for Python applications.
- Various open-source contributors for resources and tools in the NLP and deep learning communities.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
