import yfinance as yf

# Define o ticker da Petrobras (PETR4)
ticker = "PETR4.SA"

# Obtém os dados da ação
dados = yf.Ticker(ticker)

# Pega a última cotação (preço atual), acessando via iloc para evitar o FutureWarning
preco_atual = dados.history(period="1d")['Close'].iloc[0]

# Exibe o preço
print(f"A cotação atual da PETR4 é: R$ {preco_atual:.2f}")
