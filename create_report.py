import json
import pandas as pd
import os

# Create output folder if it doesn't exist
os.makedirs('output', exist_ok=True)

# Load LLM analysis results from output folder
with open("output/llm_analysis.json", "r", encoding='utf-8') as f:
    results = json.load(f)
    
df = pd.DataFrame(results)

# Select columns for report
report_df = df[['url', 'headline', 'brand_mentioned', 'context', 'sentiment']]

# Save as CSV
report_df.to_csv("brand_mention_report.csv", index=False)
print("✓ CSV report saved: brand_mention_report.csv")

# Create Markdown table
markdown_table = "# Brand Mention Analysis Report\n\n"
markdown_table += f"**Total Articles Analyzed:** {len(results)}\n\n"

# Count mentions
mentions = sum(1 for r in results if r['brand_mentioned'] == 'YES')
markdown_table += f"**Brand Mentions Found:** {mentions}/{len(results)}\n\n"

markdown_table += "## Results Table\n\n"
markdown_table += "| URL | Headline | Mentioned | Context | Sentiment |\n"
markdown_table += "|-----|----------|-----------|---------|------------|\n"

for _, row in report_df.iterrows():
    url_short = row['url'][:50] + "..." if len(row['url']) > 50 else row['url']
    headline_short = row['headline'][:40] + "..." if len(row['headline']) > 40 else row['headline']
    context_short = row['context'][:60] + "..." if len(row['context']) > 60 else row['context']
    
    markdown_table += f"| {url_short} | {headline_short} | {row['brand_mentioned']} | {context_short} | {row['sentiment']} |\n"

# Save markdown report
with open("REPORT.md", "w", encoding='utf-8') as f:
    f.write(markdown_table)

print("✓ Markdown report saved: REPORT.md")
print("\n" + "="*50)
print("ALL DONE! Check these files:")
print("1. brand_mention_report.csv")
print("2. REPORT.md")
print("="*50)
