import yfinance as yf

tickers = ['PETR4.SA', 'VALE3.SA']
acoes = yf.download(tickers, period='1d')['Close']

for ticker, cotacao in acoes.items(): 
    print(f'Cotação atual de  {ticker}: R$ {cotacao[0]:.2f}')