import re

class Canonicalizer:

    def canon(self, text):
        t = text.lower()

        num = re.findall(r'no\.*\s*\(?(\d+)\)?', t)
        year = re.findall(r'(\d{4})', t)

        if num and year:
            return f"doc_{num[0]}_{year[-1]}"

        return t.replace(" ", "_")
