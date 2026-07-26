#latest version of template with class

import pygame as pg
from math import sqrt
import random
#constants
SW, SH = 800, 600
SCREENSIZE = (SW, SH)
FPS = 60



#star pygame
pg.init()
screen = pg.display.set_mode(SCREENSIZE)
clock = pg.time.Clock()
font = pg.font.Font(None, 64)
GAME = True

pIMG = pg.image.load("assets/images/car_blue.png")
playerIMG = pg.transform.scale(pIMG, (50, 100))


playerIMG_w = pg.transform.rotate(playerIMG, 0)
playerIMG_a = pg.transform.rotate(playerIMG, 90)
playerIMG_s = pg.transform.rotate(playerIMG, 180)
playerIMG_d = pg.transform.rotate(playerIMG, -90)


cashIMG = pg.image.load("assets/images/coin.png")
cashIMG = pg.transform.scale(cashIMG, (25, 25))


BG_music = pg.mixer.music.load("assets/sounds/9MinuteMusicLofiSnowyForest.mp3")
BG_music = pg.mixer.music.set_volume(.25)
pg.mixer.music.play(-1, 0.0)

jumpSound = pg.mixer.Sound("assets/sounds/jump.wav")
jumpSound.set_volume(.25)

crashSound = pg.mixer.Sound("assets/sounds/explosion_gameOver.wav")
crashSound.set_volume(.5)

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
    #global(self.hitbox[1], self.hitbox[0])

    def __init__(self, x, y, colour,who):
        self.hitbox = pg.Rect(x, y, MasterClass.w, MasterClass.h)
        self.speed = 10
        self.Colour = colour
        self.xspeed = 0
        self.yspeed = 0
        self.img = who

    def name(self):
        print("name")
    def update(self):
        self.hitbox[0] += self.xspeed
        self.hitbox[1] += self.yspeed


        pass
    def draw(self):
        #pg.draw.rect(screen, self.Colour, self.hitbox, 2)
        if self.img == 0:
            screen.blit(cashIMG , self.hitbox)
        elif self.img == 1:
            screen.blit(playerIMG_w, self.hitbox)
        elif self.img == 2:
            screen.blit(playerIMG_d, self.hitbox)
        elif self.img == 3:
            screen.blit(playerIMG_s, self.hitbox)
        elif self.img == 4:
            screen.blit(playerIMG_a, self.hitbox)


        pass
    def colliderect(self, other):
        return self.hitbox.colliderect(other.hitbox)
        #if key == "w":
            #pg.transform.rotate(player.hitbox, 90)



#creation of objects/instances
player = MasterClass(50, 50, "blue", 1)
#player.hitbox[1] - player.hitbox[3]
#player.hitbox[0] - player.hitbox[2]
#hitboxrotate = pg.transform.rotate(player.hitbox, 0)
#hitboxrotate90 = pg.transform.rotate(player.hitbox, 90)
#hitboxrotate180 = pg.transform.rotate(player.hitbox, 180)
#hitboxrotate90n = pg.transform.rotate(playerIMG, -90)

cash = MasterClass(SW//2, SH//2,"beige", 0)
speeding = 5
morespeed = 1
score = 0

running = True
while GAME:
    #EVENTS
    for event in pg.event.get():
        if event.type == pg.QUIT:
            GAME = False




    key = pg.key.get_pressed()

    if player.colliderect(cash):
        print("collided")
        cash.hitbox[1] = random.randint(100, 500)
        cash.hitbox[0] = random.randint(100, 700)

        morespeed += 1
        score += 1


    if key[pg.K_r]:
        running = True
        player.hitbox[1] = 200
        player.hitbox[0] = 400
        morespeed = 1
    if key[pg.K_w]:
        player.yspeed = -speeding - morespeed
        player.xspeed = 0
        player.hitbox[2] = 50
        player.hitbox[3] = 100
        player.img = 1
        #hitboxrotate
    if key[pg.K_a]:
        player.yspeed = 0
        player.xspeed = -speeding - morespeed
        player.hitbox[2] = 100
        player.hitbox[3] = 50
        player.img = 4
        #hitboxrotate90n
    if key[pg.K_s]:
        player.yspeed = speeding + morespeed
        player.xspeed = 0
        player.hitbox[2] = 50
        player.hitbox[3] = 100
        player.img = 3
        #hitboxrotate180

    if key[pg.K_d]:
        player.yspeed = 0
        player.xspeed = speeding + morespeed
        player.hitbox[2] = 100
        player.hitbox[3] = 50
        player.img = 2
        #hitboxrotate90

    #UPDATES

    if player.hitbox[0] > SW - player.hitbox[2] or player.hitbox[0] < 0 or player.hitbox[1] > SH - player.hitbox[3] or player.hitbox[1] < 0:
        running = False
        cash.hitbox[1] = random.randint(0, 600)
        cash.hitbox[0] = random.randint(0, 800)
        score = 0

    if running:
        screen.fill("gray")


    #DRAWS

        player.update()
        player.draw()
        #cab = pg.Rect(player.hitbox)
        #screen.blit(playerIMG, (cab[1], cab[2]))
        cash.update()
        cash.draw()
        font = pg.font.Font(None, 40)

        ScoreNumber = font.render("player score: "+str(score), True, "white")
        screen.blit(ScoreNumber, (10, 10))

    #FLIP-CLOCK

        pg.display.flip()
        clock.tick(FPS)
    else:
        screen.fill("green")
        font = pg.font.Font(None, 64)
        gameOverText = font.render("GAME OVER", True, "white")
        gameOverTextTwo = font.render("Press 'R' Key To Reload", True, "white")
        screen.blit(gameOverText, (260, 275))
        screen.blit(gameOverTextTwo, (180, 360))
        pg.display.flip()
        clock.tick(FPS)

pg.quit()
print("Game Over")


