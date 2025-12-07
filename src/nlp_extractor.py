import spacy
from sentence_transformers import SentenceTransformer, util

class NLPExtractor:

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

    def enhance_citations(self, text, deterministic_list):
        doc = self.nlp(text)
        ents = [ent.text for ent in doc.ents if ent.label_ in ["LAW", "ORG"]]

        # Merge deterministic + NLP entities
        merged = list(set(deterministic_list + ents))
        return merged
