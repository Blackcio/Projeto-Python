import tkinter as tk
from tkinter import Menu
from tkinter import messagebox

# Funções para os itens do menu
def abrir_arquivo():
    messagebox.showinfo("Abrir", "Função de abrir arquivo selecionada.")

def abrir_configuracoes():
    messagebox.showinfo("Configurações", "Função de configurações selecionada.")

def sair_aplicacao():
    janela.quit()

def abrir_ajuda():
    messagebox.showinfo("Ajuda", "Informações de ajuda.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Menu com Tkinter")
janela.geometry("400x300")

# Criar a barra de menus
menu_barra = Menu(janela)

# Criar o menu Arquivo
menu_arquivo = Menu(menu_barra, tearoff=0)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_command(label="Configurações", command=abrir_configuracoes)
menu_arquivo.add_separator()  # Linha separadora
menu_arquivo.add_command(label="Sair", command=sair_aplicacao)

# Criar o menu Ajuda
menu_ajuda = Menu(menu_barra, tearoff=0)
menu_ajuda.add_command(label="Ajuda", command=abrir_ajuda)

# Adicionar os menus à barra de menus
menu_barra.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_barra.add_cascade(label="Ajuda", menu=menu_ajuda)

# Associar a barra de menus à janela
janela.config(menu=menu_barra)

# Iniciar o loop principal da interface
janela.mainloop()
