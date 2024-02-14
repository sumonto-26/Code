import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = [pygame.transform.scale(pygame.image.load(f"Python/2024/1. January/Practice January/animation-master/attack_{i}.png"),
        [700, 500]) for i in range(1, 11)]
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.is_animating = False
        self.speed = 0.3

    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating:
            self.current_sprite += self.speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]

pygame.init()
clock = pygame.time.Clock()

WIDTH = 850
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100, 0)
moving_sprites.add(player)

run = True
while run:
    clock.tick(30)  # fps

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            player.animate()

    screen.fill([140, 130, 150])
    pygame.draw.line(screen, [0, 0, 0], (0, 500), (WIDTH, 500), 20)
    pygame.draw.rect(screen, [100, 200, 100], (0, 500, WIDTH, 100))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()

pygame.quit()
quit()
