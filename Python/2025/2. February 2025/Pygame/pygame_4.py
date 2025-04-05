import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame_4")

pos_x = 400
pos_y = 300
circle_size = 30
speed = 5


r = 0
g = 0
b = 0
while True:
    screen.fill([50,50,50])
    
    circle_color = [int(r), int(g), int(b)]
    r += 0.25
    g += 0.30
    b += 0.35
    
    if(r > 250): r = 0
    if(g > 250): g = 0
    if(b > 250): b = 0
    
    
    pygame.draw.circle(screen, [0,0,0], (pos_x, pos_y), circle_size+10)
    pygame.draw.circle(screen, circle_color, (pos_x, pos_y), circle_size)
    pygame.draw.circle(screen, [0,0,0], (pos_x+3, pos_y-2), circle_size-20)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    user_input = pygame.key.get_pressed()
    if user_input[pygame.K_UP]: pos_y -= speed
    if user_input[pygame.K_DOWN]: pos_y += speed
    if user_input[pygame.K_LEFT]: pos_x -= speed
    if user_input[pygame.K_RIGHT]: pos_x += speed
    
    pygame.time.delay(30)
    pygame.display.update()
