import tkinter as tk

janela = tk.Tk()

janela.title('Cotação de moedas')

mensagem = tk.Label(text='Sistema de busca de cotação de moedas', fg='white', bg='black', width=35, height=5)
mensagem.pack()

mensagem2 = tk.Label(text='Selecione a moeda desejada')
mensagem2.pack()

moeda = tk.Entry()
moeda.pack()

janela.mainloop()