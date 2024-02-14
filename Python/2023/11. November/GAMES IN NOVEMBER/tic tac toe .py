import pygame, sys
import numpy

pygame.init()

# ----------
# CONSTANTS
# ----------

# For making our game background
Width = 750  
Height = Width
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = Width//BOARD_COLS
Line_width = Width//24

# for circle and cross  
CIRCLE_WIDTH = Width // 24
CIRCLE_SIZE = SQUARE_SIZE //3 
CROSS_WIDTH = Width // 20
CROSS_SIZE = SQUARE_SIZE//4.5

line_space_1 = Width // 11 # for asc and desc line
line_space_2 = Width // 27 # for horizontal and vertical line

# Colour's
BG_colour = (38,180,166)
CIRCLE_COLOUR = (239,231,220)
Line_colour = (0, 125, 115)
CROSS_COLOUR = (70,70,70)

screen = pygame.display .set_mode((Width, Height))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BG_colour)

# board
board = numpy.zeros( (BOARD_ROWS, BOARD_COLS) )

def draw_lines():
    
    # 1st horizontal line
    pygame.draw.line(screen, Line_colour, (line_space_2 ,SQUARE_SIZE), (Width - line_space_2 ,SQUARE_SIZE), Line_width)
    # 2nd horizontal line
    pygame.draw.line(screen, Line_colour, (line_space_2, 2 * SQUARE_SIZE), (Width - line_space_2, 2 * SQUARE_SIZE), Line_width)

    # 1st vertical line
    pygame.draw.line(screen, Line_colour, (SQUARE_SIZE, Height // 22), (SQUARE_SIZE,Height - Height // 22), Line_width)
    # 2nd vertical line
    pygame.draw.line(screen, Line_colour, (2 * SQUARE_SIZE, Height // 22), (2 * SQUARE_SIZE, Height - Height // 22), Line_width)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range (BOARD_COLS):
            if board[row][col] == 1 :
                pygame.draw.circle(screen, CIRCLE_COLOUR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int(row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_SIZE, CIRCLE_WIDTH)
            elif board[row][col]== 2:
                pygame.draw.line( screen, CROSS_COLOUR, (col * SQUARE_SIZE + CROSS_SIZE, row * SQUARE_SIZE + CROSS_SIZE), (col * SQUARE_SIZE + SQUARE_SIZE - CROSS_SIZE, row * SQUARE_SIZE + SQUARE_SIZE - CROSS_SIZE), CROSS_WIDTH )
                pygame.draw.line( screen, CROSS_COLOUR, (col * SQUARE_SIZE + CROSS_SIZE, row * SQUARE_SIZE + SQUARE_SIZE - CROSS_SIZE), (col * SQUARE_SIZE + SQUARE_SIZE - CROSS_SIZE, row * SQUARE_SIZE + CROSS_SIZE), CROSS_WIDTH )
                
def mark_square(row,col, player):
                board[row][col] = player 
    
def available_square(row, col):
    return board[row] [col] == 0
     
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row] [col] == 0:
                return False
    return True
    
def check_win (player):
    # vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
        
    # horizontal win check
    for row in range (BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board [row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
        
    # asc diagonal win check 
    if board [2][0] == player and board [1][1] == player and board [0][2] == player:
        draw_asc_diagonal(player)
        return True
    
    #  desc diagonal win chek
    if board[0][0] == player and board [1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True
    
    return False

def draw_vertical_winning_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE//2
    
    if player == 1:
        color = CIRCLE_COLOUR
    elif player == 2:
        color = CROSS_COLOUR
    
    pygame.draw.line ( screen, color, (posX,line_space_2 ), (posX, Height - line_space_2), Line_width)

def draw_horizontal_winning_line(row, player):
   
    posY = row * SQUARE_SIZE + SQUARE_SIZE//2
    
    if player == 1:
        color = CIRCLE_COLOUR
    elif player == 2:
        color = CROSS_COLOUR
    
    pygame.draw.line ( screen, color, (line_space_2, posY), (Width - line_space_2, posY), Line_width)

def draw_asc_diagonal(player): # / 
    if player == 1:
        color = CIRCLE_COLOUR
    elif player == 2:
        color = CROSS_COLOUR
        
    pygame.draw.line ( screen, color, (line_space_1, Height - line_space_1), (Width - line_space_1, line_space_1), Width // 20)

def draw_desc_diagonal(player): # \
    if player == 1:
        color = CIRCLE_COLOUR
    elif player == 2:
        color = CROSS_COLOUR
        
    pygame.draw.line ( screen, color, (line_space_1, line_space_1), (Width - line_space_1, Height - line_space_1), Width // 20)

def restart():
    screen.fill ( BG_colour )
    draw_lines()
    player = 1 
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

draw_lines()

player = 1
game_over = False

# Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            
            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y
            
            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if available_square( clicked_row, clicked_col ):
                mark_square(clicked_row, clicked_col, player)
                if check_win( player ):
                    game_over = True
                player = player % 2 + 1

                draw_figures ()
            
        # if I press space key then game restart
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                restart()
            game_over = False
                
    pygame.display.update()
     
     
        