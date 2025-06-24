### token_usage_test.py
# Test to show token usage difference

import openai
import tiktoken

# Your API key
client = openai.OpenAI(
    api_key=""
)

def count_tokens(text, model="gpt-3.5-turbo"):
    """Count tokens in text"""
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

# Example of what LangChain agent sends (simplified)
langchain_prompt = """Answer the following questions as best you can. You have access to the following tools:

Tech Stock Analyzer: Analyze technology stocks, for example AAPL, NVDA, MSFT

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [Tech Stock Analyzer]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: Please analyze NVDA stock
Thought:"""

# Our efficient prompt
efficient_prompt = """Analyze the following stock data and provide concise investment advice:

Stock: NVDA
Price: $120.50
P/E Ratio: 35.2
Sector: Technology
Market Cap: $2.97T

Please provide:
1. Valuation assessment
2. Key risks
3. Investment recommendation
Keep response concise and professional."""

print("📊 Token Usage Comparison:")
print("=" * 50)
print(f"LangChain Agent Prompt: {count_tokens(langchain_prompt)} tokens")
print(f"Efficient Direct Prompt: {count_tokens(efficient_prompt)} tokens")
print(f"Token Reduction: {count_tokens(langchain_prompt) - count_tokens(efficient_prompt)} tokens saved")
print(f"Efficiency Gain: {((count_tokens(langchain_prompt) - count_tokens(efficient_prompt)) / count_tokens(langchain_prompt) * 100):.1f}% reduction")
