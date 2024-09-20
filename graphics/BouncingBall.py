# bouncing ball example


# dimensions of the window
width = 900
height = 500

# variables to store the ball's location, speed, and size
ball1x = 200
ball1y = 300
ball1speedx = 1
ball1speedy = 9
ball1rad = 20

def move():
    # any variables that change within this def need to be labeled global
    global ball1x, ball1speedx, ball1speedy, ball1y

    # move the ball in x and y directions
    ball1x += ball1speedx
    ball1y += ball1speedy

    # if the ball reaches the left or right walls, flip its direction
    if ball1x >= width:
        ball1speedx = -ball1speedx
    elif ball1x <= 0:
        ball1speedx = -ball1speedx

    # if the ball reaches the top or bottom walls, flip its direction
    if ball1y >= height:
        ball1speedy = -ball1speedy
    elif ball1y <= 0:
        ball1speedy = -ball1speedy

def draw(canvas):
    canvas.fill((255,255,255))

    # draw the ball using its coordinate variables
    pygame.draw.circle(canvas, (255, 120, 0), (ball1x, ball1y), ball1rad)


# don't touch the below code!
################################

import pygame, sys
from pygame.constants import KEYDOWN
from pygame.locals import QUIT

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bouncing Ball')
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
clock = pygame.time.Clock()

while True:
    move()
    draw(window)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)

