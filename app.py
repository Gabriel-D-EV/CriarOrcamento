import customtkinter as ctk

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('dark-blue')

app = ctk.CTk()
app.geometry('500x350')
app.title('Orçamentos')
app.iconbitmap('favicon.ico')

frame = ctk.CTkFrame(master=app, width=495, height=345)
frame.pack()

projeto = ctk.CTkEntry(master=frame, placeholder_text="Projeto",width=350, font=('Reboco', 14)).place(x=50, y=20)

'''hpre = ctk.CTkEntry(master=frame, placeholder_text="Projeto")
valorh = ctk.CTkEntry(master=frame, placeholder_text="Projeto")
totvalor = ctk.CTkEntry(master=frame, placeholder_text="Projeto")


'''


app.mainloop()