import pygame
import pickle
from tkinter import simpledialog
from tkinter import messagebox

pygame.init()

executando = True
marcacoes = []
pontos = []
item = ''
pos = 0, 0
fonte = pygame.font.Font(None,24)
cor_ponto = (255,255,255)
largura = 800
altura = 600
janela = pygame.display.set_mode((largura,altura))



pygame.display.set_caption('SPACE MAKER')
icon = pygame.image.load('conteudo/space.jpg')
pygame.display.set_icon(icon)
background_image = pygame.image.load('conteudo/bg.jpg')
background_image = pygame.transform.scale(background_image,(largura,altura))
pygame.mixer.music.load('conteudo\Space_Machine_Power.mp3')
pygame.mixer.music.play(-1) 

def desenhar_pontos():
    for i in range(len(marcacoes)):
        nome, posicao = marcacoes[i]
        x, y = posicao
        pygame.draw.circle(janela, cor_ponto, (x, y), 5)
        texto = fonte.render(nome, True, cor_ponto)
        janela.blit(texto, (x + 10, y - 10))
        if len(marcacoes) > 1:
            for i in range(len(pontos) - 1):
                pygame.draw.line(janela, cor_ponto, pontos[i], pontos[i + 1], 2)

def salvar(filename, marcacoes):
    try:
        with open(filename, "wb") as file:
            pickle.dump(marcacoes, file)
            print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
    finally:
        file.close()


def carregar(filename):
    try:
        with open(filename, "rb") as file:
            item = pickle.load(file)
            return item
    except FileNotFoundError:
        return []




while executando:
    for evento in pygame.event.get():
        keys = pygame.key.get_pressed()
        if evento.type == pygame.QUIT:
            executando = False


        elif keys[pygame.K_a]:
            certeza = messagebox.askquestion('Space','realmente deseja salvar?')
            if certeza == 'sim':
                salvar("dados.pickle", marcacoes)
                print("Dados salvos com sucesso!")
            else:
                break

        elif keys[pygame.K_d]:
            item = carregar("dados.pickle")
            print("Dados carregados com sucesso!")



        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring('Space','Nome da Estrela:')
            if item == '':
                item = 'Desconhecido'
            if item == None:
                break
            else:
                item = item + str(pos) 
            pontos.append(pos)
            desenhar_pontos()
            marcacoes.append((item,pos))
            print(item)

    janela.blit(background_image, (0,0))
    desenhar_pontos()
    pygame.display.flip()





pygame.quit()        