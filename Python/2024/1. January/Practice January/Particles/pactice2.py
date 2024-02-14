# time --> 10:22 - 11:12
# copied by Clear Code
import pygame
import sys
import random

pygame.init()


class Particle:
    def __init__(self):
        self.particles = []

    def emit(self, color):
    # Remove particles that have a circle_size less than or equal to 0
        self.delete_particles()
    
        # Loop through each particle
        for particle in self.particles:
            # Update particle position based on its direction
            particle[0][0] += particle[2]
            particle[0][1] += particle[3]
            
            # Decrease the size of the particle
            particle[1] -= 0.2
            
            # Get the integer position of the particle
            pos = (int(particle[0][0]), int(particle[0][1]))
            
            # Draw circle's
            pygame.draw.circle(screen, 'black', pos, int(particle[1]))
            pygame.draw.circle(screen, color, pos, int(particle[1] - 3))

    def add_particles(self):
        x_pos, y_pos = pygame.mouse.get_pos()
        circle_size = 10
        direction_x = random.randint(-3, 3)
        direction_y = random.randint(-3, 3)
        particle_circle = [[x_pos, y_pos], circle_size, direction_x, direction_y]
        self.particles.append(particle_circle)

    def delete_particles(self):
        self.particles = [particle for particle in self.particles if particle[1] > 0] # delete particles when it smaler than 0


WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

particle1 = Particle()

PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT, 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == PARTICLE_EVENT:
            particle1.add_particles()
    
    screen.fill((100, 100, 100))
    particle1.emit([0, random.randint(0, 255), 0])
    pygame.display.flip()
    clock.tick(30)
