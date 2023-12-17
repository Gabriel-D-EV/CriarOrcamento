import customtkinter as ctk
from tkinter import *
from fpdf import FPDF
from tkinter import messagebox
from view import *
import sqlite3 as lite





    

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('dark-blue')

app = ctk.CTk()
app.geometry('600x350')
app.title('Orçamentos')
app.iconbitmap('./img/favicon.ico')
app.resizable(False, False)

img = PhotoImage(file='./img/gbh-tech.png')
label_img = ctk.CTkLabel(master=app, image=img)
label_img.place(x=1, y=25)

#Front-end

frame = ctk.CTkFrame(master=app, width=300, height=350)
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




#Back-end
global lst_org

def click_():   
    nome = nome_entry.get()
    projeto = projeto_entry.get()
    hpre = hpre_entry.get()
    hpre = float(hpre)
    valorh = valorh_entry.get()
    valorh = float(valorh)
    prazo = prazo_entry.get()
    total = valorh * hpre
    

    lst_orc = [nome, projeto, hpre, valorh, prazo]
    

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
    
    tot = ctk.CTkLabel(master=frame, text=f'Valor total: R${total:.2f}',font=('Reboco', 18)).place(x=50, y=180) 
    
       
def imprimir_():
    try:
        cx = lite.connect('dados.db')
        cursor = cx.cursor()
        cursor.execute("SELECT  Nome, Projeto, Horas_Prevista, Valor_Hora, Prazo FROM Orcamento WHERE id = 1")
            
        Nome, Projeto, Horas_Prevista, Valor_Hora, Prazo = cursor.fetchone()        
        
        Horas_Prevista = int(Horas_Prevista)
        Valor_Hora = float(Valor_Hora)
        total = Horas_Prevista * Valor_Hora
        total = "{:.2f}".format(total)
        Horas_Prevista = str(Horas_Prevista)
        Valor_Hora = "{:.2f}".format(Valor_Hora)
        Prazo = str(Prazo)
        
        cx.close()
    
          
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 20)
        pdf.image('./img/formulario.png', x=0, y=0)
        
        pdf.text(115, 145, Projeto)
        pdf.text(115, 160, f'{Horas_Prevista}h')
        pdf.text(115, 175, Valor_Hora)
        pdf.text(115, 190, Prazo)
        pdf.text(120, 205, total)
        pdf.text(120, 255, f'Assinatura do(a) {Nome}')
        pdf.output(f'Orçamento do {Nome}.pdf')
        
    except Exception as e:
        messagebox.showerror('ERRO!', f'Erro ao gerar pdf: {str(e)}')
    
try:
    del_()
except Exception as e:
    messagebox.showerror('ERRO!', f'Erro ao deletar usuario: {str(e)}')        
        





btn = ctk.CTkButton(master=frame, text='Salvar', command=click_)
btn.place(x=80,y=220)

btn2 = ctk.CTkButton(master=frame, text='Gerar Orçamento', command=imprimir_)
btn2.place(x=80,y=260)

btn3 = ctk.CTkButton(master=frame, text='Finalizar', command=del_)
btn3.place(x=80,y=300)


app.mainloop()
