import re

class DeterministicExtractor:

    CITE_REGEX = r'((?:Federal|Cabinet)[^\.]+?\d{4})'
    TERM_REGEX = r'([A-Z][A-Za-z ]+)\s*:\s*(.+)'

    def extract_citations(self, text: str):
        matches = re.findall(self.CITE_REGEX, text)
        return [m[0] if isinstance(m, tuple) else m for m in matches]

    def extract_terms(self, text: str):
        matches = re.findall(self.TERM_REGEX, text)
        return [{"term": t.strip(), "definition": d.strip()} for t, d in matches]
