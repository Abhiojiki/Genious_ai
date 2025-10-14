import subprocess
import sys
import os

# Create output folder before starting
os.makedirs('output', exist_ok=True)

print("="*60)
print("Starting Full Pipeline...")
print("="*60)

steps = [
    ("crawler.py", "Step 1: Collecting URLs from Google Search"),
    ("parser.py", "Step 2: Crawling content from URLs"),
    ("llm_analyzer.py", "Step 3: Analyzing with LLM"),
    ("create_report.py", "Step 4: Creating final report")
]

for script, description in steps:
    print(f"\n{'='*60}")
    print(f"{description}")
    print(f"{'='*60}\n")
    
    result = subprocess.run([sys.executable, script])
    
    if result.returncode != 0:
        print(f"\n✗ Error in {script}. Stopping pipeline.")
        break
    
    print(f"\n✓ {description} completed successfully!")

print("\n" + "="*60)
print("PIPELINE COMPLETE!")
print("Check the 'output' folder for all results")
print("="*60)
