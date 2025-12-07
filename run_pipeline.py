import os
import json
from src.pipeline import ETLPipeline
from src.storage import S3Storage

pipeline = ETLPipeline()
results = []

RAW_DIR = "data/raw/"

for file in os.listdir(RAW_DIR):
    if file.endswith(".pdf"):
        pdf_path = os.path.join(RAW_DIR, file)
        print(f"Processing: {pdf_path}")
        out = pipeline.run_on_pdf(pdf_path)
        results.append(out)

# Save final JSON
os.makedirs("output", exist_ok=True)
json_path = "output/results.json"

with open(json_path, "w") as f:
    json.dump(results, f, indent=2)

print("Saved output to output/results.json")

# Upload to AWS S3
storage = S3Storage("sandra-etl-bucket")
storage.upload(json_path, "etl/results.json")
