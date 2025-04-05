# Trigonometry Program Pygame
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pendulum Simulation using Trigonometry")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Pendulum parameters
pendulum_length = 250
angle = math.pi / 4  # Initial angle (45 degrees)
angular_velocity = 0
angular_acceleration = 0
gravity = 0.5
damping = 0.995  # To simulate air resistance

# Pivot point
pivot_x, pivot_y = WIDTH // 2, 100

# Clock
clock = pygame.time.Clock()

def draw_pendulum():
    # Calculate bob position using trigonometry
    bob_x = pivot_x + pendulum_length * math.sin(angle)
    bob_y = pivot_y + pendulum_length * math.cos(angle)

    # Draw pendulum
    pygame.draw.line(screen, BLACK, (pivot_x, pivot_y), (bob_x, bob_y), 4)
    pygame.draw.circle(screen, RED, (int(bob_x), int(bob_y)), 20)

def update_pendulum():
    global angle, angular_velocity, angular_acceleration

    # Calculate angular acceleration using gravity and sine of the angle
    angular_acceleration = (-gravity / pendulum_length) * math.sin(angle)

    # Update angular velocity and angle
    angular_velocity += angular_acceleration
    angular_velocity *= damping  # Apply damping
    angle += angular_velocity

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear screen
        screen.fill(WHITE)

        # Update and draw pendulum
        update_pendulum()
        draw_pendulum()

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()