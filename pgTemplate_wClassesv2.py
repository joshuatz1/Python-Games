#latest version of template with class

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

running = True


class MasterClass():

    w = 25
    h = 25


    def __init__(self, x, y, colour):
        self.hitbox = pg.Rect(x, y, MasterClass.w, MasterClass.h)
        self.speed = 10
        self.Colour = colour
        self.xspeed = 0
        self.yspeed = 0



    def name(self):
        print("name")
    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            Person.hitbox[1] -= Person.speed
            pass
        if keys[pg.K_a]:
            Person.hitbox[0] -= Person.speed
            pass
        if keys[pg.K_s]:
            Person.hitbox[1] += Person.speed
            pass
        if keys[pg.K_d]:
            Person.hitbox[0] += Person.speed
            pass



        #self.hitbox[0] += self.speed
        pass
    def draw(self):
        pg.draw.rect(screen, self.Colour, self.hitbox)
        pass



#creation of objects/instances
Person = MasterClass(50, 50, "blue")

running = True
while GAME:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            GAME = False

    if running:
        screen.fill("gray")

        Person.update()
        Person.draw()












        pg.display.flip()
        clock.tick(FPS)
    else:
        screen.fill("green")
        pg.display.flip()
        clock.tick(FPS)

pg.quit()
print("Game Over")


