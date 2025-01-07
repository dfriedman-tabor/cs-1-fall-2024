# template code for you to fill in when making pygame program with moving pieces. no user controls


class Smiley:

    def __init__(self, x, y, speedx, speedy, size, eyeColor, smileColor):
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.size = size
        self.eyeColor = eyeColor
        self.smileColor = smileColor

    def draw(self, canvas):

        pygame.draw.circle(canvas, self.eyeColor, (self.x + self.size/4, self.y + self.size/4), self.size/8)
        pygame.draw.circle(canvas, self.eyeColor, (self.x + self.size*3/4, self.y + self.size/4), self.size/8)


# dimensions of the window
width = 700
height = 500

face = Smiley(100,100,0,0, 300, (255,0,0),(0,255,0))

def move():
    pass
    # write your code to move pieces here

def draw(canvas):
    # makes the background white
    canvas.fill((255,255,255))

    # draw your pieces here
    face.draw(canvas)



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
    clock.tick(30)

















