import customtkinter as ctk
from tkinter import *


def click_():
    ctk.Label.config('click')

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('dark-blue')

app = ctk.CTk()
app.geometry('600x300')
app.title('Orçamentos')
app.iconbitmap('./img/favicon.ico')
app.resizable(False, False)

img = PhotoImage(file='./img/gbh-tech.png')
label_img = ctk.CTkLabel(master=app, image=img)
label_img.place(x=1, y=0)



frame = ctk.CTkFrame(master=app, width=300, height=300)
frame.pack()
frame.place(x=300, y=0)

projeto = ctk.CTkEntry(master=frame, placeholder_text="Projeto:",width=200, font=('Reboco', 14)).place(x=50, y=40)

hpre = ctk.CTkEntry(master=frame, placeholder_text="Horas Previstas:",width=200, font=('Reboco', 14)).place(x=50, y=80)

valorh = ctk.CTkEntry(master=frame, placeholder_text="Valor da Hora:",width=200, font=('Reboco', 14)).place(x=50, y=120)

prazo = ctk.CTkEntry(master=frame, placeholder_text="Prazo de Entrega:",width=200, font=('Reboco', 14)).place(x=50, y=160)
#totvalor = 


btn = Button(master=frame, text='Gerar Orçamento', command=click_)
btn.place(x=100,y=240)


app.mainloop()