import pygame
import sys

class Player (pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animaiting = False
        self.sprites.append(pygame.image.load("Python/2023/October/1/1.png"))
        self.sprites.append(pygame.image.load("Python/2023/October/1/2.png"))
        self.sprites.append(pygame.image.load("Python/2023/October/1/3.png"))
        self.sprites.append(pygame.image.load("Python/2023/October/1/4.png"))
        self.sprites.append(pygame.image.load("Python/2023/October/1/5.png"))
        self.sprites.append(pygame.image.load("Python/2023/October/1/6.png"))
        self.sprites.append(pygame.image.load("Python/2023/October/1/7.png"))
        self.sprites.append(pygame.image.load("Python/2023/October/1/8.png"))
        self.current_sprite = 0 
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        
    def animate(self):
        self.is_animaiting = True
        
    def update(self, speed):
        if self.is_animaiting == True:
            self.current_sprite += speed
            
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            if event.type == pygame.KEYUP:
                self.is_animaiting = False
            
            self.image = self.sprites[int(self.current_sprite)]

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 600
screen_height = 400
screen = pygame. display.set_mode((screen_width, screen_height))
pygame.display.set_caption("It's Fun!")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(230,30)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            player.animate()
            
      
            
    # Drawing
    screen. fill ((50,0,50))
    moving_sprites.draw(screen)
    moving_sprites.update(0.1)
    pygame.display.flip()
    clock.tick(60)
    
        
