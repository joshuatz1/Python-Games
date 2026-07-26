# Write your code here :-)
import pygame as pg
import random

#constants
SW, SH = 800, 600
SCREENSIZE = (SW, SH)
FPS = 60

#star pygame
pg.init()

screen = pg.display.set_mode(SCREENSIZE)
background = pg.image.load("assets/images/backgroundtwo.png")
background = pg.transform.scale(background, (800, 600))


clock = pg.time.Clock()


#variables
GAME = True
white = (225, 232, 230)
blue = (36, 42, 128)
red = (219, 42, 42)
orange = (143, 76, 64)
purple = (90, 33, 107)
px, py, pw, ph = 50, 50, 50, 50

x, y, w, h = 700, 0, 50, 200

#gap = random.randint(200, 350)


PipeVal = (x, y, w, h)

PipeValBottom = (700, 450, 50, 200)
player = (px, py, pw, ph)
flappybird = pg.Rect(player)

gravity = 3
vertical = 5

font = pg.font.Font(None, 64)
bird = pg.image.load("assets/images/bird.png")
topPipe = pg.image.load("assets/images/pipeTop.png")
pipe = pg.image.load("assets/images/pipe.png")
jumpSound = pg.mixer.Sound("assets/sounds/jump.wav")
jumpSound.set_volume(.25)


gameOverMusic = pg.mixer.Sound("assets/sounds/gameOver.mp3")
gameOverMusic.set_volume(.2)
gameOverMusic.stop()

pg.mixer.music.stop()
BG_music = pg.mixer.music.load("assets/sounds/9MinuteMusicLofiSnowyForest.mp3")
BG_music = pg.mixer.music.set_volume(.25)
pg.mixer.music.play(-1, 0.0)

TPipe = pg.Rect(PipeVal)
BPipe = pg.Rect(PipeValBottom)

font = pg.font.Font(None, 64)
score = 0
running = True

pipeSpeed = 5
while GAME:
    #EVENTS
    for event in pg.event.get():
        if event.type == pg.QUIT:
            GAME = False
    #INPUTS
    key = pg.key.get_pressed()
    if key[pg.K_r]:
        running = True
        gravity = -2
        flappybird[1] += gravity
        flappybird[1] = 70
        TPipe[0] = 800
        BPipe[0] = 800
        score = 0
        pipeSpeed = 5

    if key[pg.K_w]:
        gravity = -2
        jumpSound.play()




    L, M, R = pg.mouse.get_pressed()

    #makes pipes move
    TPipe[0] -= pipeSpeed
    BPipe[0] -= pipeSpeed

    flappybird[1] += gravity


    if flappybird[1] > SH or flappybird[1] < 0:
        running = False


    if L:
        gravity = -2
        jumpSound.play()

    #UPDATES
    gravity += 0.1
    flappybird[1] += gravity


    if flappybird.colliderect(TPipe):
        print("collision")
        running = False
    if flappybird.colliderect(BPipe):
        print("collision")
        running = False

    if running:
        #DRAWS
        screen.blit(background, (0, 0))
        #screen.fill(blue)

        myScore = font.render("Score: "+str(score), True, orange)
        screen.blit(myScore, ( 50, 50 ))

        screen.blit(bird, (flappybird[0]-10,flappybird[1]))
        #pg.draw.ellipse(screen, "red", flappybird,2)

        screen.blit(topPipe, (TPipe[0],TPipe[1]))
        #pg.draw.rect(screen, "green", TPipe)

        screen.blit(pipe, (BPipe[0],BPipe[1]))
        #pg.draw.rect(screen, "green", BPipe)
        if TPipe[0] < 0 :
            pg.draw.rect(screen, "brown", TPipe)
            score += 1
            pipeSpeed += 0.8
            TPipe[0] = 800
            BPipe[0] = 800
        #FLIP/CLOCK
        pg.display.flip()
        clock.tick(FPS)


    else:
        screen.fill("green")
        print("Game Over")
        pg.display.flip()
        clock.tick(FPS)







pg.quit()
print("Game Over")

# Write your code here :-)
