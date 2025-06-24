# TechStockAIAgent 🚀

An AI-powered investment recommendation system that provides intelligent, data-driven trade recommendations with comprehensive risk management for technology stocks.

## 🎯 Project Overview

TechStockAIAgent is a sophisticated investment analysis tool that leverages OpenAI's GPT models to analyze real-time market data, options chains, and macro-economic indicators to generate precise investment recommendations. The system focuses on providing exactly one optimal trade recommendation per analysis while maintaining strict risk management protocols.

## ✨ Key Features

### 🧠 **AI-Powered Analysis**
- **OpenAI Integration**: Uses GPT-3.5-turbo for intelligent market analysis
- **Pattern Recognition**: Identifies complex relationships between market indicators
- **Contextual Decision Making**: Synthesizes multiple data points for actionable insights

### 📊 **Comprehensive Market Data**
- **Real-time Stock Prices**: Current market data via yfinance
- **Options Chains**: ATM calls/puts with volume and open interest
- **Macro Indicators**: VIX, 10-year Treasury rates
- **Technical Analysis**: Volatility, momentum, and trend indicators

### 🛡️ **Risk Management**
- **Position Sizing**: Automatic calculation based on risk tolerance
- **Loss Limits**: Ensures trades stay within specified risk parameters
- **Exit Strategies**: Defined profit targets and stop-loss levels
- **Risk/Reward Analysis**: Clear ratios for informed decision making

### 🎯 **Investment Recommendations**
- **Single Trade Focus**: One optimal recommendation per analysis
- **Multiple Strategies**: Stock purchases, call options, put options
- **Entry/Exit Points**: Specific price targets and timing
- **Professional Format**: Structured, actionable output

## 🏗️ Project Structure

```
TechStockAIAgent/
├── README.md                              # This file
├── requirements.txt                       # Python dependencies
├── INVESTMENT_SYSTEM_SPECIFICATION.md     # Detailed system specifications
├── WHY_OPENAI.md                         # Explanation of OpenAI integration
├── tech_stock_agent.py                   # LangChain-based version
├── tech_stock_agent_efficient.py         # Optimized direct OpenAI version ⭐
├── tech_stock_agent_fallback.py          # Offline analysis version
└── data/
    └── stock_utils.py                     # Stock data utilities
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key
- Internet connection for real-time data

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd TechStockAIAgent
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API key:**
   - Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
   - Update the API key in `tech_stock_agent_efficient.py`

### Usage

**Run the efficient version (recommended):**
```bash
python tech_stock_agent_efficient.py
```

**Follow the interactive prompts:**
1. Enter stock ticker (e.g., NVDA, AAPL, MSFT)
2. Specify available capital
3. Set maximum loss tolerance (%)
4. Define time horizon

**Example interaction:**
```
🚀 AI-Powered Investment Recommendation System
============================================================

📊 INVESTMENT PARAMETERS
------------------------------
Enter stock ticker: NVDA
Enter available capital ($): $10000
Enter maximum loss tolerance (%): 5
Enter time horizon: 1 month

🔍 Analyzing NVDA for optimal trade recommendation...
⏳ Gathering market data, options chains, and macro indicators...
```

## 📋 Available Versions

### 1. **tech_stock_agent_efficient.py** ⭐ (Recommended)
- **Direct OpenAI API integration**
- **Token-efficient design** (70-80% cost savings)
- **Comprehensive market data analysis**
- **Professional investment recommendations**

### 2. **tech_stock_agent.py**
- **LangChain-based implementation**
- **Agent-driven analysis**
- **Higher token usage but more flexible**

### 3. **tech_stock_agent_fallback.py**
- **Offline analysis capability**
- **No OpenAI API required**
- **Basic fundamental analysis**
- **Good for testing and fallback scenarios**

## 🎯 Sample Output

```
╔══════════════════════════════════════════════════════════════╗
║                   INVESTMENT RECOMMENDATION                  ║
╠══════════════════════════════════════════════════════════════╣
║ Analysis Date: 2025-06-23 10:30 EST
║ Target: NVDA
║ Time Horizon: 1 month
║ Available Capital: $10,000
║ Max Loss Tolerance: 5% ($500)
╠══════════════════════════════════════════════════════════════╣

RECOMMENDATION:
Trade Type: Call Option
Ticker: NVDA
Strike/Expiry: $140.0 (July 18, 2025)
Entry Price Target: $3.50
Position Size: 10 contracts
Total Investment: $3,500

EXIT STRATEGY:
Profit Target: $7.00 (100% gain)
Stop Loss: $1.75 (50% loss)
Time-based Exit: Close 1 week before expiry

RATIONALE:
NVDA shows strong momentum with AI sector tailwinds and upcoming 
earnings catalyst. Options provide leveraged exposure while 
limiting downside to acceptable risk levels.

RISK ANALYSIS:
Maximum Potential Loss: $3,500 (3.5% of capital)
Risk/Reward Ratio: 1:1

╠══════════════════════════════════════════════════════════════╣
║ MARKET DATA SNAPSHOT:
║ Current Price: $138.45
║ Volatility: 42.1%
║ VIX: 18.3
║ 10Y Treasury: 4.25%
╚══════════════════════════════════════════════════════════════╝
```

## 🔧 Configuration

### API Setup
Update your OpenAI API key in the respective files:
```python
client = openai.OpenAI(
    api_key=""
)
```

### Risk Parameters
Adjust default risk settings in the prompt generation:
- Position sizing guidance (60-80% of max loss for options)
- Stop-loss calculations
- Profit target ratios

## 📊 Technical Features

### Data Sources
- **yfinance**: Real-time stock and options data
- **OpenAI API**: AI-powered analysis and recommendations
- **Market indicators**: VIX, Treasury rates, volatility metrics

### Analysis Components
- **Fundamental Analysis**: P/E ratios, market cap, sector analysis
- **Technical Analysis**: Price momentum, volatility, returns
- **Options Analysis**: Strike selection, volume, open interest
- **Macro Analysis**: Interest rates, market sentiment

### Risk Management
- **Position Sizing**: Based on Kelly Criterion and risk tolerance
- **Stop-Loss Calculations**: Automatic based on volatility
- **Diversification**: Single-trade focus with optimal allocation

## 🎓 Why OpenAI?

The system uses OpenAI for several key advantages over traditional analysis:

| Traditional Analysis | OpenAI-Powered Analysis |
|---------------------|------------------------|
| Fixed algorithms | Adaptive reasoning |
| Single-factor focus | Multi-factor synthesis |
| Binary outputs | Nuanced recommendations |
| No explanations | Clear rationale provided |
| Static rules | Dynamic pattern recognition |

**Key Benefits:**
- **70-80% cost reduction** vs. LangChain agents
- **Complex pattern recognition** across multiple data sources
- **Natural language explanations** for investment rationale
- **Adaptive decision making** based on current market conditions

## 📈 Use Cases

### Individual Investors
- Get professional-level analysis for tech stocks
- Receive specific trade recommendations with risk management
- Understand market dynamics through AI explanations

### Risk-Conscious Traders
- Maintain strict loss limits while maximizing profit potential
- Access comprehensive options analysis
- Get multiple exit strategies for different scenarios

### Learning and Education
- Understand how multiple market factors influence trading decisions
- See real-world application of risk management principles
- Learn from AI reasoning and market analysis

## ⚠️ Important Disclaimers

- **Not Financial Advice**: This tool is for educational and research purposes
- **Risk Warning**: All investments carry risk of loss
- **API Costs**: OpenAI API usage incurs costs based on token consumption
- **Data Accuracy**: Market data depends on third-party sources
- **Professional Consultation**: Always consult with qualified financial advisors

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Implement improvements
4. Add tests and documentation
5. Submit a pull request

### Development Areas
- Additional asset classes (bonds, commodities)
- Enhanced technical indicators
- Backtesting capabilities
- Portfolio optimization features
- Web interface development

## 📝 License

This project is for educational and research purposes. Please ensure compliance with relevant financial regulations in your jurisdiction.

## 📞 Support

For questions, issues, or feature requests:
- Check the [INVESTMENT_SYSTEM_SPECIFICATION.md](INVESTMENT_SYSTEM_SPECIFICATION.md) for detailed technical specs
- Review [WHY_OPENAI.md](WHY_OPENAI.md) for AI integration explanations
- Open an issue for bugs or feature requests

---

**Built with 🤖 AI and ❤️ for intelligent investing**
