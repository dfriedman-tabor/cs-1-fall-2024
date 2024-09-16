# template code for you to fill in when creating basic pygame art


# dimensions of the window
width = 700
height = 500

def draw(canvas):
    # makes the background white
    canvas.fill((255,255,255))

    # purple circle at location (200, 400), with radius 50
    pygame.draw.circle(canvas, (255, 0, 255), (200, 400), 50)

    # green rectangle at location (50, 50) with width 100 and height 300
    pygame.draw.rect(canvas, (0, 255, 0), (50, 50, 100, 300))

    # a yellow line connecting points (50, 50) and (500, 400), with width 10
    pygame.draw.line(canvas, (255,255,0), (50,50), (500,400), 10)

    # a cyan triangle made by connecting points (400, 50), (400, 200), and (600, 125)
    pygame.draw.polygon(canvas, (0,255,255), [(400, 50), (400,200),(600,125)])


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



















