import tkinter as tk

janela = tk.Tk()

janela.title('Cotação de moedas')

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(text='Sistema de busca de cotação de moedas', fg='white', bg='black', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky='NSEW')

mensagem2 = tk.Label(text='Selecione a moeda desejada')
mensagem2.grid(row=1, column=0)

moeda = tk.Entry()
moeda.grid(row=1, column=1)

dicionario_cotacoes = {
    'Dólar': 5.47,
    'Euro': 6.68,
    'Bitcoin': 20000,
}


def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text='Cotação não encontrada!')
    mensagem_cotacao.grid(row=3, column=0)
    if cotacao_moeda:
        mensagem_cotacao['text'] = f'Cotacao do {moeda_preenchida} é de {cotacao_moeda} '


botao = tk.Button(text='Buscar cotação', command=buscar_cotacao)
botao.grid(row=2, column=1)

janela.mainloop()