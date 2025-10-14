<!-- # Brand Mention Analyzer

## Overview
This project scrapes web data, analyzes it using an LLM, and generates a brand mention report.

## Structure
- `crawler.py`: Web scraping logic
- `llm_analyzer.py`: LLM API integration
- `main.py`: Pipeline orchestration
- `requirements.txt`: Dependencies
- `brand_mention_report.csv`: Output report
- `results/`: Raw data storage

## Usage
1. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
2. Run the pipeline:
   ```powershell
   python main.py
   ```

## Research Summary
- Scrapes web pages for brand mentions
- Uses LLM for advanced analysis
- Outputs results to CSV -->

# Simple Q&A LLMBOT 🚀

A web crawler and LLM-based pipeline that searches for brand mentions across AI startup articles. This project collects URLs from Google Search, extracts article content, and uses LangChain with Google Gemini to analyze brand mentions and sentiment.

## 📋 Project Overview

This pipeline performs:
- **Web Crawling**: Collects 15 URLs from Google Search on "AI startups 2025"
- **Content Extraction**: Scrapes article headlines and main content using BeautifulSoup
- **LLM Analysis**: Uses Google Gemini (via LangChain) to detect brand mentions and sentiment
- **Report Generation**: Creates CSV and Markdown reports with findings

**Brand Analyzed**: OpenAI  
**Total Articles**: 15  
**Brand Mentions Found**: 3/15 (20%)

---

## 🎯 Results Summary

Out of 15 articles about AI startups:
- **3 articles** mentioned OpenAI
- **2 mentions** were positive (Anthropic safety focus)
- **1 mention** was neutral (Sam Altman CEO situation)
- **12 articles** had no brand mention

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **LangChain** - LLM orchestration framework
- **Google Gemini** - LLM for brand mention analysis
- **SerpAPI** - Google Search API
- **BeautifulSoup4** - HTML parsing
- **Pandas** - Data manipulation and CSV generation

---

## 📦 Installation

### 1. Clone the Repository
git clone https://github.com/yourusername/genousai-task.git
cd genousai-task



### 2. Install Dependencies

#### Python version 3.12.8

pip install -r requirements.txt



**requirements.txt**:
google-search-results
beautifulsoup4
requests
pandas
langchain
langchain-google-genai


### 3. Get API Keys

#### a) SerpAPI (Google Search)
- Sign up at: https://serpapi.com/
- Get your API key (100 free searches/month)
- Already included in `crawler.py` (or use environment variable)

#### b) Google Gemini API
- Go to: https://makersuite.google.com/app/apikey
- Click "Create API Key"
- Copy the key
- Add to `llm_analyzer.py`:
google_api_key="YOUR_GEMINI_API_KEY_HERE"



**OR** use `.env` file:
Create .env file
echo "GEMINI_API_KEY=your_key_here" > .env



---

## 🚀 Usage

### Run Full Pipeline
python runall.py



This will execute all 4 steps in sequence:
1. `crawler.py` - Fetch URLs from Google
2. `parser.py` - Extract article content
3. `llm_analyzer.py` - Analyze with Gemini LLM
4. `create_report.py` - Generate CSV and Markdown reports

### Run Individual Steps
Step 1: Get URLs
python crawler.py

Step 2: Parse content
python parser.py

Step 3: LLM analysis
python llm_analyzer.py

Step 4: Create report
python create_report.py



---

---

## 📊 Output Files

### 1. `output/brand_mention_report.csv`
CSV table with columns:
- Source URL
- Article headline
- Brand mentioned (Y/N)
- Extracted context
- Sentiment (positive/negative/neutral)

### 2. `output/REPORT.md`
Markdown formatted report with:
- Total articles analyzed
- Brand mention count
- Detailed results table

### 3. `output/llm_analysis.json`
Raw LLM responses for debugging and analysis

---

## 🔧 Customization

### Change Search Topic
Edit `crawler.py`:
"q": "Your topic here", # Change from "AI startups 2025"



### Change Brand Name
Edit `llm_analyzer.py`:
BRAND_NAME = "YourBrand" # Change from "OpenAI"



### Change Number of URLs
Edit `crawler.py`:
for start in range(0, 50, 10): # Get 50 URLs instead of 15



---

## 🧪 Testing

Basic test to verify setup:
Test SerpAPI
from serpapi import GoogleSearch
search = GoogleSearch({"q": "test", "api_key": "YOUR_KEY"})
print(search.get_dict())

Test Gemini
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key="YOUR_KEY")
print(llm.invoke("Hello"))



---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'serpapi'"
**Solution**: `pip install google-search-results`

### Issue: "403 Forbidden" when crawling
**Solution**: Some websites block scrapers. The code handles this gracefully.

### Issue: "Rate limit exceeded" from Gemini
**Solution**: Add longer sleep time in `llm_analyzer.py`:
time.sleep(5) # Instead of time.sleep(2)



### Issue: Empty content extracted
**Solution**: Some sites use JavaScript. Content extraction works best on static HTML sites.

---

## 📚 Research Summary

For detailed research findings, challenges, and LLM comparisons, see:
👉 **[RESEARCH_SUMMARY.md](RESEARCH_SUMMARY.md)**

Topics covered:
- Open-source LLM APIs explored
- Tradeoffs (accuracy, speed, documentation)
- Challenges faced (crawling, LLM querying, context extraction)
- Scalability suggestions
- Comparison: Gemini vs Cerebras

---

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

---


## 🙏 Acknowledgments

- **SerpAPI** for Google Search API
- **Google** for Gemini LLM
- **LangChain** for LLM orchestration
- **GEOnius AI** for the assignment


---
