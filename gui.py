import pyqrcode
from tkinter import *
from PIL import ImageTk, Image


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="QRCode Generator")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.urlLabel = Label(self.segundoContainer, text="URL:", font=self.fontePadrao)
        self.urlLabel.pack(side=LEFT)

        self.url = Entry(self.segundoContainer)
        self.url["width"] = 40
        self.url["font"] = self.fontePadrao
        self.url.pack(side=RIGHT)

        self.nomeLabel = Label(self.terceiroContainer, text="File name:", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.terceiroContainer)
        self.nome["width"] = 40
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=RIGHT)

        self.escalaLabel = Label(self.quartoContainer, text="Size:", font=self.fontePadrao)
        self.escalaLabel.pack(side=LEFT)

        self.escala = Entry(self.quartoContainer)
        self.escala["width"] = 40
        self.escala["font"] = self.fontePadrao
        self.escala.pack(side=RIGHT)

        self.gerarcode = Button(self.quintoContainer)
        self.gerarcode["text"] = "Generate"
        self.gerarcode["font"] = ("Calibri", "8")
        self.gerarcode["width"] = 12
        self.gerarcode["command"] = self.generator
        self.gerarcode.pack(side=RIGHT)

        self.sair = Button(self.quintoContainer)
        self.sair["text"] = "Quit"
        self.sair["font"] = ("Calibri", "8")
        self.sair["width"] = 12
        self.sair["command"] = self.quintoContainer.quit
        self.sair.pack(side=LEFT)

        self.mensagem = Label(self.quintoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    # Gerador
    def generator(self):
        link = self.url.get()
        n = self.nome.get()
        es = self.escala.get()
        qr = pyqrcode.create(link)

        qr.png(n + ".png", scale=es)
        self.mensagem["text"] = "QRCode Successful!!"


root = Tk()
root.title("QRCode Generator")
root.iconbitmap('qricon.ico')
Application(root)
root.mainloop()
