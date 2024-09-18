# template code for you to fill in when making pygame program with moving pieces. no user controls


# dimensions of the window
width = 700
height = 500

# variables to store the ball's x location and speed in the x direction
ballX = 200
speedX = 17

def move():
    global ballX, speedX

    # move the ball by its speed
    ballX += speedX

    # if the ball reaches the left or right walls, flip its direction
    if ballX >= 700:
        speedX = -17
    elif ballX <= 0:
        speedX = 17

def draw(canvas):
    canvas.fill((255,255,255))

    # draw the ball using its x coordinate variable
    pygame.draw.circle(canvas, (255, 120, 0), (ballX, 200), 30)


# don't touch the below code!
################################

import pygame, sys
from pygame.constants import KEYDOWN
from pygame.locals import QUIT

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Graphics Starter')
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

