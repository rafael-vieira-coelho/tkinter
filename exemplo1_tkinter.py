import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

contador = 0


def clicado(rotulo):
	global contador
	contador += 1
	rotulo.config(text = f"Total de cliques: {contador}")

if __name__ == '__main__':
	#janela principal
	janela = tk.Tk()
	janela.geometry("300x400")
	janela.title('Minha Primeira Janela')
	
	#criando um quadro (container)
	quadro = ttk.Frame(janela)
	quadro.pack(padx=10, pady=10) #espaçamento horizontal e vertical
	
	#criando um texto estático (label)
	rotulo = ttk.Label(quadro, text="Quantos cliques?")
	rotulo.pack()
	
	#criando um botão para contar os cliques
	botao = ttk.Button(quadro, text='Clique aqui!', 
	command=lambda: clicado(rotulo))
	botao.pack(pady=10)
	
	janela.mainloop()
