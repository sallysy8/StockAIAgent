### tech_stock_agent.py

import os
from langchain.agents import Tool, initialize_agent
from langchain_openai import OpenAI  # Updated import
from data.stock_utils import get_tech_stock_data
import openai

def analyze_stock(ticker):
    data = get_tech_stock_data(ticker)
    summary = f"""
    [Stock Analysis Report]
    Stock: {ticker}
    Current Price: ${data['price']}
    P/E Ratio: {data['pe_ratio']}
    Sector: {data['sector']}
    Market Cap: {data['market_cap']}
    Business Summary: {data['summary']}
    """
    return summary

tools = [
    Tool(
        name="Tech Stock Analyzer",
        func=analyze_stock,
        description="Analyze technology stocks, for example AAPL, NVDA, MSFT"
    )
]

# Set up OpenAI API key - using direct API key approach
llm = OpenAI(temperature=0, openai_api_key="")
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

def run_query():
    print("🚀 Welcome to Tech Stock AI Analysis Tool")
    print("=" * 50)
    
    while True:
        query = input("\nEnter stock symbol to analyze (e.g., NVDA, AAPL, MSFT) or 'q' to quit: ").strip()
        
        if query.lower() == 'q':
            print("👋 Thanks for using the tool!")
            break
            
        if not query:
            print("⚠️ Please enter a valid stock symbol")
            continue
            
        print(f"\n📊 Analyzing {query.upper()}...")
        print("-" * 50)
        
        try:
            response = agent.run(f"Please analyze the stock {query}")
            print(response)
        except openai.RateLimitError as e:
            print("❌ OpenAI API quota exceeded. Please check your billing details.")
            print("💡 Suggestions:")
            print("   1. Visit https://platform.openai.com/usage to check usage")
            print("   2. Visit https://platform.openai.com/account/billing to add payment method")
            print("   3. Or use tech_stock_agent_fallback.py for basic analysis")
            break
        except Exception as e:
            print(f"❌ Error occurred: {str(e)}")
            print("💡 Try using tech_stock_agent_fallback.py for basic analysis")

if __name__ == "__main__":
    run_query()
