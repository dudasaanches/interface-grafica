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


def adicao():
    num1 = int(caixa.get())
    num2 = int(caixa1.get())

    a = num1 + num2
    texto1.configure(text=f"Adição: {a}")

def sub():
    num1 = int(caixa.get())
    num2 = int(caixa1.get())

    s = num1 - num2
    texto1.configure(text=f"Subtração: {s}")

def multi():
    num1 = int(caixa.get())
    num2 = int(caixa1.get())

    m = num1 * num2
    texto1.configure(text=f"Multiplicação: {m}")

def divisao():
    num1 = int(caixa.get())
    num2 = int(caixa1.get())

    d = num1 / num2
    texto1.configure(text=f"Divição: {d}")


texto1 = tk.CTkLabel(janela, text="Calculadora")
texto1.grid(row=5, column=6, columnspan=2)

caixa = tk.CTkEntry(janela, placeholder_text="Digite o número", width=200,height=50)
caixa.grid(row=7, column=6, columnspan=2)

caixa1 = tk.CTkEntry(janela, placeholder_text="Digite o número", width=200,height=50)
caixa1.grid(row=8, column=6,columnspan=2)

btn1 = tk.CTkButton(janela, text="+",command = adicao, width=50,
                   height=30,fg_color="MediumTurquoise",hover_color="Teal")
btn1.grid(row=9, column=6)

btn2 = tk.CTkButton(janela, text="-",command = sub, width=50,
                   height=30,fg_color="MediumTurquoise",hover_color="Teal")
btn2.grid(row=10, column=6)

btn3 = tk.CTkButton(janela, text="x",command = multi, width=50,
                   height=30,fg_color="MediumTurquoise",hover_color="Teal")
btn3.grid(row=9, column=7)

btn4 = tk.CTkButton(janela, text="/",command = divisao, width=50,
                   height=30,fg_color="MediumTurquoise",hover_color="Teal")
btn4.grid(row=10, column=7)
texto1 = tk.CTkLabel(janela, text="")
texto1.grid(row=11, column=6)

janela.mainloop()
