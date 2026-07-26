# Write your code here :p

import pygame as pg
from math import sqrt
#constants
SW, SH = 800, 600
SCREENSIZE = (SW, SH)
FPS = 60

#star pygame
pg.init()
screen = pg.display.set_mode(SCREENSIZE)
clock = pg.time.Clock()

GAME = True

#colours
white = (225, 232, 230)
blue = (36, 42, 128)
red = (219, 42, 42)
orange = (143, 76, 64)
purple = (90, 33, 107)

#playerpositions
x = 0
px, py, pw, ph = 50, 100, 25, 25
player = (px, py, pw, ph)
player1 = pg.Rect(100, 100, 25, 75)


RED = pg.Rect(500, 250, 50, 50)
BLUE = pg.Rect(200, 250, 50, 50)
PURPLE = pg.Rect(350, 500, 50, 50)

running = True



def closeTo(rect1,rect2,rect3):
    mX, mY = pg.mouse.get_pos()
    print("mouse X: "+str(mX)+ " mouse Y: "+str(mY))


    px, py = rect3.center
    cx, cy = rect1.center
    bx, by = rect2.center
    distance3 = sqrt((mX - px)**2 + (mY - py)**2)
    distance2 = sqrt((mX - bx)**2 + (mY - by)**2)
    distance = sqrt((mX - cx)**2 + (mY - cy)**2)
    print(distance)
    print(distance2)
    print(distance3)

    if distance < distance2 and distance < distance3:
        return rect1
    elif distance2 < distance and distance2< distance3:
        return rect2
    elif distance3 < distance2 and distance3 < distance:
        return rect3



while GAME:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            GAME = False



    if running:
        screen.fill("light blue")
        #pg.draw.rect(screen, (x,x,x), (200, 200, 50, 50))
        #pg.draw.rect(screen, (255,0,0), player)
        #pg.draw.rect(screen, white, player1)
        #x += 1
        #print(x)
        #if x == 255:
           # x = 0
            #running = False

        pg.draw.rect(screen, red, RED)
        pg.draw.rect(screen, blue, BLUE)
        pg.draw.rect(screen, purple, PURPLE)
        pg.draw.rect(screen,"green", closeTo(RED,BLUE,PURPLE))

        pg.display.flip()
        clock.tick(FPS)
    else:
        screen.fill("green")
        pg.display.flip()
        clock.tick(FPS)

pg.quit()
print("Game Over")


