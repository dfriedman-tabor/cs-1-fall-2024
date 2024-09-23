# filler code for graphics with key controls

# feel free to change the window size
WIDTH = 600
HEIGHT = 600

# your variables here


def move():
    # your code here


# handles what should happen when a key is pressed
# note that this only activates once per press - it does not
# activate repeatedly if the key is held down
def keyPressed(event):
    # an example of how to check if a certain key is pressed
    if event.key == pygame.K_w:
        print("w pressed")



# handles what should happen when a key is released
def keyReleased(event):
    # an example of how to check if a certain key is released
    if event.key == pygame.K_w:
        print("w released")


# defines how we want to draw our window
def draw(canvas):
    # set the background white - feel free to change this color!
    canvas.fill((255,255,255))

    # add more shapes here

# ************** DON'T TOUCH THE BELOW CODE ***************************
import pygame, sys
from pygame.locals import *
import random
# always need this - starts the graphics
pygame.init()
pygame.font.init()
fps = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman', 30)
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Pong')

# loop to keep the game continuously running
while True:

    # update any variables
    move()

    # draw our graphics
    draw(window)

    # this cycles through all the events that may happen during the game
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            keyPressed(event)
        elif event.type == KEYUP:
            keyReleased(event)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    # update the graphics display
    pygame.display.update()

    # rest for 60 milliseconds
    fps.tick(60)
