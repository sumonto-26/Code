# 15 V I D E O finish !  
import pygame
import random
pygame.init()

# Making screen size
screen_width = 1000
screen_height = 700

# make a clock
fps = 30
clock = pygame.time.Clock()


# Make display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(" Code with harry pygame course")
pygame.display.update()

# color define
background_color = [50, 250, 200]
snake_color = [10, 100, 255]
fruit_color = [255, 0, 0]

# Define snake variables
snake_size_x = 25
snake_size_y = 25
snake_velocity_x = 0
snake_velocity_y = 0
snake_x = 500
snake_y = 350

# Define fruit variables
fruit_x = random.randint (25, screen_width-20)
fruit_y = random.randint (25, screen_height-20)
fruit_size_x = 20
fruit_size_y = 20

# Score variable
score = 0
init_velocity = 5
score_colour = [0, 0, 0]
score_x = 20
score_y = 20

# Make font variables
font_size = 40
font = pygame.font.SysFont('Constantia', font_size)

# make a function
def Score_text (text , colour, x , y):
    screen_text = font.render(text, True, colour )
    screen.blit(screen_text, [x, y])
    


# Creating a Game loop
exit_game = False

while exit_game == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True 
            
        # for making movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_velocity_x =+ init_velocity
                snake_velocity_y = 0
                
            if event.key == pygame.K_LEFT:
                snake_velocity_x =- init_velocity
                snake_velocity_y = 0
                
            if event.key == pygame.K_UP:
                snake_velocity_y =- init_velocity
                snake_velocity_x = 0
                
            if event.key == pygame.K_DOWN:
                snake_velocity_y =+ init_velocity
                snake_velocity_x = 0
                
    # if snake eat fruit it make random position 
    if abs(snake_x - fruit_x) <15 and abs(snake_y - fruit_y) <15:
        # increase score 
        score = score + 1
        fruit_x = random.randint (20, screen_width-20)
        fruit_y = random.randint (20, screen_height-20)
        
                
    # for make bundary 
    if snake_x < 0:
        snake_x = screen_width
    if snake_x > screen_width:
        snake_x = 0
        
    if snake_y < 0:
        snake_y = screen_height
    if snake_y > screen_height:
        snake_y = 0
                
    snake_x = snake_x + snake_velocity_x
    snake_y = snake_y + snake_velocity_y
    
                
    clock.tick(fps)
    screen.fill(background_color)  
    
    # Call Score_text
    Score_text("SCORE: " + str(score * 1), score_colour, score_x, score_y)
    
    # draw fruit 
    pygame.draw.rect (screen, fruit_color, [fruit_x, fruit_y, fruit_size_x, fruit_size_y])
    
    # draw snake head
    pygame.draw.rect (screen, snake_color, [snake_x, snake_y, snake_size_x, snake_size_y])   
    pygame.display.update()

pygame.quit()
quit()