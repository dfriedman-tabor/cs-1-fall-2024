# template code for you to fill in when making pygame program with moving pieces. no user controls


# dimensions of the window
width = 700
height = 500

def move():
    # write your code to move pieces here

def draw(canvas):
    # makes the background white
    canvas.fill((255,255,255))

    # draw your pieces here



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
while True:
    move()
    draw(window)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()



















