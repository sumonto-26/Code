import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Project")


def draw_menu():
    pygame.draw.rect(screen, [150, 150, 150], [0,0, WIDTH,80])
    pygame.draw.line(screen, 'Black', (0,80), (WIDTH,80), 5)


    # Draw box for know which size is our Brush
    


    # DRAWING COLOR OPTION'S
    Red = pygame.draw.rect(screen, [250, 10, 50], [1120, 10, 30,30])
    Green = pygame.draw.rect(screen, [150, 250, 150], [1090, 10, 30,30])
    Blue = pygame.draw.rect(screen, [0, 0, 85], [1060, 10, 30,30])
    Black = pygame.draw.rect(screen, [80, 80, 80], [1030, 10, 30,30])
    Yellow = pygame.draw.rect(screen, [250, 250, 150], [1120, 40, 30,30])
    Dark_green = pygame.draw.rect(screen, [0, 85, 0], [1090, 40, 30,30])
    Sky_blue = pygame.draw.rect(screen, [150, 150, 255], [1060, 40, 30,30])
    Orange = pygame.draw.rect(screen, [255, 180, 0], [1030, 40, 30,30])

    Color_list = [Red, Green, Blue, Black, Yellow, Dark_green, Sky_blue, Orange]
    Rgb_list = [[250, 10, 50], [150, 250, 150], [0, 0, 85], [80, 80, 80], [250, 250, 150], [0, 85, 0], [150, 150, 255], [255, 180, 0]]

    # Brush Size Option's
    Big_brush = pygame.draw.rect(screen, [0, 0, 50], [50,15, 50,50])
    pygame.draw.circle(screen, 'light blue', (75, 40), 18)
    Medium_brush = pygame.draw.rect(screen, [0, 0, 50], [110,15, 50,50])
    pygame.draw.circle(screen, 'light blue', (135, 40), 15)
    Small_brush = pygame.draw.rect(screen, [0, 0, 50], [170,15, 50,50])
    pygame.draw.circle(screen, 'light blue', (195, 40), 10)
    Tiny_brush = pygame.draw.rect(screen, [0, 0, 50], [230,15, 50,50])
    pygame.draw.circle(screen, 'light blue', (255, 40), 5)

    Brush_list = [Big_brush, Medium_brush, Small_brush, Tiny_brush]
    

    return Color_list, Rgb_list, Brush_list


run = True
while run:
    screen.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_menu()
    pygame.display.update()

pygame.quit()