from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

#cores
color1 = "#3b3b3b" #Preta / Escura
color2 = "#333333" #Preta / Clara
color3 = "#FFFFFF" #Branco
color4 = "#fcc058" #Laranja

window = Tk()
window.title("Calculadora de Idade")
window.geometry("310x410")
window.configure(bg=color1)

window.minsize(310, 410)
#window.maxsize(310, 410)

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

style = ttk.Style(window)
style.theme_use("clam")

#Frames
"""
O Frame é como uma "caixa" onde colocamos os elementos.
A tela é dividida em 2 áreas:

    top_frame: parte de cima, fundo cinza escuro.

    bottom_frame: parte de baixo, fundo cinza ainda mais escuro.
"""
top_frame = Frame(window, width=310, 
                  height=140, pady=0, padx=0,
                  relief="flat", bg=color2)
top_frame.grid(row=0, column=0, sticky="nsew")

bottom_frame = Frame(window, width=310, 
                  height=140, pady=0, padx=0,
                  relief="flat", bg=color1)

bottom_frame.grid(row=1, column=0, sticky="nsew")
#Labels - Etiquetas com o texto

#Labels Top Frame
app_calculator = Label(top_frame, text="Calculadora de", 
                       width=25, height=1, padx=3, relief="flat",
                       anchor="center", font=("Ivy 15 bold"),
                       bg=color2, fg=color3)
#app_calculator.place(x=0, y=30)
app_calculator.grid(row=0, column=0, sticky="nsew", pady=(5, 5), padx=10)

app_of_rage = Label(top_frame, text="Idade", 
                       width=11, height=1, padx=0, relief="flat",
                       anchor="center", font=("Arial 35 bold"),
                       bg=color2, fg=color4)
#bg = background - fundo
#fg = foreground - letra
#app_of_rage.place(x=0, y=70)
app_of_rage.grid(row=1, column=0, sticky="nsew", pady=(0, 5), padx=10)

top_frame.grid_rowconfigure(0, weight=1)
top_frame.grid_rowconfigure(1, weight=1)
top_frame.grid_columnconfigure(0, weight=1)


#Labels Bottom Frame
"""l_initial_date = Label(bottom_frame, text="Data Inicial", height=1,
                       padx=0, pady=0, relief="flat", anchor=NW, font=("Ivy 9"),
                       bg=color1, fg=color3)"""
                       
l_initial_date = Label(bottom_frame, text="Data Atual",
                       relief="flat", anchor="w", font=("Ivy 9"),
                       bg=color1, fg=color3)
#l_initial_date.place(x=50, y=30)
l_initial_date.grid(row=0, column=0, columnspan=2, sticky="w", padx=(25, 5), pady=20)

cal_initial_date = DateEntry(bottom_frame, width=12, background="darkblue", 
                             foreground="white", borderwidth=2, date_pattern="dd/mm/y", 
                             year=2025)

#cal_initial_date.place(x=170, y=30)
cal_initial_date.grid(row=0, column=2,sticky="e", padx=(5, 25), pady=20)

l_birth_date = Label(bottom_frame, text="Data de Nascimento",
                       relief="flat", anchor="w", font=("Ivy 9"),
                       bg=color1, fg=color3)

l_birth_date.grid(row=1, column=0, columnspan=2, sticky="w", padx=(25, 5), pady=20)

cal_birth_date = DateEntry(bottom_frame, width=12, background="darkblue", 
                             foreground="white", borderwidth=2, date_pattern="dd/mm/y", 
                             year=1998)

cal_birth_date.grid(row=1, column=2,sticky="e", padx=(5, 25), pady=20)

#Ano
app_years = Label(bottom_frame, text="0",
                       relief="flat", anchor="center", font=("Ivy 20 bold"),
                       bg=color1, fg=color3)


app_years.grid(row=2, column=0, sticky="w", padx=(25, 5), pady=20)

app_labels_years = Label(bottom_frame, text="Anos",
                       relief="flat", anchor="center", font=("Ivy 15 bold"),
                       bg=color1, fg=color3)

app_labels_years.grid(row=3, column=0, sticky="w", padx=(25, 5), pady=20)

#Meses
app_months = Label(bottom_frame, text="0",
                       relief="flat", anchor="center", font=("Ivy 20 bold"),
                       bg=color1, fg=color3)

app_months.grid(row=2, column=1, sticky="nsew", padx=(20, 20), pady=20)

app_labels_months = Label(bottom_frame, text="Meses",
                       relief="flat", anchor="center", font=("Ivy 15 bold"),
                       bg=color1, fg=color3)

app_labels_months.grid(row=3, column=1, sticky="nsew", padx=(20, 20), pady=20)

#Dias
app_days = Label(bottom_frame, text="0",
                       relief="flat", anchor="center", font=("Ivy 20 bold"),
                       bg=color1, fg=color3)

app_days.grid(row=2, column=2, sticky="e", padx=(5, 20), pady=20)

app_labels_days = Label(bottom_frame, text="Dias",
                       relief="flat", anchor="center", font=("Ivy 15 bold"),
                       bg=color1, fg=color3)

app_labels_days.grid(row=3, column=2, sticky="e", padx=(5, 25), pady=20)


#Calculo de Dias etc
def calculate_age():
    '''
    Forma antiga e ruim:
    
    initial_date_str = cal_initial_date.get_date()
    birth_date_str = cal_birth_date.get_date()
    
    month_1, day_1, year_1 = [int(f) for f in initial_date_str.split('/')]
    initial_date = date(year_1, month_1, day_1)
    
    month_2, day_2, year_2 = [int(f) for f in birth_date_str.split('/')]
    birth_date = date(year_2, month_2, day_2)
    
    years = relativedelta(initial_date, birth_date).years
    months = relativedelta(initial_date, birth_date).months
    days = relativedelta(initial_date, birth_date).days
    
    app_years["text"] = years
    app_months["text"] = months
    #app_days["text"] = days
    
    '''
    initial_date = cal_initial_date.get_date()
    birth_date = cal_birth_date.get_date()
    
    diff = relativedelta(initial_date, birth_date)
    
    years = diff.years
    months = diff.months
    days = diff.days
    
    app_years["text"] = years
    app_months["text"] = months
    # Você pode criar um `app_days` se quiser exibir os dias também
    app_days["text"] = days


#Botão
b_calculate_age = Button(bottom_frame, text="Calcular Idade", width=20, 
                         height=1, bg=color1, fg=color3, font=("Ivy 10 bold"), anchor="center",
                         relief=RAISED, overrelief=RIDGE, command=calculate_age)

b_calculate_age.grid(row=4, column=0, columnspan=3, sticky="nsew", padx=(30, 30), pady=20)


bottom_frame.grid_rowconfigure(0, weight=1)
bottom_frame.grid_rowconfigure(1, weight=1)
bottom_frame.grid_rowconfigure(2, weight=1)
bottom_frame.grid_rowconfigure(3, weight=1)
bottom_frame.grid_rowconfigure(4, weight=1)
bottom_frame.grid_columnconfigure(0, weight=1)
bottom_frame.grid_columnconfigure(1, weight=1)
bottom_frame.grid_columnconfigure(2, weight=1)

window.mainloop()