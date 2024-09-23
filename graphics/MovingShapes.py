# moving shapes solution

# dimensions of the window
width = 700
height = 500

# variables to store the ball's x location and speed in the x direction
barX = 0
barY = 0
barXSpeed = 5
barWidth = 40

rectX = 350
rectY = 250
rectXSpeed = 5
rectYSpeed = 4
rectWidth = 30

ball1X = 350
ball1Y = 250
ball1XSpeed = 3
ball1Rad = 25

ball2X = 350
ball2Y = 250
ball2YSpeed = 6
ball2Rad = 45

def move():
    global barX, rectX, rectY, rectXSpeed, rectYSpeed, ball1XSpeed, ball1X, ball2Y, ball2YSpeed

    # move and reset the column
    barX += barXSpeed
    if barX >= width:
        barX = -barWidth

    # move and bounce the square
    rectX += rectXSpeed
    rectY += rectYSpeed
    if rectX + rectWidth >= width or rectX <= 0:
        rectXSpeed *= -1
    if rectY + rectWidth >= height or rectY <= 0:
        rectYSpeed *= -1

    # move and bounce the first ball
    ball1X += ball1XSpeed
    if ball1X + ball1Rad >= width or ball1X - ball1Rad <= 0:
        ball1XSpeed *= -1

    # move and bounce the second ball
    ball2Y += ball2YSpeed
    if ball2Y + ball2Rad >= height or ball2Y - ball2Rad <= 0:
        ball2YSpeed *= -1


def draw(canvas):
    canvas.fill((255,255,255))

    # draw the two balls
    pygame.draw.circle(canvas, (255, 120, 0), (ball2X, ball2Y), ball2Rad)
    pygame.draw.circle(canvas, (0, 120, 0), (ball1X, ball1Y), ball1Rad)

    # draw the column
    pygame.draw.rect(canvas, (120, 0, 0), (barX, barY, barWidth, height))

    # draw the square
    pygame.draw.rect(canvas, (120, 0, 120), (rectX, rectY, rectWidth, rectWidth))




# don't touch the below code!
################################

import pygame, sys
from pygame.constants import KEYDOWN
from pygame.locals import QUIT

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Moving Shapes')
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

