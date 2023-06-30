import tkinter as tk


def enviar():
    print(var_classe.get())


janela = tk.Tk()

var_classe = tk.StringVar(value='Nada')

botao_classeeconomica = tk.Radiobutton(text='Classe Econômica', variable=var_classe, value='Classe Econômica', command=enviar)
botao_classeexecutiva = tk.Radiobutton(text='Classe Executiva', variable=var_classe, value='Classe Executiva', command=enviar)
botao_primeiraclasse = tk.Radiobutton(text='Primeira Classe', variable=var_classe, value='Primeira Classe', command=enviar)
botao_classeeconomica.grid(row=0, column=0)
botao_classeexecutiva.grid(row=0, column=1)
botao_primeiraclasse.grid(row=0, column=2)


def enviar():
    print(var_classe.get())


# botao_enviar = tk.Button(text='Enviar', command=enviar)
# botao_enviar.grid(row=1, column=1)

janela.mainloop()