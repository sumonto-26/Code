import pygame
import time 
import math 
import random
from utils import scale_image,blit_rotate_center, blit_text_center
pygame.font.init()


grass = scale_image (pygame.image.load('2024/1. January/Car game/imgs/grass.jpg'), 4)
finish = scale_image (pygame.image.load('2024/1. January/Car game/imgs/finish.png'), 1)
finish_position = (120, 250)
finish_mask = pygame.mask.from_surface(finish)


car = scale_image (pygame.image.load(f'2024/1. January/Car game/imgs/tank.png'), 0.09)
enemy_car = scale_image (pygame.image.load('2024/1. January/Car game/imgs/red_car.png'), 0.5)

track_border = scale_image (pygame.image.load('2024/1. January/Car game/imgs/track-border.png'),0.9)
track_border_mask = pygame.mask.from_surface(track_border)
track = scale_image (pygame.image.load('2024/1. January/Car game/imgs/track.png'), 0.9)

width,height = track.get_width(), track.get_height()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Racing game")


main_font1 = pygame.font.SysFont("comicsans", 25)
main_font2 = pygame.font.SysFont(None, 80)

path = [(175, 119), (110, 70), (56, 133), (70, 481), (318, 731), (404, 680), (418, 521), (507, 475), (600, 551), (613, 715), (736, 713),
(734, 399), (611, 357), (409, 343), (433, 257), (697, 258), (738, 123), (581, 71), (303, 78), (275, 377), (176, 388), (178, 260)]

class GameInfo:
    LEVELS = 5

    def __init__(self, level = 1):
        self.level = level
        self.started = False
        self.level_start_time = 0

    def next_level(self):
        self.level += 1
        self.started = False

    def reset(self):
        self.level = 1
        self.started = False
        self.level_start_time = 0

    def game_finished(self):
        return self.level > self.LEVELS

    def start_level(self):
        self.started = True
        self.level_start_time = time.time()

    def get_level_time(self):
        if not self.started:
            return
        return round(time.time() - self.level_start_time , 1)


class CarMovement:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.start_pos
        self.acceleration = 0.1

    def rotation(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel 
        elif right:
            self.angle -= self.rotation_vel 
            

    def draw(self,win):
        blit_rotate_center(win, self.img, (self.x,self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def collide (self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi

    def reset(self):
        self.x, self.y = self.start_pos
        self.angle = 0
        self.vel = 0

class PlayerCar(CarMovement):
    IMG = car
    start_pos = (140, 200)

    def reduce_speed(self):
        self.vel = max (self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
        self.vel = -self.vel*1.5
        self.move()

class ComputerCar(CarMovement):
    IMG = enemy_car
    start_pos = (190, 210)

    def __init__(self,max_vel, rotation_vel, path = []):
        super().__init__(max_vel, rotation_vel)
        self.path = path
        self.current_point = 0
        self.vel = max_vel
    
    def draw_points(self,win):
        for point in self.path:
            pygame.draw.circle(win,(255, 0, 0), point, 5)
        
    def draw(self,win):
        super().draw(win)
        # self.draw_points(win)

    def calulate_angle(self):
        target_x, target_y = self.path[self.current_point]
        x_diff = target_x - self.x
        y_diff = target_y - self.y

        if y_diff == 0:
            desired_radian_angle = math.pi / 2
        else:
            desired_radian_angle = math.atan(x_diff/y_diff)

        if target_y > self.y:
            desired_radian_angle += math.pi

        difference_in_angle = self.angle - math.degrees(desired_radian_angle)
        if difference_in_angle >= 180:
            difference_in_angle -= 360

        if difference_in_angle > 0:
            self.angle -= min(self.rotation_vel, abs(difference_in_angle))
        else:
            self.angle += min(self.rotation_vel, abs(difference_in_angle))

    def update_path_point(self):
        target = self.path[self.current_point]
        rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
        if rect.collidepoint(*target):
            self.current_point += 1

    def move(self):
        if self.current_point >= len(self.path):
            return

        self.calulate_angle()
        self.update_path_point()
        super().move()

    def next_level(self, level):
        self.reset()
        self.vel = self.max_vel + (level - 1) * 0.2
        self.current_point = 0

def draw(win, images, player_car, computer_car, game_info):
    for img, pos in images:
        win.blit(img, pos)

    level_text = main_font1.render(f"Level {game_info.level}", 1, (0, 0, 0))
    win.blit(level_text, (10, height - level_text.get_height() - 100))

    time_text = main_font1.render(f"Time {game_info.get_level_time()}s", 1, (0, 0, 0))
    win.blit(time_text, (10, height - time_text.get_height() - 70))


    vel_text = main_font1.render(f"Vel {round(player_car.vel, 2)}px/s", 1, (0, 0, 0))
    win.blit(vel_text, (10, height - vel_text.get_height() - 40))

    player_car.draw(win)
    computer_car.draw(win)
    pygame.display.update()

def move_player(player_car):    

    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_LEFT]:
        player_car.rotation(left= True)
    if keys[pygame.K_RIGHT]:
        player_car.rotation(right= True)
    if keys[pygame.K_DOWN]:
        moved = True
        player_car.move_backward()
    if keys[pygame.K_UP] :
        moved = True
        player_car.move_forward()
    # BOOST
    if keys[pygame.K_b] :
        moved = True
        player_car.move_forward()
        player_car.move_forward()

    if not moved:
        player_car.reduce_speed()

def handle_collision(player_car, computer_car, game_info):

    if player_car.collide(track_border_mask) != None:
        player_car.bounce()

    computer_finish_poi_collide = computer_car.collide(finish_mask, *finish_position)
    if computer_finish_poi_collide != None:
        blit_text_center(win, main_font2, "You lost!")
        pygame.display.update()
        pygame.time.wait(5000)
        game_info.reset()
        player_car.reset()
        computer_car.reset()

    player_finish_poi_collide = player_car.collide(finish_mask, *finish_position)
    if player_finish_poi_collide != None:
        if player_finish_poi_collide[1] == 0:
            player_car.bounce()
        else:
            game_info.next_level()
            player_car.reset()
            computer_car.next_level(game_info.level)

run = True 
clock = pygame.time.Clock()
images = [(grass,(0,0)),(track,(0,0)),
         (finish, finish_position), 
         (track_border, (0, 0))]

player_car = PlayerCar(5,5)
computer_car = ComputerCar(2,5, path)
game_info = GameInfo()

while run:
    clock.tick(60)

    draw(win, images, player_car, computer_car, game_info)

    while not game_info.started:
        blit_text_center(win, main_font2, f"Press any key to start level {game_info.level}")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

            if event.type == pygame.KEYDOWN:
                game_info.start_level()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    move_player(player_car)
    computer_car.move()

    handle_collision(player_car, computer_car, game_info)

    if game_info.game_finished():
        blit_text_center(win, main_font2, "You win the game!")
        pygame.time.wait(5000)
        game_info.reset()
        player_car.reset()
        computer_car.reset()

pygame.quit()

