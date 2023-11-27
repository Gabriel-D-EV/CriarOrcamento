import customtkinter as ctk
from tkinter import *
from fpdf import FPDF
from tkinter import messagebox
from view import *

    

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

nome_entry = ctk.CTkEntry(master=frame, placeholder_text="Nome:",width=200, font=('Reboco', 14))
nome_entry.place(x=50, y=20)

projeto_entry = ctk.CTkEntry(master=frame, placeholder_text="Projeto:",width=200, font=('Reboco', 14))
projeto_entry.place(x=50, y=50)

hpre_entry = ctk.CTkEntry(master=frame, placeholder_text="Horas Previstas:",width=200, font=('Reboco', 14))
hpre_entry.place(x=50, y=80)

valorh_entry = ctk.CTkEntry(master=frame, placeholder_text="Valor da Hora:",width=200, font=('Reboco', 14))
valorh_entry.place(x=50, y=110)

prazo_entry = ctk.CTkEntry(master=frame, placeholder_text="Prazo de Entrega em dias:",width=200, font=('Reboco', 14))
prazo_entry.place(x=50, y=140)


tot = ctk.CTkLabel(master=frame, text='Valor total: ',font=('Reboco', 18)).place(x=50, y=190) 




#Back-end

def click_():   
    nome_= nome_entry.get()
    projeto_ = projeto_entry.get()
    hpre_ = hpre_entry.get()
    valorh_ = valorh_entry.get()
    prazo_ = prazo_entry.get()

    lst_orc = [nome_, projeto_, hpre_, valorh_, prazo_]

    for i in lst_orc:
        if i == '':
            messagebox.showerror('ERRO!', 'Preencha todos os campos')
            return
    inserir_(lst_orc)
    messagebox.showinfo('Sucesso!!' 'Dados inseridos')
    
    nome_entry.delete(0,'end')
    projeto_entry.delete(0,'end')
    hpre_entry.delete(0,'end')
    valorh_entry.delete(0,'end')
    prazo_entry.delete(0,'end')
    



btn = ctk.CTkButton(master=frame, text='Gerar Orçamento', command=click_)
btn.place(x=80,y=240)


#importar pdf


'''   
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
        
'''




app.mainloop()