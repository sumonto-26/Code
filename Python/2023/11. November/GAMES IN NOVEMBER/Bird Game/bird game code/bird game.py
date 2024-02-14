import pygame
import sys

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
PLAYER_WIDTH = 96
PLAYER_HEIGHT = 170
ROCK_WIDTH = 40
ROCK_HEIGHT = 40
PLAYER_SPEED = 15
ROCK_SPEED = 10
BIRD_FALL_SPEED = 1

class BirdGame:
    def __init__(self):
        pygame.init()

        # Screen setup
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Bad Bird Brawl")

        # Load images
        self.load_images()

        # Player setup
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT - SCREEN_HEIGHT // 3

        # Objects setup
        self.rocks = []
        self.birds = [Bird(70, 28, 5), Bird(440, 122, 5), Bird(840, 222, 5), Bird(350, 322, 5)]
        self.weres = [Were(-20, 300), Were(-20, 106), Were(-20, 200), Were(-20, 400)]

        # Flag to start the game
        self.game_started = False

        # Initialize the rock_on_screen variable
        self.rock_on_screen = False

    def load_images(self):
        self.background = pygame.image.load("Bird Game/img/bg.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.were_img = pygame.image.load("Bird Game/img/were.png").convert_alpha()
        self.were_img = pygame.transform.scale(self.were_img, (SCREEN_WIDTH - 60, 60))

        self.player_img_big = pygame.image.load("Bird Game/img/bird game project...png").convert_alpha()
        self.player_img = pygame.transform.scale(self.player_img_big, (PLAYER_WIDTH, PLAYER_HEIGHT))

        self.rock_img_big = pygame.image.load("Bird Game/img/bird game project 1.png").convert_alpha()
        self.rock_img = pygame.transform.scale(self.rock_img_big, (ROCK_WIDTH, ROCK_HEIGHT))

        self.bird_img_big = pygame.image.load("Bird Game/img/bird1.png").convert_alpha()
        self.bird_img = pygame.transform.scale(self.bird_img_big, (60, 100))

        # Create a variable to keep track of the cooldown for throwing rocks
        self.rock_cooldown = 0
        self.rock_on_screen = False  # Track if a rock is on the screen 

        # Player setup
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT - SCREEN_HEIGHT // 3

        # Objects setup
        self.rocks = []
        self.birds = [Bird(70, 28, 5), Bird(440, 122, 5), Bird(840, 222, 5), Bird(350, 322, 5)]
        self.weres = [Were(-20, 300), Were(-20, 106), Were(-20, 200), Were(-20, 400)]

        # Flag to start the game
        self.game_started = False


    def show_title_screen(self):
        title_screen_big = pygame.image.load("Bird Game/img/homepage.png").convert()
        title_screen = pygame.transform.scale(title_screen_big, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.screen.blit(title_screen, (0, 0))

        # Draw a "Start" button
        font = pygame.font.SysFont("Comic Sans MS", 50)
        start_button = font.render("Start", True, (0, 0, 50))
        start_button_rect = start_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
        self.screen.blit(start_button, start_button_rect)

        pygame.display.update()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN :
                    # Check if the mouse click is inside the "Start" button
                    if start_button_rect.collidepoint(event.pos):
                        waiting = False
                        self.game_started = True

                    

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()

        if self.game_started:
            if keys[pygame.K_LEFT]:
                self.player_x -= PLAYER_SPEED
            if keys[pygame.K_RIGHT]:
                self.player_x += PLAYER_SPEED

            if keys[pygame.K_UP] and self.rock_cooldown <= 0 and not self.rock_on_screen:
                for bird in self.birds:
                    
                    if not bird.hit:
                        new_rock = Rock(self.player_x, self.player_y)
                        self.rocks.append(new_rock)
                        # Set a cooldown (in frames) before another rock can be thrown
                        self.rock_cooldown = 10  # Adjust this value to change the cooldown duration
                        self.rock_on_screen = True
        return True

    def update_game(self):
        self.player_x = max(50, min(self.player_x, SCREEN_WIDTH - PLAYER_WIDTH - 85))

        for bird in self.birds:
            if bird.hit:
                bird.y -= BIRD_FALL_SPEED

            if not bird.hit:
                for rock in self.rocks:
                    if rock.y < 0:
                        self.rocks.remove(rock)
                        self.rock_on_screen = False  # Mark the rock as off the screen
                        
                    elif pygame.Rect(rock.x, rock.y, ROCK_WIDTH, ROCK_HEIGHT).colliderect(pygame.Rect(bird.x, bird.y, 60, 100)):
                        bird.hit = True
                        bird.y = -50 # Reset the bird's fall position
                        self.rock_on_screen = False  # Mark the rock as off the screen

        for rock in self.rocks:
            rock.move()

        # Decrement the rock cooldown timer
        self.rock_cooldown = max(0, self.rock_cooldown - 1)

    def draw_objects(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))

        if self.game_started:
            self.screen.blit(self.player_img, (self.player_x, self.player_y))

            for bird in self.birds:
                self.screen.blit(self.bird_img, (bird.x, bird.y))

            for rock in self.rocks:
                self.screen.blit(self.rock_img, (rock.x, rock.y))

            for were in self.weres:
                self.screen.blit(self.were_img, (were.x, were.y))

        pygame.display.update()

    def run(self):
        clock = pygame.time.Clock()
        run = True

        while run:
            run = self.handle_events()
            self.update_game()
            self.draw_objects()
            clock.tick(30)  # Limit frame rate to 30 FPS

        pygame.quit()

class Bird:
    def __init__(self, x, y, bird_speed):
        self.x = x
        self.hit = False
        self.y = y
        self.bird_speed = bird_speed

class Were:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rock:
    def __init__(self, x, y):
        self.x = x + 27
        self.y = y + 55

    def move(self):
        self.y -= ROCK_SPEED

if __name__ == "__main__":
    game = BirdGame()
    game.show_title_screen()  # Display the title screen
    game.run()  # Start the game loop after the player clicks the "Start" button
