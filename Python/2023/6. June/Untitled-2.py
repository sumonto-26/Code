import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption('runner')
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200))
test_surface.fill('Red')

while True:
    # draw all our elements
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(test_surface,(200,100))
    pygame.display.update()

