import customtkinter as tk
import random

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

num = random.randint(1,100)
def verificar():
    num1 = int(caixa1.get())

    if num1 > num:
        texto1.configure(text="O número é menor")
    elif num > num1:
        texto1.configure(text="O número é maior")
    elif num1 == num:
        texto1.configure(text="Acertou")
        janela.destroy()

texto= tk.CTkLabel(janela, text="Adivinhe o número")
texto.grid(row=6, column=6)

caixa1=tk.CTkEntry(janela, placeholder_text="Digite", width=200, height=50)
caixa1.grid(row=7, column=6)

btn1= tk.CTkButton(janela, text="Clique Aqui", command= verificar, width=100, height=50, fg_color='DarkTurquoise')
btn1.grid (row=9, column=6)

texto1= tk.CTkLabel(janela, text="")
texto1.grid(row=10, column=6)


janela.mainloop()