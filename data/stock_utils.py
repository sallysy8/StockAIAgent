import yfinance as yf

def get_tech_stock_data(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        'symbol': ticker,
        'price': info.get('currentPrice'),
        'pe_ratio': info.get('trailingPE'),
        'sector': info.get('sector'),
        'market_cap': info.get('marketCap'),
        'summary': info.get('longBusinessSummary')
    }
