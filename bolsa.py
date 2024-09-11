import tkinter as tk
import yfinance as yf
import time

# Função para obter a cotação atual da PETR4
def obter_cotacao():
    ticker = "PETR4.SA"
    dados = yf.Ticker(ticker)
    preco_atual = dados.history(period="1d")['Close'].iloc[0]
    return preco_atual

# Função para atualizar a cotação na interface
def atualizar_cotacao():
    preco_atual = obter_cotacao()
    label_cotacao.config(text=f"Cotação atual da PETR4: R$ {preco_atual:.2f}")
    # Atualiza a cada 5 segundos (5000 milissegundos)
    janela.after(5000, atualizar_cotacao)

# Cria a janela principal
janela = tk.Tk()
janela.title("Cotação PETR4 em Tempo Real")

# Cria um label para exibir a cotação
label_cotacao = tk.Label(janela, text="Carregando cotação...", font=("Arial", 20))
label_cotacao.pack(pady=20)

# Inicia a atualização da cotação
atualizar_cotacao()

# Executa a janela do Tkinter
janela.mainloop()
