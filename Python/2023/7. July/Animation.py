import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x , pos_y):
        super().__init__()
        self.is_animating = False
        self.sprites = []
        
        self.sprites.append(pygame.image.load('2023/7. July/photo/Frog animation/attack_1.png'))
        self.sprites.append(pygame.image.load('2023/7. July/photo/Frog animation/attack_2.png'))
        self.sprites.append(pygame.image.load('2023/7. July/photo/Frog animation/attack_3.png'))
        self.sprites.append(pygame.image.load('2023/7. July/photo/Frog animation/attack_4.png'))
        self.sprites.append(pygame.image.load('2023/7. July/photo/Frog animation/attack_5.png'))
        self.sprites.append(pygame.image.load('2023/7. July/photo/Frog animation/attack_6.png'))
        self.sprites.append(pygame.image.load('2023/7. July/photo/Frog animation/attack_7.png'))
        self.sprites.append(pygame.image.load('2023/7. July/photo/Frog animation/attack_8.png'))
        self.sprites.append(pygame.image.load('2023/7. July/photo/Frog animation/attack_9.png'))
        self.sprites.append(pygame.image.load('2023/7. July/photo/Frog animation/attack_10.png'))
        
        
        self.current_sprite = 0
        self.image = self.sprites [self.current_sprite]
        
        
        
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self. is_animating = True
        
        
    def update(self):
        
        speed = 0.2
        
        if self.is_animating == True:
            self.current_sprite += speed
            
            if int( self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            
            self.image = self.sprites[int (self.current_sprite)]

              
              
# General setup
pygame.init()
clock = pygame.time.Clock()

# Basic setup
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption('Animation')

# Creating the sprite and groups
moving_sprites = pygame.sprite.Group()
player = Player(250, 250)
moving_sprites.add (player)

while True:
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:   
            player.animate()

    # DRAWING
    screen.fill ('grey12')
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)