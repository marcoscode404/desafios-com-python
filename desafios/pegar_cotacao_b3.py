import yfinance as yf

tickers = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'BBDC4.SA', 'ABEV3.SA', 'BBAS3.SA', 'WEGE3.SA', 'KLBN4.SA', 'EQTL3', 'CSNA3.SA']
tickers_fiis = ['HGLG11.SA', 'XPML11.SA', 'KNRI11.SA', 'VISC11.SA', 'BCFF11.SA', 'MXRF11.SA', 'BRCR11.SA', 'XPLG11.SA', 'HSML11.SA']

acoes = yf.download(tickers, period='1d')['Close']
fiis = yf.download(tickers_fiis, period='1d')['Close']

for ticker, cotacao in acoes.items(): 
    print(f'Cotação atual de  {ticker}: R$ {cotacao[0]:.2f}')

for fii, cotacao in fiis.items():
    print(f'Cotação atual de {fii}: R$ {cotacao[0]:.2f}')



ticker = yf.Ticker(acoes)