import pygame 
import random
import math

pygame.init()

# Screen settings
WIDTH, HEIGHT = 1200, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Realistic Rocket Smoke")
clock = pygame.time.Clock()

# Load rocket image
ICON = pygame.image.load("Pygame/roket.png")
pygame.display.set_icon(ICON)

IMAGE_WIDTH, IMAGE_HEIGHT = 100, 100
ROCKET_IMAGE = pygame.transform.scale(ICON, (IMAGE_WIDTH, IMAGE_HEIGHT))

# Smoke types
SMOKE_TYPES = ['classic', 'dark', 'blue', 'fire']

class Rocket:
    def __init__(self, x, y):
        self.image = ROCKET_IMAGE
        self.x, self.y = x, y
        self.angle = 0
        self.velocity_x, self.velocity_y = 0, 0
        self.acceleration = 0.5
        self.friction = 0.02
        self.bounce_factor = 0.3
        self.follow_mouse = False
        self.smoke_active = False
    
    def rotate_center(self):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=(self.x + IMAGE_WIDTH // 2, self.y + IMAGE_HEIGHT // 2))
        return rotated_image, new_rect

    def move(self, keys, smoke_particles, smoke_type):
        cos_a, sin_a = math.cos(math.radians(self.angle + 90)), math.sin(math.radians(self.angle + 90))

        if self.smoke_active:
            smoke_particles.append(SmokeParticle(self.x, self.y, cos_a, sin_a, smoke_type))

        if keys[pygame.K_UP]:
            self.velocity_x += self.acceleration * cos_a
            self.velocity_y -= self.acceleration * sin_a
        
        elif keys[pygame.K_DOWN]:
            self.velocity_x -= self.acceleration * cos_a
            self.velocity_y += self.acceleration * sin_a

        self.angle += 5 * keys[pygame.K_LEFT] - 5 * keys[pygame.K_RIGHT]
        
        # Mouse following movement
        if self.follow_mouse:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dx, dy = mouse_x - self.x, mouse_y - self.y
            self.angle = math.degrees(math.atan2(-dy, dx)) - 90
            self.velocity_x, self.velocity_y = dx * 0.05, dy * 0.05
        
        self.velocity_x *= 1 - self.friction
        self.velocity_y *= 1 - self.friction
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Bounce on walls
        self.x = max(0, min(self.x, WIDTH - IMAGE_WIDTH))
        self.y = max(0, min(self.y, HEIGHT - IMAGE_HEIGHT))
        
        if self.x in [0, WIDTH - IMAGE_WIDTH]:
            self.velocity_x *= -self.bounce_factor
        if self.y in [0, HEIGHT - IMAGE_HEIGHT]:
            self.velocity_y *= -self.bounce_factor


class SmokeParticle:
    COLORS = {
        'classic': (150, 150, 150),
        'dark': (80, 80, 80),
        'blue': (random.randint(0,100), random.randint(0,100) , random.randint(200,250)),
        'fire': (random.randint(10,255), random.randint(50,100), 0)
    }
    
    def __init__(self, x, y, cos_a, sin_a, smoke_type):
        self.x = x + IMAGE_WIDTH // 2 - cos_a * 30
        self.y = y + IMAGE_HEIGHT // 2 + sin_a * 30
        self.size = random.randint(10, 30)
        self.alpha = 255
        self.color = self.COLORS.get(smoke_type, (150, 150, 150))
        self.velocity_x = random.uniform(-1, 1)
        self.velocity_y = random.uniform(-2, -0.5)
        self.rotation = random.uniform(-2, 2)
    
    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.size *= 0.98
        self.alpha -= 4
        return self.size > 0 and self.alpha > 0
    
    def draw(self, screen):
        if self.alpha > 0:
            surface = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
            pygame.draw.circle(surface, (*self.color, self.alpha), (self.size, self.size), self.size)
            screen.blit(surface, (self.x - self.size, self.y - self.size))


class Game:
    def __init__(self):
        self.rocket = Rocket(300, 100)
        self.smoke_particles = []
        self.smoke_type_index = 0  # Start with classic smoke
    
    def run(self):
        running = True
        while running:
            screen.fill((30, 30, 30))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.smoke_type_index = (self.smoke_type_index + 1) % len(SMOKE_TYPES)
                    elif event.key == pygame.K_m:  # Toggle mouse follow mode
                        self.rocket.follow_mouse = not self.rocket.follow_mouse
                    elif event.key == pygame.K_s:  # Toggle smoke
                        self.rocket.smoke_active = not self.rocket.smoke_active
            
            keys = pygame.key.get_pressed()
            self.rocket.move(keys, self.smoke_particles, SMOKE_TYPES[self.smoke_type_index])
            self.smoke_particles = [p for p in self.smoke_particles if p.update()]
            for particle in self.smoke_particles:
                particle.draw(screen)
            rotated_image, new_rect = self.rocket.rotate_center()
            screen.blit(rotated_image, new_rect.topleft)
            self.display_info()
            pygame.display.update()
            clock.tick(30)
        pygame.quit()
    
    def display_info(self):
        font = pygame.font.SysFont("Arial", 24)
        smoke_text = font.render(f"Smoke Type: {SMOKE_TYPES[self.smoke_type_index]}", True, (255, 255, 255))
        mode_text = font.render(f"Mode: {'Mouse' if self.rocket.follow_mouse else 'Keys'}", True, (255, 255, 255))
        screen.blit(smoke_text, (20, 20))
        screen.blit(mode_text, (20, 50))


if __name__ == "__main__":
    Game().run()
