# template code for you to use when in need of mouse clicks and key presses
from random import randint

# dimensions of the window
width = 400
height = 400


def draw(canvas):

    canvas.fill((255,255,255))


def mousePressed(mouseX, mouseY):
    pass

def keyPressed(key):
    pass



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



















