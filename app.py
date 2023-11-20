import customtkinter as ctk
from tkinter import *
from fpdf import FPDF


def click_():
    nome_= nome.get()
    projeto_ = projeto.get()
    hpre_ = hpre.get()
    valorh_ = valorh.get()
    prazo_ = prazo.get()

    total = float(hpre_) * float(valorh_)
    
    if nome_ =="" or projeto_ == "" or hpre_ == "" or valorh_ == "" or prazo_ == "":
        ctk.messagebox.showerror("Erro", "Preencha todos os campos")
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.image('./img/formulario.png', x=0, y=0)

    pdf.text(115, 145, projeto_)
    pdf.text(115, 160, f'{hpre_}h')
    pdf.text(115, 175, f'{valorh_:.2f}')
    pdf.text(115, 190, prazo_)
    pdf.text(120, 205, f'{total:.2f}')
    pdf.text(120, 225, f'Assinatura do(a) {nome_}')

    pdf.output(f'Orçamento do {nome_}.pdf')
    

    

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

#Front-end

frame = ctk.CTkFrame(master=app, width=300, height=300)
frame.place(x=300, y=0)

nome = ctk.CTkEntry(master=frame, placeholder_text="Nome:",width=200, font=('Reboco', 14)).place(x=50, y=20)

projeto = ctk.CTkEntry(master=frame, placeholder_text="Projeto:",width=200, font=('Reboco', 14)).place(x=50, y=50)

hpre = ctk.CTkEntry(master=frame, placeholder_text="Horas Previstas:",width=200, font=('Reboco', 14)).place(x=50, y=80)

valorh = ctk.CTkEntry(master=frame, placeholder_text="Valor da Hora:",width=200, font=('Reboco', 14)).place(x=50, y=110)

prazo = ctk.CTkEntry(master=frame, placeholder_text="Prazo de Entrega:",width=200, font=('Reboco', 14)).place(x=50, y=140)


tot = ctk.CTkLabel(master=frame, text='Valor total: ',font=('Reboco', 18)).place(x=50, y=190) 


btn = ctk.CTkButton(master=frame, text='Gerar Orçamento', command=click_)
btn.place(x=80,y=240)

#Back-end

    






#importar pdf







app.mainloop()