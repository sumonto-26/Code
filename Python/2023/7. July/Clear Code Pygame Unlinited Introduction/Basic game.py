import pygame
import random
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        player_walk_11 = pygame.image.load('2023/7. July/Clear Code Pygame Unlinited Introduction/photos/player walk 1.png').convert_alpha()
        player_walk_21 = pygame.image.load('2023/7. July/Clear Code Pygame Unlinited Introduction/photos/player walk 2.png').convert_alpha()
        
        player_walk_1 = pygame.transform.rotozoom(player_walk_11, 0, 0.06) # 1 name # 2 angle and 3 how big
        player_walk_2 = pygame.transform.rotozoom(player_walk_21, 0, 0.06) 
        
        self.player_walk = [player_walk_1 , player_walk_2]
        self.player_index = 0
        self.player_jump1 = pygame.image.load('2023/7. July/Clear Code Pygame Unlinited Introduction/photos/player jump.png').convert_alpha()
        self.player_jump = pygame.transform.rotozoom(self.player_jump1, 0, 0.06) 
        
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (200 , 450))
        self.gravity = 0
        
        self.jump_sound = pygame.mixer.Sound('2023/7. July/Clear Code Pygame Unlinited Introduction/photos/audio_jump (1).mp3')
        

    def player_input(self):
        keys  = pygame.key.get_pressed()
        if keys [pygame.K_UP] and self.rect.bottom >= 450:
            self.gravity = -20
            self.jump_sound.play()
            self.jump_sound.set_volume(0.5)

    def apply_grabity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 450:
            self.rect.bottom = 450
            
    def animation_state (self):
        if self.rect.bottom < 270:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
            
    def update (self):
        self.player_input()
        self.apply_grabity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        
        if type == 'fly':
            fly_1 = pygame.image.load('2023/7. July/Clear Code Pygame Unlinited Introduction/photos/Fly1.png').convert_alpha()
            fly_2 = pygame.image.load('2023/7. July/Clear Code Pygame Unlinited Introduction/photos/Fly2.png').convert_alpha()
            self.frames = [fly_1 , fly_2] 
            y_pos = 330
            
        else:
            snail_1 = pygame.image.load('2023/7. July/Clear Code Pygame Unlinited Introduction/photos/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('2023/7. July/Clear Code Pygame Unlinited Introduction/photos/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 450
            
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint( 1100, 1200), y_pos))
            
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 5
        self.destroy()
        
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

def display_score():
    
    current_time = int(pygame.time.get_ticks() / 1500) - start_time
    score_surface = text_font1.render(f'SCORE: {current_time}', True,(200, 200, 200))
    score_rect = score_surface.get_rect(center = (120,50))
    
    score_box = pygame.draw.rect(screen,((65, 65, 65)), score_rect,60)
    screen.blit(score_surface, score_rect)
    return current_time
  
def collision_sprite():
    if pygame.sprite.spritecollide( player.sprite ,obstacle_group, False ):
        obstacle_group.empty()
        return False
    
    else:   return True
    

pygame.init()

screen_width = 1000
screen_height = 620

screen = pygame.display.set_mode(( screen_width, screen_height ))
pygame.display.set_caption('Clear Code pygame ultimate introduction to pygame')
clock = pygame.time.Clock()

text_font1 = pygame.font.SysFont(None , 50)
text_font2 = pygame.font.SysFont(None , 80)
text_font3 = pygame.font.SysFont('Constantia' , 65)

game_active = False
start_time = 0
score = 0

# background music
bg_music = pygame.mixer.Sound ('2023/7. July/Clear Code Pygame Unlinited Introduction/photos/music (1).wav')
bg_music.play(loops = -1)
bg_music.set_volume(0.2)


# Group
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('2023/7. July/Clear Code Pygame Unlinited Introduction/photos/Background.png').convert_alpha()
ground_surface = pygame.image.load('2023/7. July/Clear Code Pygame Unlinited Introduction/photos/Ground.png').convert_alpha() 

sky_surface = pygame.transform.rotozoom(sky_surface, 0, 0.28) 
ground_surface = pygame.transform.rotozoom(ground_surface, 0, 0.25) 

# Snail
snail_frame_1 = pygame.image.load('2023/7. July/Clear Code Pygame Unlinited Introduction/photos/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('2023/7. July/Clear Code Pygame Unlinited Introduction/photos/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0 
snail_surface = snail_frames[snail_frame_index]

# snail_rect = snail_surface.get_rect(topleft = (600 , 270))

# fly
fly_frame_1 = pygame.image.load('2023/7. July/Clear Code Pygame Unlinited Introduction/photos/Fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('2023/7. July/Clear Code Pygame Unlinited Introduction/photos/Fly2.png').convert_alpha()
fly_frames = [fly_frame_1 , fly_frame_2] 
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

obstacle_rect_list = []

player_walk_1 = pygame.image.load('2023/7. July/Clear Code Pygame Unlinited Introduction/photos/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('2023/7. July/Clear Code Pygame Unlinited Introduction/photos/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1 , player_walk_2]
player_index = 0
player_jump = pygame.image.load('2023/7. July/Clear Code Pygame Unlinited Introduction/photos/player jump.png').convert_alpha()

player_surface = player_walk [player_index]

player_rect  = player_surface.get_rect(topleft = (200, 220))
player_gravity = 0

player_stand = pygame.image.load("2023/7. July/Clear Code Pygame Unlinited Introduction/photos/player walk 1.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 0.22) # 1 name # 2 angle and 3 how big
player_stand_rect = player_stand.get_rect(center = (250, 300))

game_name = text_font2.render('Sumontos game' , True , (0, 255, 200), 10 )
game_name_rect = game_name.get_rect(center = (650, 150))

game_message = text_font1. render("Press up arrow button to start", True, (200 , 200 , 200), )
game_message_rect = game_message.get_rect(center = (500 , 550))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer , 1700)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer , 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer , 200)

# making gaming loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if player_rect.bottom >= 450: # for if our player stand on ground then only jump then
                        player_gravity = -20
                         
        else:
            if event.type == pygame.KEYDOWN and event. key == pygame.K_UP:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1500)
        
        if game_active:        
            if event.type == obstacle_timer  :
                obstacle_group.add(Obstacle(random.choice(['fly', 'snail'])))

            # making snail and fly animation
            if event.type == snail_animation_timer:
                
                if snail_frame_index == 0 : 
                    snail_frame_index = 1
                else: 
                    snail_frame_index = 0
                    
                snail_surface = snail_frames[snail_frame_index]
            
            if event.type == fly_animation_timer:
                if fly_frame_index == 0 : 
                    fly_frame_index = 1
                    
                else: 
                    fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]
            
            
    if game_active:
        
        screen.blit(sky_surface,(-150,-50))
        screen.blit( ground_surface,(0,450))
        
        score = display_score ()
        
        player.draw(screen)
        player.update()
        
        obstacle_group.draw(screen)
        obstacle_group.update()
            
        game_active = collision_sprite()

        
    else:
        screen.fill((100, 100, 100))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 450)
        player_gravity = 0
        
        score_message = text_font3.render(f'YOUR SCORE: {score}', True, (0 , 0 , 0) )
        score_message_rect = score_message.get_rect(center = (650, 300))
        screen.blit(score_message , score_message_rect)
        
        screen.blit(game_name, game_name_rect)
        screen.blit(game_message , game_message_rect)
        
        if score == 0 :    
            screen.blit(game_message , game_message_rect)
            
        else:   
            screen.blit(score_message, score_message_rect)
            
    
    def commands ():
    
        # make user input 1 event loop and 2 pygame.key
        # keys = pygame.key.get_pressed()
        # if keys [pygame.K_UP]:
        #     print('jump')
            
            
        # To make collisions to player rect and snailrect macth to make gameover
        # if (player_rect.colliderect(snail_rect)) :
        #     print('True')
        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
        #     print (pygame.mouse.get_pressed())
        
        # Make rectangle
        # variable = pygame.Rect(left,top,width,height)
        
        # making font
        # variable = pygame.font.SysFont or Font(font_type  , font size)
        
        # blit 4 image and 1 text
        # screen . blit ([image, font, text_name] , ( x , y) )
            
        # screen.blit(snail_surface , snail_rect)
        # screen.blit(score_surface , score_rect )
        
        # # make snail return back
        # snail_rect.x -= 7
        # if snail_rect.x < -100:
        #     snail_rect.x = screen_width
        
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if player_rect.collidepoint(event.pos):
        #         if player_rect.bottom >= 450: # for if our player stand on ground then only jump then
        #             player_gravity = -23
            
        # variable = font_name . render (text , Anti-Aliase [True or False] , Color )  
        # score_surface = text_font1.render ("Runner game" , True, ((0, 64, 60)) )
 
 
        # to load image
        # variable = pygame. image. load ('image_name').convert_alpha() [ convert_alpha for make those image better]

        # if random.randint(0,2):
        #     obstacle_rect_list.append(snail_surface.get_rect(topleft = (random.randint(900, 1100)  , 270)))
        # else:
        #     obstacle_rect_list.append(fly_surface.get_rect(topleft = (random.randint(900, 1100)  , 180)))
        

        # obstacle movement
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        # collision
        # game_active = collisions(player_rect, obstacle_rect_list)


        # player_gravity += 1
        # player_rect.y += player_gravity
        # we make our ground like boundary
        # if player_rect.bottom >= 450 :
            # player_rect.bottom = 450
        # player_animation()
        # screen.blit(player_surface , player_rect)
        
                
        # def obstacle_movement (obstacle_list):
        #     if obstacle_list:
        #         for obstacle_rect in obstacle_list:
        #             obstacle_rect.x -= 5
                    
        #             if obstacle_rect.bottom >= 450:
        #                 screen.blit(snail_surface, obstacle_rect)
        #             else:
        #                 screen.blit(fly_surface, obstacle_rect)
                    
        #         obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
                    
        #         return obstacle_list
        #     else:
        #         return []
        
        # def collisions(player, obstacles):
        #     if obstacles :
        #         for obstacle_rect in obstacles:
        #             if player.colliderect(obstacle_rect): return False
        #     return True
            
        # def player_animation():
        #     global player_surface , player_index
            
        #     if player_rect.bottom < 450:
        #         player_surface = player_jump
        #     else:
        #         player_index += 0.1
        #         if player_index >= len (player_walk): player_index = 0
        #         player_surface = player_walk[int(player_index)]
        # player_stand = pygame.transform.scale2x(player_stand) for double size

        pass
        
    pygame.display.update()
    clock.tick(60)