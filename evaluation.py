import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 1. ABLATION DATA (Regex vs Hybrid)

data = {
    "Document": [
        "Cabinet Res 12 (2025)", "Cabinet Res 34 (2025)", "Cabinet Res 37 (2017)",
        "Cabinet Res 52 (2017)", "Cabinet Res 55 (2025)", "Cabinet Res 74 (2023)",
        "FDL 28 (2022)", "FDL 37 (2021)", "FDL 37 (2022)",
        "FDL 47 (2022)", "FDL 7 (2017)", "FDL 8 (2017)", "FDL 32 (2021)"
    ],
    "Regex_Only": [11,9,8,7,6,7,12,10,11,14,8,10,15],
    "Hybrid": [15,13,12,10,9,11,18,14,16,21,12,15,22],
}

df = pd.DataFrame(data)
df["Additional"] = df["Hybrid"] - df["Regex_Only"]
df["Improvement_%"] = ((df["Additional"] / df["Regex_Only"]) * 100).round(2)



# 2. SUMMARY METRICS

def generate_summary_metrics(df):
    total_regex = df["Regex_Only"].sum()
    total_hybrid = df["Hybrid"].sum()
    additional = df["Additional"].sum()
    improvement = round((additional / total_regex) * 100, 2)

    print("\n===== Summary Metrics =====")
    print(f"Total Citations (Regex Only):      {total_regex}")
    print(f"Total Citations (Hybrid):          {total_hybrid}")
    print(f"Additional Citations Extracted:    {additional}")
    print(f"Overall Improvement:               {improvement}%")

    return total_regex, total_hybrid, additional, improvement



# 3. SAVE ABLATION TABLE AS CSV + MARKDOWN

def export_tables(df):
    df.to_csv("ablation_results.csv", index=False)
    print("\nCSV saved: ablation_results.csv\n")

    with open("ablation_results.md", "w") as f:
        f.write(df.to_markdown(index=False))

    print("Markdown saved: ablation_results.md\n")



# 4. GRAPHS & VISUALIZATIONS

def generate_graphs(df):

    # Chart: Regex vs Hybrid
    plt.figure(figsize=(12, 6))
    x = np.arange(len(df["Document"]))
    width = 0.35

    plt.bar(x - width/2, df["Regex_Only"], width, label="Regex Only")
    plt.bar(x + width/2, df["Hybrid"], width, label="Hybrid (Regex + NLP)")

    plt.xlabel("Document")
    plt.ylabel("Citations Extracted")
    plt.title("Deterministic vs Hybrid Extraction (Ablation Study)")
    plt.xticks(x, df["Document"], rotation=70)
    plt.legend()
    plt.tight_layout()
    plt.savefig("chart_regex_vs_hybrid.png", dpi=300)
    plt.show()

    print("Saved: chart_regex_vs_hybrid.png")

    #Bar Chart: Additional Citations 
    plt.figure(figsize=(12, 6))
    plt.bar(df["Document"], df["Additional"])
    plt.xlabel("Document")
    plt.ylabel("Additional Citations Found")
    plt.title("Extra Citations Extracted by NLP Enhancement")
    plt.xticks(rotation=70)
    plt.tight_layout()
    plt.savefig("chart_additional_citations.png", dpi=300)
    plt.show()

    print("Saved: chart_additional_citations.png")

    #Line Chart: Improvement Percentage
    plt.figure(figsize=(12,6))
    plt.plot(df["Document"], df["Improvement_%"], marker='o')
    plt.xlabel("Document")
    plt.ylabel("Improvement (%)")
    plt.title("Percentage Improvement per Document")
    plt.xticks(rotation=70)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("chart_percentage_improvement.png", dpi=300)
    plt.show()

    print("Saved: chart_percentage_improvement.png")



# 5. FULL CONSOLIDATED REPORT

def generate_full_report(df):
    print("\n=========== FULL EVALUATION REPORT ===========\n")

    print("1. Overall Metrics")
    print("----------------------------------------------")
    generate_summary_metrics(df)

    print("\n2. Ablation Table")
    print("----------------------------------------------")
    print(df.to_markdown(index=False))

    print("\nFiles generated:")
    print("✓ ablation_results.csv")
    print("✓ ablation_results.md")
    print("✓ chart_regex_vs_hybrid.png")
    print("✓ chart_additional_citations.png")
    print("✓ chart_percentage_improvement.png")



# MAIN EXECUTION

if __name__ == "__main__":
    export_tables(df)
    generate_graphs(df)
    generate_full_report(df)

    print("\nEvaluation complete!")
