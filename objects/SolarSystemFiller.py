# filler code for a solar system simulation

import math
from os import times


width = 770
height = 770

dist_scale = 13e9
time_scale = 2e5
planet_scale = 1

G = 6.67e-11

# class here

# variables here


def move():
    pass



def draw(canvas):
    pass

def keyPressed(key):
    pass


# don't touch the below code!
################################

import pygame, sys
from pygame.constants import KEYDOWN
from pygame.locals import QUIT

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Solar System')
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
        if event.type == KEYDOWN:
            keyPressed(event.key)
    pygame.display.update()
    clock.tick(30)

