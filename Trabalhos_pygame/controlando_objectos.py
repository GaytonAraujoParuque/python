import pygame
from pygame.locals import *
from sys import exit

pygame.init()

preto = (0, 0, 0)
branco = (225, 225, 225)
vermelho = (225, 0, 0)
verde = (0, 225, 0)
azul = (0, 0, 225)
amarelo = (225, 225, 0)
rosa = (225, 0, 225)
azul_ciano = (0, 225, 225)
caqui = (211.77, 202.95, 123.525)

largura = 800
altura = 500
x = largura / 2 - 50
y = altura / 2 - 50
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Mickey Mouse')
relogio = pygame.time.Clock()

deve_continuar = True
while deve_continuar:
    relogio.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False

        if event.type == KEYDOWN:
            if event.key == K_a:
                x -= 10

            if event.key == K_d:
                x += 10

            if event.key == K_w:
                y -= 10

            if event.key == K_s:
                y += 10

    if pygame.key.get_pressed()[K_a]:
        x -= 10

    if pygame.key.get_pressed()[K_d]:
        x += 10

    if pygame.key.get_pressed()[K_w]:
        y -= 10

    if pygame.key.get_pressed()[K_s]:
        y += 10


    janela.fill(rosa)

    pygame.draw.rect(janela, azul, (x, y, 100, 100))
   

    pygame.display.update()

pygame.quit()