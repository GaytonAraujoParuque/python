import pygame
pygame.init()

x = 100
y = 50
largura = 500
altura = 500
verde = (0, 225, 0)
vermelho = (225, 0, 0)
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('GODZILa')

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False     
    janela.fill(verde)
    pygame.draw.rect(janela, vermelho, (x, y, 50, 50))
    if x < 450:
        x += 1
    if x == 450 and y < 450:
        y += 1
    if x == 450 and y == 450:
        x = 0
        y = 0

    pygame.display.update()
pygame.quit()