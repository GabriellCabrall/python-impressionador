import tkinter as tk

janela = tk.Tk()

janela.title('Cotação de moedas')

mensagem = tk.Label(text='Sistema de busca de cotação de moedas', fg='white', bg='blackcd', width=50, height=10)
mensagem.pack()

mensagem2 = tk.Label(text='Selecione a moeda desejada', height=15, width=70)
mensagem2.pack()

janela.mainloop()