import pygame
import random
import math
from pygame import mixer

# start pygame and mixer module
mixer.init()
pygame.init()

clock = pygame.time.Clock()

# to make our background music
mixer.music.load('2023/6. June/icon_picture/background (1).wav')
# to set out background music and it play countineu
mixer.music.play(-1)


# making display
screen = pygame.display.set_mode((900, 600))


# Make a title
pygame.display.set_caption("Space Shooter Game")
icon = pygame.image.load('2023/6. June/icon_picture/space game.png')
pygame.display.set_icon(icon)

# Load background image
background = pygame.image.load('2023/6. June/icon_picture/space background.jpg')

# Our spaceship image
spaceshipimg = pygame.image.load('2023/6. June/icon_picture/spaceship (1).png')

enemyimg = []
enemyX = []
enemyY = []
enemyspeedX = []
enemyspeedY = []

num_of_enemys = 5

for i in range (num_of_enemys):

    # Load our enemy image
    enemyimg.append(pygame.image.load('2023/6. June/icon_picture/ufo.png'))

    # To make random position for our enemy
    enemyX.append(random.randint(0,835))
    enemyY.append(random.randint(30,150))

    # make 2 variable to enemy movement
    enemyspeedX.append(1)
    enemyspeedY.append(40)

score = 0

#load our bullet img
bulletimg = pygame.image.load('2023/6. June/icon_picture/startup.png')
check = False
bulletX = 466
bulletY = 490

# to make our spaceship x axies and y axies
spaceshipX = 450
spaceshipY = 480
changeX = 0

# Use gaming loop
running = True

# To make Score font
font = pygame.font.SysFont('Arial',32,'bold')


# to make our score in our screen
def score_text():
    img = font.render(f'Your Score : {score}', True, pygame.Color('white'))
    screen.blit(img, (10,10))
    
# game over font making
font_gameover = pygame.font.SysFont('Arial',100,'bold')
    
def gameover():
    img_gameover = font_gameover.render('GAME OVER', True , pygame.Color('white'))
    screen.blit(img_gameover, (180, 150))

while running:
    # to set our background
    screen.blit(background,(0 , 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #For movement our spaceship
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX =-5
            if event.key == pygame.K_RIGHT:
                changeX = 5    
                
            if event.key == pygame.K_UP:
                if check is False:
                    
                    # When we preace up key this music play
                    Bullet_Sound = mixer.Sound("2023/6. June/icon_picture/laser.wav")
                    Bullet_Sound.play ()
                    
                    check = True
                    bulletX = spaceshipX + 16 # to shot our bullet on spaceship's tip
            
        # if we relese the key it not break to break this spaceship we type this 2 line
        if event.type == pygame.KEYUP:
            changeX = 0
                         
    spaceshipX += changeX #spaceshipX = spaceshipX - changeX
    
    # Make boundary left side
    if spaceshipX <= 0:
        spaceshipX = 0
    # Right side
    elif spaceshipX >=836:
        spaceshipX = 836
    
    
    for i in range(num_of_enemys):
        
        if enemyY[i] >350:
            for j in range (num_of_enemys):
                enemyY[i] = 2000
            gameover()
            break
        
        enemyX[i] += enemyspeedX[i]
        # To make enemy movement
        if enemyX[i] <= 0:
            enemyspeedX[i] = 1
            enemyY[i] += enemyspeedY[i]
        if enemyX[i] >= 835:
            enemyspeedX[i] =- 1
            enemyY[i] += enemyspeedY[i]
            
          
        # make distance formula 
        distance = math.sqrt(math.pow( bulletX - enemyX[i], 2 ) + math.pow( bulletY - enemyY[i], 2 ))
        if distance <35 :
            Blast_Sound = mixer.Sound('2023/6. June/icon_picture/explosion.wav')
            Blast_Sound.play()
            
            bulletY = 480
            check = False
            enemyX[i] = random.randint(0,835)
            enemyY[i] = random.randint(30,150)
            score += 1
            
                
        screen.blit(enemyimg[i], (enemyX[i], enemyY[i]))
    
    if bulletY <=0:
        bulletY = 490
        check = False
        
    if check is True:
        screen.blit(bulletimg, (bulletX, bulletY))
        # bullet speed
        bulletY -= 4
        

    # For controle speed
    clock.tick(200)
    
    screen.blit(spaceshipimg, (spaceshipX, spaceshipY))

    # Call score_text function 
    score_text()
        
    # update display
    pygame.display.update()
    
pygame.QUIT()
QUIT()