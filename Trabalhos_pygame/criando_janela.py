import pygame
pygame.init()

largura = 400
altura = 300
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('KING KONG')

deve_continuar = True
while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False
pygame.quit()