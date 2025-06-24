### tech_stock_agent_efficient.py
# Investment recommendation system with macro analysis and option data

import openai
import yfinance as yf
from datetime import datetime, timedelta
import requests
from data.stock_utils import get_tech_stock_data

# Set up OpenAI client directly
client = openai.OpenAI(
    api_key=""
)

def get_comprehensive_market_data(ticker):
    """Get comprehensive market data including options and macro indicators"""
    try:
        stock = yf.Ticker(ticker)
        
        # Get stock info and recent price data
        info = stock.info
        hist = stock.history(period="3mo")
        
        if hist.empty:
            return {'error': f"No price data available for {ticker}"}
            
        current_price = hist['Close'].iloc[-1]
        
        # Get options data safely
        options_data = {}
        try:
            options_dates = stock.options
            if options_dates and len(options_dates) > 0:
                # Get options for the nearest expiry
                nearest_expiry = options_dates[0]
                option_chain = stock.option_chain(nearest_expiry)
                calls = option_chain.calls
                puts = option_chain.puts
                
                # Find ATM options safely
                if not calls.empty and not puts.empty:
                    # Find closest strike to current price
                    call_idx = (calls['strike'] - current_price).abs().idxmin()
                    put_idx = (puts['strike'] - current_price).abs().idxmin()
                    
                    atm_calls = calls.loc[call_idx]
                    atm_puts = puts.loc[put_idx]
                    
                    options_data = {
                        'expiry': nearest_expiry,
                        'atm_call': {
                            'strike': atm_calls['strike'],
                            'price': atm_calls['lastPrice'],
                            'volume': atm_calls.get('volume', 0),
                            'openInterest': atm_calls.get('openInterest', 0)
                        },
                        'atm_put': {
                            'strike': atm_puts['strike'],
                            'price': atm_puts['lastPrice'],
                            'volume': atm_puts.get('volume', 0),
                            'openInterest': atm_puts.get('openInterest', 0)
                        }
                    }
        except Exception as opt_error:
            print(f"Options data unavailable: {opt_error}")
            options_data = {}
        
        # Calculate technical indicators safely
        returns = hist['Close'].pct_change().dropna()
        volatility = returns.std() * (252**0.5) if not returns.empty else 0
        
        # 20-day return calculation
        recent_return = 0
        if len(hist) >= 20:
            recent_return = (current_price - hist['Close'].iloc[-20]) / hist['Close'].iloc[-20]
        
        return {
            'ticker': ticker.upper(),
            'current_price': current_price,
            'pe_ratio': info.get('forwardPE'),
            'market_cap': info.get('marketCap'),
            'sector': info.get('sector'),
            'beta': info.get('beta'),
            'volatility': volatility,
            'recent_return': recent_return,
            'options': options_data,
            'earnings_date': info.get('earningsDate'),
            'dividend_yield': info.get('dividendYield')
        }
    except Exception as e:
        return {'error': f"Error fetching data for {ticker}: {str(e)}"}

def get_macro_indicators():
    """Get key macro-economic indicators"""
    try:
        # Get treasury rates and VIX
        treasury_10y = yf.Ticker("^TNX")
        vix = yf.Ticker("^VIX")
        
        # Get recent data with error handling
        tnx_hist = treasury_10y.history(period="5d")
        vix_hist = vix.history(period="5d")
        
        tnx_price = tnx_hist['Close'].iloc[-1] if not tnx_hist.empty else None
        vix_price = vix_hist['Close'].iloc[-1] if not vix_hist.empty else None
        
        return {
            'treasury_10y': tnx_price,
            'vix': vix_price,
            'date': datetime.now().strftime("%Y-%m-%d")
        }
    except Exception as e:
        print(f"Warning: Could not fetch macro data: {e}")
        return {
            'treasury_10y': None,
            'vix': None,
            'date': datetime.now().strftime("%Y-%m-%d"),
            'error': f"Macro data unavailable: {str(e)}"
        }

def generate_trade_recommendation(ticker, time_horizon, max_loss_pct, capital):
    """Generate a single trade recommendation with comprehensive analysis"""
    try:
        # Get all data
        stock_data = get_comprehensive_market_data(ticker)
        macro_data = get_macro_indicators()
        
        if 'error' in stock_data:
            return stock_data['error']
        
        # Calculate position sizing
        max_loss_amount = capital * (max_loss_pct / 100)
          # Create comprehensive prompt for AI analysis
        prompt = f"""As a professional investment analyst, provide ONE specific trade recommendation based on this data:

STOCK DATA (as of {datetime.now().strftime("%Y-%m-%d")}):
- {ticker.upper()}: ${stock_data['current_price']:.2f}
- P/E Ratio: {stock_data.get('pe_ratio', 'N/A')}
- Beta: {stock_data.get('beta', 'N/A')}
- Sector: {stock_data.get('sector', 'N/A')}
- Annualized Volatility: {stock_data['volatility']:.1%}
- 20-day Return: {stock_data['recent_return']:.1%}

OPTIONS DATA:
{f"ATM Call ({stock_data['options']['expiry']}): Strike ${stock_data['options']['atm_call']['strike']}, Price ${stock_data['options']['atm_call']['price']}, Volume {stock_data['options']['atm_call']['volume']}" if stock_data.get('options') and stock_data['options'] else "Options data unavailable"}

MACRO CONDITIONS:
- 10Y Treasury: {f"{macro_data.get('treasury_10y', 'N/A'):.2f}%" if macro_data.get('treasury_10y') else "N/A"}
- VIX: {f"{macro_data.get('vix', 'N/A'):.1f}" if macro_data.get('vix') else "N/A"}

CONSTRAINTS:
- Time Horizon: {time_horizon}
- Available Capital: ${capital:,}
- Maximum Loss Limit: {max_loss_pct}% (${max_loss_amount:,.0f})

POSITION SIZING GUIDANCE:
- For OPTIONS: Maximum position size should utilize significant portion of loss tolerance (aim for 60-80% of max loss for high-conviction trades)
- For STOCKS: Position size based on stop-loss distance from entry price
- ALWAYS ensure maximum possible loss ≤ ${max_loss_amount:,.0f}

Provide EXACTLY ONE trade recommendation in this format:

RECOMMENDATION:
Trade Type: [Stock/Call Option/Put Option]
Ticker: {ticker.upper()}
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

Be specific with numbers and keep response under 300 words."""

        # Get AI recommendation
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert quantitative analyst providing specific, actionable trade recommendations with precise risk management."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=400,
            temperature=0.1  # Low temperature for consistent, factual analysis
        )
        
        ai_recommendation = response.choices[0].message.content
          # Format the complete analysis
        result = f"""
╔══════════════════════════════════════════════════════════════╗
║                   INVESTMENT RECOMMENDATION                  ║
╠══════════════════════════════════════════════════════════════╣
║ Analysis Date: {datetime.now().strftime("%Y-%m-%d %H:%M")} EST
║ Target: {ticker.upper()}
║ Time Horizon: {time_horizon}
║ Available Capital: ${capital:,}
║ Max Loss Tolerance: {max_loss_pct}% (${max_loss_amount:,})
╠══════════════════════════════════════════════════════════════╣

{ai_recommendation}

╠══════════════════════════════════════════════════════════════╣
║ MARKET DATA SNAPSHOT:
║ Current Price: ${stock_data['current_price']:.2f}
║ Volatility: {stock_data['volatility']:.1%}
║ VIX: {f"{macro_data.get('vix', 'N/A'):.1f}" if macro_data.get('vix') else "N/A"}
║ 10Y Treasury: {f"{macro_data.get('treasury_10y', 'N/A'):.2f}%" if macro_data.get('treasury_10y') else "N/A"}
╚══════════════════════════════════════════════════════════════╝

⚠️  DISCLAIMER: This is not financial advice. Past performance does not 
guarantee future results. Always consult with a qualified financial advisor.
        """
        
        return result
        
    except openai.RateLimitError:
        return "❌ OpenAI API quota exceeded. Please check your account balance."
    except Exception as e:
        return f"❌ Analysis failed: {str(e)}"

def run_query():
    print("🚀 AI-Powered Investment Recommendation System")
    print("=" * 60)
    print("Get specific trade recommendations with risk management")
    print("=" * 60)
    
    while True:
        print("\n📊 INVESTMENT PARAMETERS")
        print("-" * 30)
        
        # Get ticker
        ticker = input("Enter stock ticker (e.g., NVDA, AAPL, MSFT) or 'q' to quit: ").strip().upper()
        if ticker.lower() == 'q':
            print("👋 Thanks for using the Investment Recommendation System!")
            break
            
        if not ticker:
            print("⚠️ Please enter a valid stock ticker")
            continue
        
        # Get investment parameters
        try:
            capital = float(input("Enter available capital ($): $").replace('$', '').replace(',', ''))
            if capital <= 0:
                print("⚠️ Capital must be positive")
                continue
                
            max_loss_pct = float(input("Enter maximum loss tolerance (%): ").replace('%', ''))
            if max_loss_pct <= 0 or max_loss_pct > 100:
                print("⚠️ Loss tolerance must be between 0-100%")
                continue
                
            time_horizon = input("Enter time horizon (e.g., '1 week', '1 month', '3 months'): ").strip()
            if not time_horizon:
                time_horizon = "1 month"
                
        except ValueError:
            print("⚠️ Please enter valid numbers")
            continue
        
        print(f"\n🔍 Analyzing {ticker} for optimal trade recommendation...")
        print("⏳ Gathering market data, options chains, and macro indicators...")
        print("-" * 60)
        
        # Generate recommendation
        recommendation = generate_trade_recommendation(ticker, time_horizon, max_loss_pct, capital)
        print(recommendation)
        
        # Ask if user wants another analysis
        another = input("\n🔄 Would you like another recommendation? (y/n): ").strip().lower()
        if another not in ['y', 'yes']:
            print("👋 Thanks for using the Investment Recommendation System!")
            break

if __name__ == "__main__":
    run_query()
