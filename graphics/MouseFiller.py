# template code for you to use when in need of mouse clicks and key presses
from random import randint

# dimensions of the window
width = 400
height = 400

ballwidth = 40
ballheight = 60
ballx = 100
bally = 200

def draw(canvas):

    canvas.fill((255,255,255))

    # draw your image at a given location
    canvas.blit(ballImage, (ballx, bally))


def mousePressed(mouseX, mouseY):
    pass

def keyPressed(key):
    pass

def setup():
    # load your image and scale it to a given size
    global ballImage
    ballImage = pygame.transform.scale(pygame.image.load("football.png"), (ballwidth, ballheight))

# don't touch the below code!
################################

import pygame, sys
from pygame.constants import KEYDOWN
from pygame import MOUSEBUTTONDOWN
from pygame.locals import QUIT

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Graphics Starter')
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

setup()

while True:
    draw(window)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            keyPressed(event.key)
        if event.type == MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            mousePressed(mx, my)
    pygame.display.update()



















