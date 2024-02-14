import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y , player_score, opponent_score, score_time
    
    ball.x += ball_speed_x 
    ball.y += ball_speed_y
            
    # Vertical or y axis
    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1
         
         
    # Horizontal or x axis
    if ball.left <= 0 :
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()
        
    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound)
        opponent_score += 1
        score_time = pygame.time.get_ticks()
        
         
    # for player and opponent box are like boundary
    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
            
        elif abs (ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
              
        elif abs (ball.top - player.bottom) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
              
    if ball.colliderect(opponent) and ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        
        elif abs (ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
              
        elif abs (ball.top - opponent.bottom) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        
def player_animation():
    
    # WE MAKE BOUNDARY
    player.y += player_speed
    if player.top <= 0 :
        player. top = 0
    if player. bottom >= screen_height:
        player. bottom = screen_height
    
def opponent_ai():
    
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y :
        opponent.bottom -= opponent_speed
        
    if opponent.top <= 0 :
        opponent. top = 0
    if opponent. bottom >= screen_height:
        opponent. bottom = screen_height
        
def ball_start() :
    global ball_speed_x, ball_speed_y, score_time
    
    current_time = pygame.time.get_ticks ()
    ball.center = (screen_width/ 2 , screen_height/ 2)
    
    if current_time - score_time < 700:
        number_three = game_font.render("3", False, light_grey)
        screen.blit(number_three,(screen_width / 2 - 10, screen_height / 2 + 20))
    
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2", False, light_grey)
        screen.blit(number_two,(screen_width / 2 - 10, screen_height / 2 + 20))
    
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1 Go!", False, light_grey)
        screen.blit(number_one,(screen_width / 2 - 50, screen_height / 2 + 20))
    
    
    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
        
    else:
        ball_speed_y = 7 * random.choice((1 , - 1))
        ball_speed_x = 7 * random.choice((1 , - 1))
        score_time = None
        
    
# General setup   
pygame.mixer.pre_init(44100, -16, 2, 512) 
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ping Pong')

# Game Rectagnles
ball = pygame.Rect(screen_width / 2 - 15 , screen_height / 2 - 50, 30, 30)
player = pygame.Rect(screen_width - 20 , screen_height / 2 - 70, 15, 140)
opponent = pygame.Rect(10 ,screen_height/ 2 - 70, 15, 140)

# color making
background_color = pygame.Color('grey12')
light_grey = [200,200,200]

# All speed variables
ball_speed_x = 7 * random.choice((1 , -1))
ball_speed_y = 7 * random.choice((1 , -1))
player_speed = 0
opponent_speed = 7


# Text variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font('freesansbold.ttf', 64)
game_font2 = pygame.font.Font('freesansbold.ttf', 164)

# score timer
score_time = True

# Sound
pong_sound = pygame.mixer.Sound('2023/6. June/Ping Pong Game Music/pong.ogg')
score_sound = pygame.mixer.Sound('2023/6. June/Ping Pong Game Music/score.ogg')


while True:
    # Handling input 
    for event in pygame .event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
            
    # Game logic
    ball_animation()
    player_animation()
    opponent_ai()
            
    # Visuals
    screen.fill(background_color)
    pygame.draw.rect(screen, pygame.Color('cyan'), player)
    pygame.draw.rect(screen, pygame.Color('red'), opponent)
    pygame.draw.aaline(screen,(255, 0, 0), (screen_width/2, 0), (screen_width / 2, screen_height ))
    
    pygame.draw.ellipse(screen, pygame.Color('orange'), ball)
        
    if score_time:
        ball_start()
    

    player_text = game_font.render(f'{player_score}', False, pygame.Color ('cyan'))
    screen.blit(player_text, (1115, 30))
        
    opponent_text = game_font.render(f'{opponent_score}', False, pygame.Color('red'))
    screen.blit(opponent_text, (30, 30))
    
    
    # I made those lines
    # if player blues score 10 player blue win
    if player_score == 10:
        gameover = 'BLUE WIN'
        gameover_text = game_font2.render(f'{gameover}', False, pygame.Color('cyan'), )
        screen.blit(gameover_text,(170, 300))
        ball_speed_x = 0
        ball_speed_y = 0  
        
    # if player reds score 10 player red win
    elif opponent_score == 10:
        gameover2 = 'RED WIN'
        gameover_text2 = game_font2.render(f'{gameover2}', False, pygame.Color('red'), )
        screen.blit(gameover_text2,(250, 300))
        ball_speed_x = 0
        ball_speed_y = 0
        
        
    # Updating the window
    pygame.display.flip()
    clock.tick(60)
    
    
pygame.QUIT()
quit()
