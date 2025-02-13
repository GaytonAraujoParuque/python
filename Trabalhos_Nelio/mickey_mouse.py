import pygame
pygame.init()

preto = (0, 0, 0)
branco = (225, 225, 225)
verde = (0, 225, 0)

largura = 700
altura = 700
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Ola Mickey')
janela.fill(verde)

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False


    pygame.draw.circle(janela, preto, (200, 200), 130)
    pygame.draw.circle(janela, preto, (600, 200), 130)      
    pygame.draw.circle(janela, preto, (400, 400), 200)
    pygame.draw.circle(janela, branco, (325.50, 350), 25)
    pygame.draw.circle(janela, branco, (475, 350), 25)
    pygame.draw.rect(janela, branco, (300, 350, 50, 30))
    pygame.draw.rect(janela, branco, (450, 350, 50, 30))
    pygame.draw.circle(janela, branco, (475, 380), 25)
    pygame.draw.circle(janela, branco, (325, 380), 25)
    pygame.draw.circle(janela, preto, (325, 365), 15)
    pygame.draw.circle(janela, preto, (475, 365), 15)


    pygame.display.update()

pygame.quit()