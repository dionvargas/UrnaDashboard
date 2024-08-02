import tkinter as tk
from tkinter import ttk
import os.path
import datetime
import pygame
from model.Voto import Voto
from PIL import Image, ImageTk

class InterfaceUrna:
    def __init__(self,questoes, db_manager):
        self.db_manager = db_manager
        self.questoes = questoes
        self.qtdQuestoes = len(questoes)
        self.questaoAtual = 0
        self.usuarioAtual = Voto.getLastVoteUser(self.db_manager)
        self.usuarioAtual += 1
        pygame.init()

        self.root = tk.Tk()

        self.root.title("Urna Digital")
        self.root.geometry("600x980")  # Define o tamanho da tela

        imageLogo = ImageTk.PhotoImage(Image.open("./static/images/senaiFundo.jpg"))
        logo = tk.Label(self.root, image=imageLogo)
        logo.pack(pady=20)

        ## Cria um frame com com as a mensagem inicial
        self.formInicial = tk.Frame(self.root)
        self.formInicial.pack(expand=True)

        self.mensagem_bemvindo = tk.Label(self.formInicial, text="Bem-vindo(a) a nossa urna eletrônica. \n Você é nosso "+ str(self.usuarioAtual) +"° entrevistado", font=("Helvetica", 20))
        self.mensagem_bemvindo.pack(pady=200)

        botaoStart = tk.Button(self.formInicial, text="Começar", command=self.atualizaInterface, font=("Helvetica", 20), height=2, width=20)
        botaoStart.pack()

        ## Cria um frame com com as perguntas e botões
        self.questionForm = tk.Frame(self.root)
        self.questionForm.pack(expand=True)  # Expande o frame junto com a janela

        # Título superior
        self.titulo = tk.Label(self.questionForm, text="Pergunta", font=("Helvetica", 20), wraplength=580)
        self.titulo.pack(pady=10)

        # Imagens para os botões
        imagem1 = Image.open("./static/images/semImagem.jpeg").resize((250, 250))
        imagem2 = Image.open("./static/images/semImagem.jpeg").resize((250, 250))
        imagem3 = Image.open("./static/images/semImagem.jpeg").resize((250, 250))
        imagem4 = Image.open("./static/images/semImagem.jpeg").resize((250, 250))

        # Converter imagens para o formato suportado pelo tkinter
        img1 = ImageTk.PhotoImage(imagem1)
        img2 = ImageTk.PhotoImage(imagem2)
        img3 = ImageTk.PhotoImage(imagem3)
        img4 = ImageTk.PhotoImage(imagem4)

        # Frame para os botões
        botoes_frame_l1 = tk.Frame(self.questionForm)
        botoes_frame_l1.pack(expand=True)  # Expande o frame junto com a janela
        botoes_frame_l2 = tk.Frame(self.questionForm)
        botoes_frame_l2.pack(expand=True)  # Expande o frame junto com a janela

        # Botões com espaçamento e texto abaixo da imagem
        self.botao1 = tk.Button(botoes_frame_l1, image=img1, text="alternativaA", compound="bottom", padx=10, pady=10)
        self.botao2 = tk.Button(botoes_frame_l1, image=img2, text="alternativaB", compound="bottom", padx=10, pady=10)
        self.botao3 = tk.Button(botoes_frame_l2, image=img3, text="alternativaC", compound="bottom", padx=10, pady=10)
        self.botao4 = tk.Button(botoes_frame_l2, image=img4, text="alternativaD", compound="bottom", padx=10, pady=10)

        self.botao1.config(command=self.clickBtnA)
        self.botao2.config(command=self.clickBtnB)
        self.botao3.config(command=self.clickBtnC)
        self.botao4.config(command=self.clickBtnD)

        # Grid 2x2 para os botões
        self.botao1.pack(side="left")
        self.botao2.pack(side="left")
        self.botao3.pack(side="left")
        self.botao4.pack(side="left")

        # Rodapé
        self.rodape = tk.Label(self.questionForm, text="Pergunta x/" + str(self.qtdQuestoes), font=("Helvetica", 16))
        self.rodape.pack(pady=20)

        ## Cria um frame com com as a mensagem final
        self.formFinal = tk.Frame(self.root)
        self.formFinal.pack(expand=True)

        mensagem_final = tk.Label(self.formFinal, text="Muito obrigado por participar da nossa pesquisa.", font=("Helvetica", 20))
        mensagem_final.pack(pady=200)

        botaoStart = tk.Button(self.formFinal, text="Próximo participante", command=self.atualizaInterface, font=("Helvetica", 20),height=2, width=20)
        botaoStart.pack()

        self.atualizaInterface()

    def novaPergunta(self, nova_questao):
        # Atualize o texto do rótulo superior
        self.titulo.config(text=nova_questao.pergunta)

        if(os.path.exists("./static/images/" + str(nova_questao.id) + "/")):
            # Carregue as novas imagens (se necessário)
            nova_imagem1 = Image.open("./static/images/"+str(nova_questao.id)+"/a.png").resize((250, 250))
            nova_imagem2 = Image.open("./static/images/"+str(nova_questao.id)+"/b.png").resize((250, 250))
            nova_imagem3 = Image.open("./static/images/"+str(nova_questao.id)+"/c.png").resize((250, 250))
            nova_imagem4 = Image.open("./static/images/"+str(nova_questao.id)+"/d.png").resize((250, 250))
        else:
            # Imagens para os botões
            nova_imagem1 = Image.open("./static/images/semImagem.jpeg").resize((250, 250))
            nova_imagem2 = Image.open("./static/images/semImagem.jpeg").resize((250, 250))
            nova_imagem3 = Image.open("./static/images/semImagem.jpeg").resize((250, 250))
            nova_imagem4 = Image.open("./static/images/semImagem.jpeg").resize((250, 250))

        # Atualize as imagens dos botões
        img1 = ImageTk.PhotoImage(nova_imagem1)
        img2 = ImageTk.PhotoImage(nova_imagem2)
        img3 = ImageTk.PhotoImage(nova_imagem3)
        img4 = ImageTk.PhotoImage(nova_imagem4)

        self.botao1.config(image=img1, text=nova_questao.alternativaA)
        self.botao2.config(image=img2, text=nova_questao.alternativaB)
        self.botao3.config(image=img3, text=nova_questao.alternativaC)
        self.botao4.config(image=img4, text=nova_questao.alternativaD)

        self.rodape.configure(text="Pergunta "+ str(nova_questao.id) + "/" + str(self.qtdQuestoes))

        # Redesenha a interface
        self.root.update()
        self.root.mainloop()

    def atualizaInterface(self):
        self.formInicial.pack_forget()  # Oculta o frame incial
        self.questionForm.pack_forget() # Oculta o formulário de perguntas
        self.formFinal.pack_forget()    # Oculta o frame final

        if(self.questaoAtual == 0):
            self.mensagem_bemvindo.configure(text="Bem-vindo(a) a nossa urna eletrônica. \n Você é nosso "+ str(self.usuarioAtual) +"° entrevistado")
            self.formInicial.pack()
            self.questaoAtual += 1
            # Redesenha a interface
            self.root.update()
            self.root.mainloop()

        else:
            if(self.questaoAtual <= self.qtdQuestoes):
                self.questionForm.pack()
                nova_questao = self.questoes[self.questaoAtual-1]
                if(self.questaoAtual != 1):
                    pygame.mixer.music.load("./static/sounds/confirma.mp3")
                    pygame.mixer.music.play()
                self.questaoAtual += 1
                self.novaPergunta(nova_questao)
            else:
                self.usuarioAtual += 1
                self.formFinal.pack()
                self.questaoAtual = 0
                pygame.mixer.music.load("./static/sounds/finalizando.mp3")
                pygame.mixer.music.play()

    def clickBtnA(self):
        print("Botão A clicado")
        Voto(self.questaoAtual-1, "A", self.usuarioAtual, self.getDataHoraAtual()).vote(self.db_manager)
        self.atualizaInterface()

    def clickBtnB(self):
        print("Botão B clicado")
        Voto(self.questaoAtual-1, "B", self.usuarioAtual, self.getDataHoraAtual()).vote(self.db_manager)
        self.atualizaInterface()

    def clickBtnC(self):
        print("Botão C clicado")
        Voto(self.questaoAtual-1, "C", self.usuarioAtual, self.getDataHoraAtual()).vote(self.db_manager)
        self.atualizaInterface()

    def clickBtnD(self):
        print("Botão D clicado")
        Voto(self.questaoAtual-1, "D", self.usuarioAtual, self.getDataHoraAtual()).vote(self.db_manager)
        self.atualizaInterface()

    def getDataHoraAtual(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
