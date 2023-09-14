import customtkinter as tk
import statistics as s

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

list = []
def adicionar():
    list.append(int(caixa1.get()))

def calcular():
    mediana = s.median(list)
    moda = s.mode(list)
    media = s.mean(list)
    texto1.configure(text=f"Mediana: {mediana}\nModa: {moda}\nMédia: {media}")

texto= tk.CTkLabel(janela, text="Edercício")
texto.grid(row=6, column=6, columnspan=2)

caixa1=tk.CTkEntry(janela, placeholder_text="Digite", width=200, height=50)
caixa1.grid(row=7, column=6, columnspan=2)

btn1= tk.CTkButton(janela, text="Adicionar", command= adicionar, width=100, height=50, fg_color='DarkTurquoise')
btn1.grid (row=9, column=6)

btn2= tk.CTkButton(janela, text="Calcular", command= calcular, width=100, height=50, fg_color='DarkTurquoise')
btn2.grid (row=9, column=7)

texto1= tk.CTkLabel(janela, text="")
texto1.grid(row=10, column=6, columnspan=2)


janela.mainloop()