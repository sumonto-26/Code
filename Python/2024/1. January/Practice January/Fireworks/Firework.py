# copied py LeMaster Tech's video

import pygame
import random

pygame.init()

WIDTH = 500
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)  # New
pygame.display.set_caption("Fireworks")
FPS = 60
timer = pygame.time.Clock()

# For fireworks
fireworks = []
counter = 0
new_fireworks = True
Color_list = [(150, 255, 150), (255, 150, 150), (150, 150, 255), (255, 255, 255)]
projectiles = []


def draw_fireworks(firework_list, projectile_list):
    remove = []
    # putting this line here constantly refreshes the surface; comment it out if you want tails
    surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1),(-1, 0), (-1, -1), (2, 0), (-2, 0), (0, 2), (0, -2), (2, 2), (2, -2), (-2, 2), (-2, -2)]
    for i in range(len(firework_list)):
        if firework_list[i][3] < counter and firework_list[i][2] < firework_list[i][1]:
            pygame.draw.rect(screen, firework_list[i][4], [firework_list[i][0], firework_list[i][1], 15, 15], 0, 5)
            firework_list[i][1] -= firework_list[i][5]
        elif firework_list[i][2] >= firework_list[i][1]:
            x_start = firework_list[i][0]
            y_start = firework_list[i][1]
            # each projectile needs to start from x and y start and go outward in different directions
            for j in range(len(directions)):
                projectile_list.append([x_start, y_start, directions[j][0] * 3, directions[j][1] * 3, firework_list[i][4], 60])

            remove.append(i)
    remove.sort(reverse=True)
    for r in remove:
        firework_list.pop(r)

    # projectile code
    remove = []
    for i in range(len(projectile_list)):
        color = projectile_list[i][4][0], projectile_list[i][4][1], projectile_list[i][4][2], projectile_list[i][5] * 4
        pygame.draw.circle(surface, color, (int(projectile_list[i][0]), int(projectile_list[i][1])), 4)
        projectile_list[i][5] -= 1
        projectile_list[i][0] += projectile_list[i][2]
        projectile_list[i][1] += projectile_list[i][3]
        projectile_list[i][3] += 0.1
        if projectile_list[i][5] < 0 or projectile_list[i][0] < -3 or HEIGHT < projectile_list[i][0]:
            remove.append(i)
    for p in range(len(remove)):
        projectile_list.pop(0)
    screen.blit(surface, (0, 0))

    return firework_list, projectile_list


run = True
while run:

    timer.tick(FPS)
    screen.fill([0, 0, 0])
    counter += 1

    if new_fireworks:
        for i in range(30):
            # starting x_pos, explosion height, delay before launching, color, y_speed
            fireworks.append(
                [random.randint(10, WIDTH - 10), HEIGHT, random.randint(10, HEIGHT // 2), random.randint(0, 300),
                 random.choice(Color_list), random.randint(6, 7)]
            )
        new_fireworks = False

    fireworks, projectiles = draw_fireworks(fireworks, projectiles)

    if not fireworks and not projectiles:
        counter = 0
        new_fireworks = True
        surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
