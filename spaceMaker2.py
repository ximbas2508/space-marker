from curses import KEY_DOWN
import pygame
from tkinter import simpledialog

pygame.init()

executando = True
marcacoes = []
pontos = []
item = ''
tecla = pygame.key.get_pressed()
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
        

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring('Space','Nome da Estrela:')
            if item == '':
                item = 'Desconhecido'+str(pos)
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