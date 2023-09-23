import pygame
import time
import math
from utilities import scale_image, blit_rotate_car

pygame.init()

######__IMAGES AND BACKGROUNDS___######
GRASS = scale_image(pygame.image.load("grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("track.png"), 0.9)

TRACK_BORDER = scale_image(pygame.image.load("track-border.png"), 0.9)
FINISH = pygame.image.load("finish.png")

RED_CAR = scale_image(pygame.image.load("red-car.png"), 0.55)
GREEN_CAR = scale_image(pygame.image.load("green-car.png"), 0.55)

#   PYGAME DISPLAY
WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("racing game")

FPS = 60


class absractcar:
    def __abs__(self, max_vel, rotation_vel):
        self.img = self.Img
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        if right:
            self.angle -= self.rotation_vel
    def draw(self, win):
        blit_rotate_car(win,self.img)


class Playercar(absractcar):
    Img = RED_CAR

clock = pygame.time.Clock()


def draw(win, image):
    for img, pos in image:
        WIN.blit(img, pos)


images = [(GRASS, (0, 0)), (TRACK, (0, 0))]
run = True
while run:
    clock.tick(FPS)
    pygame.display.update()
    draw(WIN, images)
    WIN.blit(RED_CAR, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
pygame.quit()
