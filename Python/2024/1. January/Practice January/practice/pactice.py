import pygame
import random

pygame.init()

WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("practice")

# Define a Font
text_font = pygame.font.SysFont( None, 40, bold=True, italic=True)

# make a function for draw our text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

# rect formula's
def draw_easy_rect(color, x, y, width, height):
    pygame.draw.rect(screen, color, (x, y, width, height))

def draw_hard_rect(color, x, y, width, height, out_line, bottom_right, top_left, top_right, bottom_left):
    pygame.draw.rect(screen, color, (x, y, width, height), out_line, bottom_right, top_left, top_right, bottom_left)

# circle formula's
def draw_easy_circle(color, x,y, size):
    pygame.draw.circle(screen, color, (x,y),size)

def draw_hard_circle(color, x,y, size, out_line):
    pygame.draw.circle(screen, color, (x,y), size, out_line, draw_top_right= True, draw_bottom_left=True)


# ellipse formula
def draw_ellipse(color, x, y, width, height):
    pygame.draw.ellipse(screen, color, (x,y, width, height))

# arc formula's
def draw_arc(color, x,y,width, height, start_angle, end_angle, out_line):
    pygame.draw.arc(screen, color, (x,y, width, height), start_angle, end_angle, out_line )


# line formula
def draw_line(color, start_x, start_y, end_x, end_y, line_width):
    pygame.draw.line(screen, color, (start_x, start_y), (end_x, end_y), line_width)


# gaming loop
run = True
while run:

    screen.fill((150, 150, 200))

    draw_easy_rect('green', 300, 500, 100, 100)
    draw_hard_rect('red', 500, 500, 140, 140, 10, 30, 25, 60, 50)

    draw_text("Easy", text_font, 'dark green', x=315, y=530 )
    draw_text("Hard", text_font, 'dark red', x=530, y=550 )

    draw_easy_circle('green', 150, 100, 30)
    draw_hard_circle('red', 500, 100, 30, 0)

    draw_ellipse('green', 500, 200, 50, 160)

    draw_arc('red', 200,300, 150,150, 2, 7, 5)

    draw_line('green', 100, 350 , 350, 100, 5)

    # polygon formulas
    # pygame.draw.polygon(screen, color, (more than [2 * (x,y)] other wise it thows error))
    pygame.draw.polygon(screen,"green", ((600, 460), (740,300), (750, 200), (800, 400)))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    pygame.display.update()

pygame.quit()
quit()