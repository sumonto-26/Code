import pygame 
from pygame.locals import*

# Made in 20 June 2023 by Sumonto

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic_Tac_Toe')


# define variables
line_width = 20
markers = []
clicked = False 
pos = []
player = 1
winner = 0 
game_over = False


# define colors
green = [0,255,0]
red = [ 255,0,0]
blue = [0, 0, 255 ]
black = [ 0, 0, 0]
white = (255, 255, 255)

# define font
font = pygame.font.SysFont (None, 80)

# create play again rectangle
again_rect = Rect(screen_width // 2 - 160, screen_height // 2 + 10 , 320, 100)

def draw_grid():
    background = [0,255, 255]
    grid = [ 0, 0, 0]
    
    screen.fill (background)
    for i in range(1, 3):
        pygame.draw.line(screen, grid, (0, i * 200), (screen_width, i * 200) , line_width)
        pygame.draw.line(screen, grid, (i * 200, 0), (i * 200, screen_height) , line_width)
  
for i in range(3):
    row = [ 0 ] * 3 
    markers.append(row)
      
def draw_markers():
    i_pos = 0
    for i in markers:
        j_pos = 0
        for j in i :
            if j == 1:
                pygame.draw.line(screen, (0, 0, 255), (i_pos * 200 + 30, j_pos * 200 + 30), (i_pos * 200 + 170, j_pos * 200 + 170), 35)
                pygame.draw.line(screen, (0, 0, 255), (i_pos * 200 + 30, j_pos * 200 + 170), (i_pos * 200 + 170, j_pos * 200 + 30), 35)
            if j == -1:
                pygame.draw.circle(screen,red, (i_pos * 200 + 100, j_pos * 200 + 100), 76, 25)
            j_pos += 1
        i_pos += 1
 
 
def check_winner():
    
    global winner
    global game_over
    
    j_pos = 0
    for i in markers:
        # check colums
        if sum (i) == 3:
            winner = 1
            game_over = True

        if sum (i) == -3:
            winner = 2
            game_over = True   
        # check rows
        if markers[0][j_pos] + markers[1][j_pos] + markers[2][j_pos] == 3:
            winner = 1
            game_over= True
        
        if markers[0][j_pos] + markers[1][j_pos] + markers[2][j_pos] == -3:
            winner = 2
            game_over= True
            
        j_pos += 1
        
        
        # check cross
        if markers[0][0] + markers[1][1] + markers [2][2] == 3 or markers[2][0] + markers[1][1] + markers [0][2] == 3 :
            winner = 1
            game_over = True
            
        if markers[0][0] + markers[1][1] + markers [2][2] == -3 or markers[2][0] + markers[1][1] + markers [0][2] == -3 :
            winner = 2
            game_over = True
            
            
            
def draw_winner(winner):
    if winner == 1:
        win_text = 'PLAYER ' + 'X' + " WIN!"
        win_img = font.render(win_text, True, white)
        pygame.draw.rect(screen, (0, 0, 255 ), (screen_width // 2 - 200, screen_height // 2 - 85, 450, 90))
        screen.blit(win_img, (screen_width // 2 - 200 , screen_height // 2 - 70 ))   
         
    elif winner == 2:
        win_text = 'PLAYER ' + 'O' + " WIN!"
        win_img = font.render(win_text, True, white)
        pygame.draw.rect(screen, (255, 0, 0 ), (screen_width // 2 - 200, screen_height // 2 - 85, 450, 90))
        screen.blit(win_img, (screen_width // 2 - 200 , screen_height // 2 - 70 ))      
    

             
        
    again_text = 'Play Again?'
    again_img = font.render(again_text, True, white)
    pygame.draw.rect(screen, (50 , 50 , 50), again_rect )
    screen.blit(again_img, (screen_width // 2 - 160, screen_height // 2 + 20 ))
    
 
runing = True
while runing == True:
    
    draw_grid()
    draw_markers()
    
    # add event handlers 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if game_over == 0 :
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
                
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 200][cell_y // 200] == 0 :
                    markers[cell_x // 200][cell_y // 200] = player
                    player *= -1
                    check_winner()
      
    if game_over == True:
        draw_winner(winner)
        # check for mouseclick to use if user has clicked on Play Again
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked  == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                
                # reset variables
                markers = []
                pos = []
                player = 1
                winner = 0 
                game_over = False               
                for i in range(3):
                    row = [ 0 ] * 3 
                    markers.append(row)             
                
                
    pygame.display.update()
            
pygame.quit()
quit()