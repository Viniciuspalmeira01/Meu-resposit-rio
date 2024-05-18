from tkinter import *
from customtkinter import *
from PyPDF2 import *


class Frame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = CTkLabel(self)
        self.label.pack(padx=20)

        self.name = CTkEntry(self, placeholder_text='nome do arquivo', bg_color='white')
        self.name.pack(pady=20)
        
        arquivo = f' {self.name.get()}.pdf'

class Window(CTk):
    def __init__(self):
        super().__init__()
        self.title('Reader')
        self.geometry('600x300')
        self.index = int(0)
        self.paginas = num_pages
        self.pdf_textos = {'Inicio':'0'}

        self.frame = Frame(self)
        self.frame.pack(pady= 40)

        self.arquivo = CTkInputDialog(self,text='nome do arquivo', text_color='green')

        self.advanced = CTkButton(self.frame,width=140 , height=28, text ='+', command = leitura)
        self.advanced.pack(pady=20)
        
        self.exibir = CTkLabel(self, text ='')
        self.exibir.pack(pady=30)

        link = self.arquivo.get()
        
        self.tela = CTkFrame(self)
        self.tela.pack(pady=40)

        with open (f'{link}', 'r') as arquivo01:
            pdf = PdfReader(arquivo01)
            num_pages = len(pdf.pages)
            textos = pdf.pages[0]

            update_label()

        def update_label():
            pagina = self.paginas[self.index]
            texto = f'{pagina}: {textos[pagina]}'
            self.tela.configure(text=texto)  
            for i in range(self.paginas):
                pagina = pdf.pages[i]   
                texto = pagina.extract_text()
                self.pdf_textos[f'{i+1}-Pagina'] = texto
            return self.exibir.configure(text =self.pdf_textos)
        
        def leitura():
            if self.index < len(self.paginas) - 1:
                self.index += 1
            else:
                self.index = 0  # Reinicia para a primeira página ao chegar ao fim
        self.exibir.update()

if __name__ == '__main__':
    app = Window()
    app.mainloop()
