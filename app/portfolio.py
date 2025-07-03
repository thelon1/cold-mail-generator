import pandas as pd 
import chromadb
import uuid

class Portfolio:

    def __init__(self, file_path = "app/resource/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name = 'portfolio')

    def load_portfolio(self):
        if self.collection.count() == 0:
            for _, row in self.df.iterrows():
                self.collection.add(
                                    documents=[row["Techstack"]], 
                                    metadatas=[{"link": row["Links"]}], 
                                    ids=[str(uuid.uuid4())])

    def query_links(self, skills):  # ✅ Method name must be query_links
        results = self.collection.query(query_texts=skills, n_results=2)
        metadata_list = results.get('metadatas', [[]])[0]
        return [meta['link'] for meta in metadata_list if 'link' in meta]
