import customtkinter as ctk
from tkinter import *

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('dark-blue')

app = ctk.CTk()
app.geometry('450x600')
app.title('Orçamentos')
app.iconbitmap('./img/favicon.ico')
app.resizable(False, False)

img = PhotoImage(file='./img/gbh-tech.gif')
label_img = ctk.CTkLabel(master=app, image=img)
label_img.place(x=5, y=5)


'''
frame = ctk.CTkFrame(master=app, width=445, height=595)
frame.pack()

projeto = ctk.CTkEntry(master=frame, placeholder_text="Projeto",width=350, font=('Reboco', 14)).place(x=50, y=280)

hpre = ctk.CTkEntry(master=frame, placeholder_text="Horas Previstas",width=350, font=('Reboco', 14)).place(x=50, y=320)

valorh = ctk.CTkEntry(master=frame, placeholder_text="Valor da Hora",width=350, font=('Reboco', 14)).place(x=50, y=360)

prazo = ctk.CTkEntry(master=frame, placeholder_text="Projeto",width=350, font=('Reboco', 14)).place(x=50, y=400)
#totvalor = 


'''


app.mainloop()