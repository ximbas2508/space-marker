import pygame
from tkinter import simpledialog
from tkinter import messagebox
import json

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


def salvar():
    with open("stars.json", "w") as file:
        json.dump(marcacoes, file)

def carregar():
    global marcacoes

    try:
        with open("stars.json", "r") as file:
            marcacoes = json.load(file)
    except FileNotFoundError:
        marcacoes = []


def excluir():
    global marcacoes
    marcacoes = []

if marcacoes == []:
    certeza2 = messagebox.askquestion('Space','deseja continuar com os ultimos dados salvos?')
    if certeza2 == 'yes':
        carregar()
    else:
        pass
    

while executando:
    for evento in pygame.event.get():
        keys = pygame.key.get_pressed()
        if evento.type == pygame.QUIT:
            executando = False
            salvar()


        elif keys[pygame.K_F1]:
            certeza = messagebox.askquestion('Space','realmente deseja salvar?')
            if certeza == 'yes':
                salvar()
                print("Dados salvos com sucesso!")
            else:
                break

        elif keys[pygame.K_F2]:
            certeza3 = messagebox.askquestion('Space','realmente deseja carregar?')
            if certeza3 == 'yes':
                carregar()
                print("Dados carregados com sucesso!")
            else:
                pass

        elif keys[pygame.K_F3]:
            certeza4 = messagebox.askquestion('Space','realmente deseja carregar?')
            
            if certeza4 =='yes':
                excluir()
                print('dados excluidos com sucesso')
            else:
                pass


        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
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


    texto_instrucoes = fonte.render(f"Pressione F1 para salvar", True, cor_ponto)
    texto_instrucoes2 = fonte.render(f"Pressione F2 para carregar", True, cor_ponto)
    texto_instrucoes3 = fonte.render(f"Pressione F3 para excluir", True, cor_ponto)
    janela.blit(texto_instrucoes, (10, 10))
    janela.blit(texto_instrucoes2, (10, 30))
    janela.blit(texto_instrucoes3, (10, 50))
    
    pygame.display.flip()



pygame.quit()        