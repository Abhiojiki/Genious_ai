

import json
from xml.parsers.expat import model
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
import time
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
# Create output folder if it doesn't exist
os.makedirs('output', exist_ok=True)

# Configure Gemini with LangChain (get free API key from https://makersuite.google.com/app/apikey)
llm = ChatGoogleGenerativeAI(
    model="gemini-flash-lite-latest",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3
)

# Load articles from output folder
with open("output/articles.json", "r", encoding='utf-8') as f:
    articles = json.load(f)

# Choose your brand name
BRAND_NAME = "OpenAI, Anthropic, Mistral AI, DeepMind, xAI, ElevenLabs, Groq, Synthesia, Deepgram, AssemblyAI, Shield AI, Highspot, ByteDance, DeepL"  # Change this to any brand you want

results = []

for idx, article in enumerate(articles):
    print(f"\n[{idx+1}/15] Analyzing: {article['headline'][:50]}...")
    
    # Create prompt for LLM
    prompt = f"""
Article Title: {article['headline']}

Article Content: {article['content']}

Question: Is any among these "{BRAND_NAME}" mentioned in this article? 
Answer in this exact format:
- Mentioned: YES or NO
- Context: [If YES, provide the exact sentence or context. If NO, write "Not mentioned"]
- Sentiment: [If YES, write POSITIVE, NEGATIVE, or NEUTRAL]
"""
    
    try:
        # Create message object
        message = HumanMessage(content=prompt)
        
        # Query Gemini using LangChain
        response = llm.invoke([message])
        llm_answer = response.content
        
        # Parse response (simple parsing)
        mentioned = "YES" if "YES" in llm_answer.split('\n')[0].upper() else "NO"
        
        # Extract context and sentiment
        lines = llm_answer.split('\n')
        context = "Not mentioned"
        sentiment = "N/A"
        
        for line in lines:
            if "Context:" in line or "context:" in line.lower():
                context = line.split(':', 1)[1].strip()
            if "Sentiment:" in line or "sentiment:" in line.lower():
                sentiment = line.split(':', 1)[1].strip()
        
        result = {
            'url': article['url'],
            'headline': article['headline'],
            'brand_mentioned': mentioned,
            'context': context,
            'sentiment': sentiment,
            'full_llm_response': llm_answer
        }
        
        results.append(result)
        print(f"✓ Brand mentioned: {mentioned}")
        
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        results.append({
            'url': article['url'],
            'headline': article['headline'],
            'brand_mentioned': "ERROR",
            'context': f"Error: {str(e)}",
            'sentiment': "N/A",
            'full_llm_response': ""
        })
    
    time.sleep(2)  # Rate limiting

# Save results to output folder
with open("output/llm_analysis.json", "w", encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"\n✓ Analysis complete! Saved to output/llm_analysis.json")
