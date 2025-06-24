# Investment Recommendation System Specification

## Overview
This document outlines the requirements and specifications for an AI-powered investment recommendation system that provides precise, data-driven trade recommendations with comprehensive risk management.

## Core Objective
**Recommend exactly one trade (equity or option) that, in your judgment, offers the highest expected profit over [TIME HORIZON] while keeping maximum potential loss ≤ [MAX LOSS % or $] of my capital.**

## Key Principles
- **Single Recommendation**: The system must provide exactly ONE trade recommendation per analysis
- **Risk-First Approach**: Maximum loss must never exceed the specified tolerance
- **Evidence-Based**: All recommendations must be backed by comprehensive market data
- **Independent Analysis**: Avoid relying solely on third-party forecasts

## Research Scope

### 1. Market Data Requirements
- **Price Data**: Real-time stock prices and historical performance
- **Options Chains**: Current option prices, strikes, expiries, volume, and open interest
- **Date Stamp**: All data must be current as of [TODAY]

### 2. Macro-Economic Analysis
- **Interest Rates**: Current 10-year Treasury yields
- **Market Volatility**: VIX index levels
- **Inflation Indicators**: Current inflation trends and expectations
- **Tariff Policies**: Impact of current trade policies on target sectors
- **Federal Reserve Outlook**: Current monetary policy stance and future expectations

### 3. Company-Specific Research
- **Fundamental Analysis**: 
  - P/E ratios and valuation metrics
  - Revenue growth and profitability trends
  - Earnings estimates and guidance
  - Debt levels and financial health
- **Recent News**: Material developments affecting stock price
- **Sector Analysis**: Industry trends and competitive positioning

### 4. Market Sentiment Analysis
- **Options Flow**: Analysis of option volume and open interest patterns
- **Institutional Activity**: Large block trades and insider activity
- **Technical Indicators**: Price momentum, volatility, and trend analysis

## Deliverables

### 1. Chosen Instrument
- **Equity Trade**: Stock ticker and number of shares
- **Options Trade**: 
  - Ticker symbol
  - Strike price
  - Expiration date
  - Contract type (Call/Put)
  - Number of contracts

### 2. Trading Strategy
- **Entry Price Target**: Specific price level for trade execution
- **Position Size**: Exact number of shares or contracts
- **Total Investment**: Dollar amount to be invested

### 3. Exit Strategy
- **Profit Target**: Specific price level or percentage gain to close position
- **Stop Loss**: Maximum loss threshold with specific exit conditions
- **Time-Based Exit**: Conditions for closing position based on time decay or market events
- **Alternative Scenarios**: Backup exit strategies for different market conditions

### 4. Risk Analysis
- **Maximum Loss Calculation**: 
  - Dollar amount of maximum potential loss
  - Percentage of total capital at risk
  - Verification that loss stays within specified limits
- **Risk/Reward Ratio**: Expected profit vs. maximum loss ratio
- **Probability Assessment**: Estimated likelihood of success

### 5. Rationale
- **Data Synthesis**: Concise explanation combining all research elements
- **Market Opportunity**: Why this specific trade offers the highest expected profit
- **Risk Justification**: How the risk level aligns with the profit potential
- **Timing Rationale**: Why now is the optimal time for this trade

## Analysis Framework

### Input Parameters
- **Available Capital**: Total investment funds available
- **Risk Tolerance**: Maximum acceptable loss (% or $)
- **Time Horizon**: Investment timeframe (days/weeks/months)
- **Target Security**: Specific stock or sector to analyze

### Data Integration
1. **Real-Time Market Data**: Current prices, volume, volatility
2. **Options Market Data**: Strikes, premiums, Greeks, open interest
3. **Fundamental Metrics**: Financial ratios, earnings, growth rates
4. **Macro Indicators**: Rates, inflation, policy impacts
5. **Sentiment Indicators**: Options flow, institutional activity

### Decision Logic
1. **Opportunity Identification**: Screen for highest probability setups
2. **Risk Assessment**: Calculate maximum loss scenarios
3. **Position Sizing**: Determine optimal investment amount
4. **Strategy Selection**: Choose between equity vs. options approach
5. **Exit Planning**: Define specific profit/loss targets

## Output Format

### Structured Recommendation
```
RECOMMENDATION:
Trade Type: [Stock/Call Option/Put Option]
Ticker: [Symbol]
Strike/Expiry: [If option]
Entry Price Target: $[X.XX]
Position Size: [Shares/Contracts]
Total Investment: $[Amount]

EXIT STRATEGY:
Profit Target: $[Price] ([X]% gain)
Stop Loss: $[Price] ([X]% loss)
Time-based Exit: [Conditions]

RATIONALE:
[2-3 sentences explaining why this trade offers highest expected profit within risk limits]

RISK ANALYSIS:
Maximum Potential Loss: $[Amount] ([X]% of capital)
Risk/Reward Ratio: [X:1]
```

## Quality Standards

### Data Requirements
- **Timeliness**: All market data must be current
- **Accuracy**: Price and volume data must be verified
- **Completeness**: All required data points must be available

### Analysis Standards
- **Independence**: Recommendations based on proprietary analysis
- **Objectivity**: Remove bias toward specific outcomes
- **Transparency**: Clear explanation of decision factors

### Risk Management
- **Conservative Approach**: Err on the side of capital preservation
- **Stress Testing**: Consider adverse market scenarios
- **Position Limits**: Never exceed specified risk tolerance

## Implementation Notes

### Technology Stack
- **Data Sources**: Real-time market data feeds
- **Analysis Engine**: AI-powered recommendation system
- **Risk Engine**: Automated position sizing and risk calculation
- **User Interface**: Interactive parameter input system

### Workflow
1. **Parameter Collection**: Gather user inputs (capital, risk tolerance, time horizon)
2. **Data Aggregation**: Collect all required market and fundamental data
3. **Analysis Processing**: Apply AI algorithms to identify optimal trade
4. **Risk Validation**: Verify recommendation meets risk constraints
5. **Output Generation**: Format and present structured recommendation

### Compliance
- **Disclaimers**: Include appropriate risk warnings
- **Regulatory**: Ensure recommendations comply with financial regulations
- **Documentation**: Maintain audit trail of analysis process

## Success Metrics

### Performance Indicators
- **Accuracy**: Percentage of recommendations that meet profit targets
- **Risk Control**: Percentage of trades that stay within loss limits
- **Profitability**: Average return per recommendation
- **Efficiency**: Time from analysis to recommendation delivery

### Continuous Improvement
- **Feedback Loop**: Track actual vs. predicted outcomes
- **Model Updates**: Refine algorithms based on performance
- **Data Enhancement**: Improve data sources and analysis depth

---

*This specification serves as the foundation for building a comprehensive, AI-powered investment recommendation system that prioritizes risk management while seeking optimal profit opportunities.*
