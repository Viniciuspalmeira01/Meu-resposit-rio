import customtkinter as ctk
from tkinter import *

vini={'palmeiravinicius@gmail.com':'alquimia190'}#Cliente inicial

janela_inicial=ctk.CTk()#rodando a janela
janela_inicial.geometry('800x420')
janela_inicial.title('Janela inicial')

frame = ctk.CTkFrame(janela_inicial, width=300 , height=350, corner_radius=41)
frame.pack(pady=20)

email= ctk.CTkEntry(frame,placeholder_text='Seu email', fg_color='white', text_color='black',width=200  )
email.pack(padx=20,pady=10)

password =  ctk.CTkEntry(frame, placeholder_text='password', show ='*', fg_color='white', text_color='black', width=200)
password.pack(pady=20)

label = ctk.CTkLabel(janela_inicial, text='')
def login():
        for x in vini.items():
            if x == {'palmeiravinicius@gmail.com:alquimia190'}:
                  label.configure(text='Acesso permitido')
                  janela_inicial.destroy()
            else:
                  label.configure(text='Acesso negado,tente novamente.')

button = ctk.CTkButton(frame , width=140 , height=28 , corner_radius=36 ,command=login, hover_color='gray' , fg_color='green')
button.pack(pady=30)

janela_inicial.mainloop()                             
