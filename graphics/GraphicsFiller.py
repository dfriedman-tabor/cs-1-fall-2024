
# dimensions of the window
width = 700
height = 500

def draw(canvas):

    # makes the background white
    canvas.fill((255, 255, 255))

    # draws a blue rectangle at location 50, 100 with a width of 75 and height of 150
    pygame.draw.rect(canvas, (0, 0, 255), (50, 100, 75, 150))

    # draws a red circle at location 200,200 with a radius of 30
    pygame.draw.circle(canvas, (255,0,0), (200,200), 30)



# don't touch the below code!
################################

import pygame, sys
from pygame.constants import KEYDOWN
from pygame.locals import QUIT

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Flappy Bird')
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
while True:
    draw(window)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()



















