# example for drawing multiple objects at once using a for loop

# dimensions of the window
width = 700
height = 500

def draw(canvas):
    # makes the background white
    canvas.fill((255,255,255))

    # draw a row of circles left to right across the screen
    x = 0
    for i in range(0, 20):
        pygame.draw.circle(canvas, (255,0,0), (x, 300), 25)
        x += 50


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
    draw(window)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


















