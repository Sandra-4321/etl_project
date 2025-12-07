import pdfplumber
import os
from src.logger import get_logger
from src.deterministic import DeterministicExtractor
from src.nlp_extractor import NLPExtractor
from src.canonicalizer import Canonicalizer

logger = get_logger()

class PDFIngestor:

    def extract(self, path):
        text = ""
        with pdfplumber.open(path) as pdf:
            for p in pdf.pages:
                page_text = p.extract_text()
                if page_text:
                    text += page_text + "\n"

        # SAVE EXTRACTED TEXT TO data/text/
        os.makedirs("data/text", exist_ok=True)
        filename = os.path.basename(path).replace(".pdf", ".txt")
        text_file_path = f"data/text/{filename}"

        with open(text_file_path, "w", encoding="utf-8") as f:
            f.write(text)

        logger.info(f"Saved extracted text to {text_file_path}")

        return text


class ETLPipeline:

    def __init__(self):
        self.ingestor = PDFIngestor()
        self.det = DeterministicExtractor()
        self.nlp = NLPExtractor()
        self.canon = Canonicalizer()

    def run_on_pdf(self, pdf_path):
        logger.info(f"Extracting text from {pdf_path}")
        text = self.ingestor.extract(pdf_path)

        logger.info("Running deterministic extraction...")
        det_cits = self.det.extract_citations(text)
        terms = self.det.extract_terms(text)

        logger.info("Enhancing via NLP...")
        improved_cits = self.nlp.enhance_citations(text, det_cits)

        logger.info("Canonicalizing results...")
        canonicalized = [self.canon.canon(c) for c in improved_cits]

        return {
            "pdf": pdf_path,
            "citations_raw": improved_cits,
            "citations_canonical": canonicalized,
            "terms": terms
        }
