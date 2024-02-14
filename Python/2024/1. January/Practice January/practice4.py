import pygame
import random
import math

pygame.init()

# Create the screen
WIDTH, HEIGHT = 900, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")

# Player Variable
player_x = WIDTH / 2
player_y = HEIGHT - 50
player_size = 30
player_speed = 0.4
player_color = [0, 155, 0]

# Enemy Variable
num_of_enemies = 5

enemy_size = []
enemy_x = []
enemy_y = []
enemy_speed_x = []
enemy_speed_y = []
enemy_color = []

# make multiple enemies
for _ in range(num_of_enemies):
    enemy_size.append(30)
    enemy_x.append(random.randint(0, WIDTH - enemy_size[-1]))
    enemy_y.append(random.randint(50, 270))
    enemy_speed_x.append(0.4)
    enemy_speed_y.append(70)
    enemy_color.append([random.randint(0,255), 0, 0])

# Bullet Variable
bullet_color = [0, 0, 50]
bullet_x = 0
bullet_y = player_y
bullet_size = 5
bullet_speed = 1
bullet_state = "ready"


# for score
score_value = 0
score_size = 25
font = pygame.font.Font("freesansbold.ttf", score_size)
text_x = 10
text_y = 10

# Game Over Text
game_over_text_size = WIDTH//10
Ofont = pygame.font.Font("freesansbold.ttf", game_over_text_size)


def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, [0,0,50])
    screen.blit(score, (x,y))

def game_over_text():
    over_text = Ofont.render("GAME OVER", True, (0,0,50))
    screen.blit(over_text, (WIDTH//5, HEIGHT // 2.4))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    pygame.draw.circle(screen, bullet_color, (x + player_size // 2, y), bullet_size)


# Check if bullet and enemy are collide
def isCollision(bullet_x, bullet_y, enemy_x, enemy_y, enemy_size):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2))) # Formula
    if distance <= enemy_size:
        return True
    else:
        return False

# Game Loop
run = True
while run:
    screen.fill((150, 150, 150))

    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))  # player

    for i in range(num_of_enemies):
        pygame.draw.rect(screen, enemy_color[i], (enemy_x[i], enemy_y[i], enemy_size[i], enemy_size[i]))  # enemy

        # collision
        collision = isCollision(bullet_x, bullet_y, enemy_x[i], enemy_y[i], enemy_size[i])
        if collision:
            bullet_y = player_y
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, WIDTH - enemy_size[i])
            enemy_y[i] = random.randint(50, 270)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # user input
    if event.type == pygame.KEYDOWN:
        # player movement
        if event.key == pygame.K_LEFT:
            player_x -= player_speed
        if event.key == pygame.K_RIGHT:
            player_x += player_speed
            
        if event.key == pygame.K_UP:
            if bullet_state == "ready":
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)

    # player Boundary
    if player_x >= WIDTH - player_size:
        player_x = 0
    elif player_x <= 0:
        player_x = WIDTH - player_size

    # Enemy Movement
    for i in range(num_of_enemies):
        
        # Game Over 
        if enemy_y[i] > 450:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            game_over_text()
            break 
        
        
        enemy_x[i] += enemy_speed_x[i]
        if enemy_x[i] <= 0:
            enemy_speed_x[i] = abs(enemy_speed_x[i])
            enemy_y[i] += enemy_speed_y[i]
        elif enemy_x[i] >= WIDTH - enemy_size[i]:
            enemy_speed_x[i] = -abs(enemy_speed_x[i])
            enemy_y[i] += enemy_speed_y[i]

    # for multiple bullets
    if bullet_y <= 0:
        bullet_y = player_y
        bullet_state = "ready"

    # For Bullet Movement
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_speed

    show_score(text_x, text_y)

    pygame.display.update()

pygame.quit()
quit()
