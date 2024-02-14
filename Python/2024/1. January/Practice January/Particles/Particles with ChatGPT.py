import pygame
import sys
import random

class Particle:
    def __init__(self):
        self.particles = []

    def emit(self):
        self.delete_particles()
        for particle in self.particles:
            particle[0][0] += particle[2]
            particle[0][1] += particle[3]
            particle[1] -= 0.2 # make small
            pos = (int(particle[0][0]), int(particle[0][1]))
            pygame.draw.circle(screen, 'black', pos, int(particle[1]))
            pygame.draw.circle(screen, [0,random.randint(0,255),10], pos, int(particle[1] - 3))

    def add_particles(self, mouse_pos):
        x_pos, y_pos = mouse_pos # to get mouse position
        radius = 10 # circle size
        # make random direction
        direction_x = random.randint(-1, 1) 
        direction_y = random.randint(-1, 1)
        particle_circle = [[x_pos, y_pos], radius, direction_x, direction_y]
        self.particles.append(particle_circle)

    def delete_particles(self):
        self.particles = [particle for particle in self.particles if particle[1] > 1]

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
PARTICLE_EVENT = pygame.USEREVENT + 1
particle1 = Particle()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == PARTICLE_EVENT:
            particle1.add_particles(pygame.mouse.get_pos())

        
    screen.fill((50, 50, 50))
    particle1.emit()
    pygame.display.flip()
    clock.tick(60)
