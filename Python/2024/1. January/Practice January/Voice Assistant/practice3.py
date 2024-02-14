import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 750))
pygame.display.set_caption("voice assistant")

def draw_main(active_color):
    pygame.draw.circle(screen,[150,250,150], (640,375), 250)
    pygame.draw.circle(screen,"black", (640,375), 300, 20)
    pygame.draw.circle(screen,"black", (640,375), 250, 15)
    # logo
    pygame.draw.rect(screen,active_color, (580,185, 125,280), 0, 100 )
    pygame.draw.arc(screen,active_color, (535, 200, 220,300), 3.14, 0, 20)
    pygame.draw.rect(screen,active_color, (625,485, 40,80), 0, 5 )

 
run = True
while run:
    screen.fill((200, 250, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        active_color = 'red'
        if event.type == pygame.MOUSEBUTTONDOWN:
            active_color = 'green'
    
    draw_main(active_color)
    pygame.display.update()

pygame.quit()
quit()