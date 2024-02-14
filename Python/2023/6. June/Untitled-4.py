import pygame
pygame.init()
white = pygame.Color(' white')
# Or, white = [255, 255, 255]

screen = pygame.display.set_mode((600, 600))

run = True
while run == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
            
pygame.display.update()            