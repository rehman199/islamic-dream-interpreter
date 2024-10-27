from langchain.embeddings import HuggingFaceBgeEmbeddings
from qdrant_client import QdrantClient
import openai
import os


class DreamInterpreter():
    def __init__(self):
        self.openai_client = openai.OpenAI(
            base_url=os.getenv('OPENAI_BASE_URL'),
            api_key=os.getenv("OPENAI_API_KEY")
        )
        self.embeddings = HuggingFaceBgeEmbeddings(
            model_name=os.getenv("EMBEDDINGS_MODEL_NAME"))
        self.qdrant_client = QdrantClient(url=os.getenv("QDRANT_URL"), api_key=os.getenv('QDRANT_API_KEY')
                                          )

    def get_context(self, query):
        question_embedding = self.embeddings.embed_query(query)

        docs = self.qdrant_client.search(os.getenv("QDRANT_VECTOR_STORE"),
                                         query_vector=question_embedding)
        context = [doc.payload['page_content'] for doc in docs]
        return " ".join(context)

    def generate_answer(self, query):
        messages = [
            {"role": "system", "content": "You are a chatbot that generates islamic dream interpretations using only the context provided from Ibn Sirin's book of dictionary of dreams. If there are multiple interpretations, you will provide them using the context only."},
            {"role": "user", "content": f"context:\n{
                self.get_context(query)}\nQuestion:{query}"},
        ]
        response = self.openai_client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=messages,
        )
        return response.choices[0].message.content
