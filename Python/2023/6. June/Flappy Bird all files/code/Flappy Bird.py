import pygame , sys , time
from settings import *
from sprites import BG , Ground , Plane , Obstacle


class Game:
    # make our first method 
    def __init__(self):
        
        # at first make setup
        pygame. init()
        self.screen = pygame.display.set_mode((window_width, window_height))
        pygame. display. set_caption(' PROJECT FLAPPY BIRD CLONE')
        self.clock = pygame.time.Clock()
        self.active = True
        
        # make sprite group
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprite = pygame.sprite.Group()
        
        # Scale factor
        bg_height = pygame.image.load('2023/6. June/Flappy Bird all files/background.png'). get_height()
        self.scale_factor = window_height /bg_height
        
        # Sprite setup
        BG(self.all_sprites, self.scale_factor)
        Ground([self.all_sprites,self.collision_sprite], self.scale_factor)
        self.plane = Plane(self.all_sprites, self.scale_factor / 1.6)
        
        # timer 
        self. obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1400)
        
        # text 
        self.font = pygame.font.Font('2023/6. June/Flappy Bird all files/BD_Cartoon_Shout.ttf',30)
        self.score = 0
        self.start_offset = 0
        
        # menu
        self.menu_surf = pygame.image.load('2023/6. June/Flappy Bird all files/menu.png').convert_alpha()
        self.menu_rect = self.menu_surf.get_rect(center = (window_width / 2 , window_height / 2))
        
        # background music
        self.music = pygame.mixer.Sound("2023/6. June/Flappy Bird all files/sound/sounds_music.wav")
        self.music.play(loops = -1)
        self.music.set_volume(0.3)
        
    def collisions(self):
        if pygame.sprite.spritecollide(self.plane,self.collision_sprite, False, pygame.sprite.collide_mask)\
            or self.plane.rect.top <= 0:
                for sprite in self.collision_sprite.sprites():
                    if sprite.sprite_type == 'obstacle' :
                        sprite.kill()
                self.active = False
                self.plane.kill()
        
    def display_score (self):
        if self.active:
            self.score = (pygame.time.get_ticks() - self.start_offset) // 1000
            x =  135
            y =  50
            
        else:
            x = window_width /2
            y = window_height / 2 + (self.menu_rect.height / 1.5)
        
        score_surf = self.font.render('score is: '+ str(self.score), True, pygame.Color('brown'))
        
        score_rect =  score_surf.get_rect(midtop = (x, y))
        self.screen.blit(score_surf,score_rect)
     
    # make another method 
    def run(self):
        last_time = time.time()
        # make gaming while loop in our run method
        while True:
            
            # Delta time
            delta_time = time.time() - last_time
            last_time = time.time()
            
            # make event for loop 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key == pygame.K_UP:
                            self.plane.jump()
                            
                    else:
                        self.plane = Plane(self.all_sprites, self.scale_factor / 1.6)
                        self.active = True
                        self.start_offset = pygame.time.get_ticks()
                        
                        
                if event.type == self.obstacle_timer and self.active:
                    Obstacle([self.all_sprites, self.collision_sprite], self.scale_factor * 0.9)
                    
            # Making Game Logic
            self.screen.fill("black")
            self.all_sprites.update(delta_time)
            self.collisions()
            self.all_sprites.draw(self.screen)
            self.display_score()
            
            if self.active: 
                self.collisions
                
            else:
                self.screen.blit(self.menu_surf, self.menu_rect)
            
            pygame.display.update()
            self.clock.tick(FRAMERATE)
            
if __name__ == '__main__':
    game = Game()
    game.run()
