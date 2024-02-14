import pygame

def scale_image(img, size):
    a = round(img.get_width() * size), round(img.get_height() * size)
    return pygame.transform.scale(img,a)

def blit_rotate_center(win, image, top_left, angle): # bujhi nai
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center = image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)

def blit_text_center(win, font, text):
    render = font.render(text, 1, (0, 0, 0))
    win.blit(render, (win.get_width()/2 - render.get_width()/
    2, win.get_height()/2 - render.get_height()/2))