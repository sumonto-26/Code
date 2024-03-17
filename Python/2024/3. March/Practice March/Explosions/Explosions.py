import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
default_speed = 150  # milliseconds between frames

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Explosion Animation")

background_color = (102, 102, 102)

# Load explosion frames with background removal
explosion_frames = []
for i in range(1, 7):
    file_path = f"Code/Python/2024/3. March/Practice March/Explosions/Explosions ({i}).jpg"
    frame = pygame.image.load(file_path).convert()  # Load the image
    explosion_frames.append(frame)

# Scale frames to fit the screen
explosion_frames = [pygame.transform.scale(frame, (150, 150)) for frame in explosion_frames]

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = explosion_frames[0]
        self.rect = self.image.get_rect(center=(x, y))
        self.frame_index = 0
        self.last_frame_update = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_update > default_speed:
            self.frame_index += 1
            if self.frame_index < len(explosion_frames):
                self.image = explosion_frames[self.frame_index]
            else:
                self.kill()
            self.last_frame_update = current_time

all_sprites = pygame.sprite.Group()

speed = default_speed
run = True
while run:
    clock.tick(30)  # Cap the frame rate at 30 FPS

    all_sprites.update()
    screen.fill(background_color)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Create an instance of Explosion at the mouse position
            explosion = Explosion(*pygame.mouse.get_pos())
            all_sprites.add(explosion)
        elif event.type == pygame.KEYDOWN:
            # Adjust animation speed with arrow keys
            if event.key == pygame.K_UP:
                speed -= 50
            elif event.key == pygame.K_DOWN:
                speed = max(50, speed + 50)

    # Draw all sprites
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
quit()
