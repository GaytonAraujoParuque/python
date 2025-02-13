import pygame
pygame.init()

preto = (0, 0, 0)
branco = (225, 225, 225)
vermelho = (225, 0, 0)
verde = (0, 225, 0)
azul = (0, 0, 225)
amarelo = (225, 225, 0)
roxo = (225, 0, 225)
azul_ciano = (0, 225, 225)
caqui = (211.77, 202.95, 123.525)

largura = 800
altura = 700
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Projeto pygame')
janela.fill(verde)

pygame.display.update()
deve_continuar = True
while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False

    pygame.draw.circle(janela, azul, (20, 20), 10)
    pygame.draw.rect(janela, amarelo, (40, 10, 20, 20))
    pygame.draw.line(janela, vermelho, (25, 40), (40, 40), 4)

    pygame.display.update()
  
pygame.quit()
