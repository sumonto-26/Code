import pygame
pygame.init()

FPS = 60
timer = pygame.time.Clock()
WIDTH = 1200
HEIGHT = 700
active_size = 0
active_color = [255, 255, 255]
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint")
painting = []


def draw_menu(active_size, active_color):
    pygame.draw.rect(screen, [150,150,150], [0,0, WIDTH, 70])
    pygame.draw.line(screen, [0,0,0], (0,1), (WIDTH, 1), 7)
    pygame.draw.line(screen, [0,0,0], (0,70), (WIDTH, 70), 5)
    pygame.draw.rect(screen, [150,150,150], [0,640, WIDTH, 70])
    pygame.draw.line(screen, [0,0,0], (0,697), (WIDTH, 697), 5)
    pygame.draw.line(screen, [0,0,0], (0,637), (WIDTH, 637), 5)

    # BRUSH'S
    xl_brush = pygame.draw.rect(screen, [0,0,80], [30, 11, 50, 50])
    pygame.draw.circle(screen, active_color, (55, 35), 18)
    l_brush = pygame.draw.rect(screen, [0,0,80], [90, 11, 50, 50])
    pygame.draw.circle(screen, active_color, (115, 35), 15)
    m_brush = pygame.draw.rect(screen, [0,0,80], [150, 11, 50, 50])
    pygame.draw.circle(screen, active_color, (175, 35), 10)
    s_brush = pygame.draw.rect(screen, [0,0,80], [210, 11, 50, 50])
    pygame.draw.circle(screen, active_color, (235, 35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]


    if active_size == 20:
        pygame.draw.rect(screen, [255, 10, 0], [30, 10, 55, 55], 5)
    elif active_size == 15:
        pygame.draw.rect(screen, [255, 10, 0], [90, 10, 50, 50], 5)
    elif active_size == 10:
        pygame.draw.rect(screen, [255, 10, 0], [150, 10, 50, 50], 5)
    elif active_size == 5:
        pygame.draw.rect(screen, [255, 10, 0], [210, 10, 50, 50], 5)


    # make some colour
    blue = pygame.draw.rect(screen, (150, 150, 255), [WIDTH - 65 , 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 30, 50), [WIDTH - 90, 10, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 10), [WIDTH - 115, 10, 25, 25])
    black = pygame.draw.rect(screen, (15, 15, 15), [WIDTH - 140, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (250, 250, 150), [WIDTH - 65 , 35, 25, 25])
    pink = pygame.draw.rect(screen, (250, 135, 225), [WIDTH - 90, 35, 25, 25])
    purple = pygame.draw.rect(screen, (170, 70, 200), [WIDTH - 115, 35, 25, 25])
    gray = pygame.draw.rect(screen, (70, 70, 70), [WIDTH - 140, 35, 25, 25])

    colour_option = [blue, red, green, black, yellow, pink, purple, gray]
    rgb_list = [(150, 150, 255), (255, 30, 50), (0, 255, 10), (15, 15, 15), (250, 250, 150), (250, 135, 225), (170, 70, 200), (70, 70, 70)]

    return brush_list, colour_option, rgb_list


def draw_painting(paints):
    for color, pos, size in paints:
        pygame.draw.circle(screen, color, pos, size)



run = True
while run:
    timer.tick(FPS)
    screen.fill([255, 255, 255])
    mouse = pygame.mouse.get_pos()
    left_button = pygame.mouse.get_pressed()[0]
    if left_button and mouse[1] > 70:
            painting.append((active_color, mouse, active_size))
    draw_painting(painting)
    if mouse[1] > 70:
        pygame.draw.circle(screen, active_color, mouse, active_size)
    brushes, colors, rgb_list = draw_menu(active_size, active_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)

            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgb_list[i]
                    
        if event.type == pygame.KEYDOWN:
            painting = []


    pygame.display.flip()


pygame.quit()