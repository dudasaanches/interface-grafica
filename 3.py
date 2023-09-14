import customtkinter as tk

tk.set_appearance_mode("dark")

janela = tk.CTk()
janela.title("Janela 1")
janela.geometry("400x350")
janela.configure(fg_color="grey31")
janela.resizable(width=False,height=False)
colunas = list(range(13))
linhas = list(range(13))
janela.grid_columnconfigure(colunas, weight=1)
janela.grid_rowconfigure(linhas, weight=1)


def verificar():
    n1 = int(caixa1.get())
    n2 = int(caixa2.get())

    prest = n1/n2
    if prest > 500 :
        texto1.configure(text="O usuário não pode pagar")
    else:
        texto1.configure(text="O usuário consegue pagar")


texto= tk.CTkLabel(janela, text="Digite o valor da compra")
texto.grid(row=6, column=6)

caixa1=tk.CTkEntry(janela, placeholder_text="Digite o valor", width=250, height=50)
caixa1.grid(row=7, column=6)

caixa2=tk.CTkEntry(janela, placeholder_text="Digite a quantidade de prestações", width=250, height=50)
caixa2.grid(row=8, column=6)

btn1= tk.CTkButton(janela, text="Clique Aqui", command= verificar, width=100, height=50, fg_color='DarkTurquoise')
btn1.grid (row=9, column=6)

texto1= tk.CTkLabel(janela, text="")
texto1.grid(row=10, column=6)


janela.mainloop()