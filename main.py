# Importar Bibliotecas
from customtkinter import *
from tkinter import *

# Tema da Janela
set_appearance_mode('dark')
set_default_color_theme('dark-blue')

# Criar Janela
root = CTk()

# Propriedades da Janela
root.title('Calculadora IMC')
root.geometry('400x300')
root.iconbitmap('muscle.ico')
root.resizable(False, False)

# Canvas
margin_canvas = Canvas(master=root, width=400, height=5, bg='#1A1A1A', highlightthickness=0)
margin_canvas.pack()

# Título
title_txt = CTkLabel(master=root, text='Calculadora IMC', font=('Monserrat', 26, 'bold'))
title_txt.pack()

# Barra de Divisão
division_frame = Frame(master=root, width=400, height=8, bg='#0077ff')
division_frame.place(x=0, y=60)

# Peso
weight_entry = CTkEntry(master=root, font=('Monserrat', 14, 'bold'))
weight_entry.place(x=20, y=120)

weight_txt = CTkLabel(master=root, text='(Kg)', font=('Monserrat', 14, 'bold'))
weight_txt.place(x=165, y=120)

# Altura
height_entry = CTkEntry(master=root, font=('Monserrat', 14, 'bold'))
height_entry.place(x=20, y=170)

height_txt = CTkLabel(master=root, text='(M)', font=('Monserrat', 14, 'bold'))
height_txt.place(x=165, y=170)

# Botão Calcular
def calculate_imc():
    weight = float(weight_entry.get())
    height = float(height_entry.get())

    imc = weight / (height * height)

    result_txt.configure(text=f'IMC: {imc:.2f}')

    if imc < 18.5:
        status_txt.configure(text='Abaixo de Peso', fg='yellow')
    elif 18.5 < imc < 24.9:
        status_txt.configure(text='Normal', fg='green')
    elif 25 < imc < 29.9:
        status_txt.configure(text='Sobrepeso', fg='yellow')
    elif 30 < imc < 34.9:
        status_txt.configure(text='Obesidade Grau I', fg='red')
    elif 35 < imc < 39.9:
        status_txt.configure(text='Obesidade Grau II', fg='red')
    elif imc > 40:
        status_txt.configure(text='Obesidade Grau III', fg='red')

submit_btn = CTkButton(master=root, text='Submeter', font=('Monserrat', 14, 'bold'), command=calculate_imc)
submit_btn.place(x=130, y=230)

# Resultado
result_txt = CTkLabel(master=root, text='IMC: 0.00', font=('Monserrat', 25, 'bold'))
result_txt.place(x=240, y=145)

# Estado
status_txt = Label(master=root, text='', font=('Monserrat', 14, 'bold'), bg='#1A1A1A', width=400, fg='white', anchor='center')
status_txt.pack()

# Ciclo da Janela
root.mainloop()