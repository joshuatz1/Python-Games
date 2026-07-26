# Write your code here :-)
import pygame as pg

# Write your code here :-)
#constants
SW, SH = 800, 600
SCREENSIZE = (SW, SH)
FPS = 60

#star pygame
pg.init()
screen = pg.display.set_mode(SCREENSIZE)
clock = pg.time.Clock()

font = pg.font.Font(None, 64)

playerIMG = pg.image.load("assets/images/burger.png")
playerIMG = pg.transform.scale(playerIMG, (25, 25))

BG_music = pg.mixer.music.load("assets/sounds/backgroundMusic.mp3")
BG_music = pg.mixer.music.set_volume(.25)
pg.mixer.music.play(-1, 0.0)

crashSound = pg.mixer.Sound("assets/sounds/explosion_gameOver.wav")
crashSound.set_volume(.5)


#colours
white = (225, 232, 230)
blue = (36, 42, 128)
red = (219, 42, 42)
orange = (143, 76, 64)
purple = (90, 33, 107)

def reset():
    global walls, player, GAME, running, counter

    wallThink = 20

    walls = [pg.Rect(50, 70, 700, wallThink),
    pg.Rect(0, 0, 800, wallThink), pg.Rect(0, 140, 100, wallThink),
    pg.Rect(90, 140, wallThink, 200), pg.Rect(160, 140, wallThink, 150), pg.Rect(180, 140, 200, wallThink), pg.Rect(380, 140, wallThink, 150),
    pg.Rect(90, 140, wallThink, 280), pg.Rect(450, 140, wallThink, 150), pg.Rect(30, 200, wallThink, 300), pg.Rect(0, 200, 30, wallThink),
    pg.Rect(467, 140, 333, wallThink), pg.Rect(730, 90, wallThink, 50), pg.Rect(90, 415, 240, wallThink), pg.Rect(160, 350, 150, wallThink),
    pg.Rect(160, 270, 150, wallThink), pg.Rect(30, 480, 150, wallThink), pg.Rect(180, 480, 220, wallThink), pg.Rect(310, 350, 90, wallThink),
    pg.Rect(380, 370, wallThink, 130), pg.Rect(400, 350, 150, wallThink), pg.Rect(450, 270, 100, wallThink), pg.Rect(445, 415, 360, wallThink),
    pg.Rect(550, 270, 250, wallThink), pg.Rect(550, 350, 180, wallThink), pg.Rect(445, 480, 360, wallThink), pg.Rect(0, 580, 800, wallThink),
    pg.Rect(445, 500, wallThink, 40), pg.Rect(525, 540, wallThink, 40), pg.Rect(605, 500, wallThink, 40), pg.Rect(685, 540, wallThink, 40)]

    player = pg.Rect(767, 100, 25, 25)

    #GAME = True
    #running = True
    #counter = 0
    #screen.fill("blue")
    #for i in walls:

            #print(counter)
            #pg.draw.rect(screen, "blue", i,2)

            #if (counter == 1 or counter == 0):
                #print("hey")
                #pg.draw.rect(screen, "red", i,2)
            #else:
                #pg.draw.rect(screen, "white", i)


            #counter +=1

reset()

GAME = True
Menu = True
running = False

while GAME:

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        player[1] -= 3
        pass
    if keys[pg.K_a]:
        player[0] -= 5
        pass
    if keys[pg.K_s]:
        player[1] += 3
        pass
    if keys[pg.K_d]:
        player[0] += 5
        pass
    if keys[pg.K_r]:
        BG_music = pg.mixer.music.load("assets/sounds/backgroundMusic.mp3")
        BG_music = pg.mixer.music.set_volume(.25)
        pg.mixer.music.play(-1, 0.0)
        running = True
        player[0] = 767
        player[1] = 100


    if Menu:
        screen.fill("black")
        MenuTextOne = font.render("Main Menu", True, "white")
        MenuTextTwo = font.render("Press 1 to play game", True, "white")
        MenuTextThree = font.render("Press 2 to go back to main menu", True, "white")
        screen.blit(MenuTextOne, (260, 100))
        screen.blit(MenuTextTwo, (180, 300))
        screen.blit(MenuTextThree, (50, 380))
        pg.display.flip()
        clock.tick(FPS)
        if keys[pg.K_1]:
            Menu = False
            running = True


    elif running:
        screen.fill("black")
        screen.blit(playerIMG, player)
        #pg.draw.rect(screen, "white", player, 2)

        for i in walls:
            pg.draw.rect(screen, "aquamarine", i)
            if player.colliderect(i):
                crashSound.play()
                running = False
            if player[0] > SW or player[0] < 0:
                running = False

        pg.display.flip()
        clock.tick(FPS)
        if keys[pg.K_2]:
            Menu = True
            running = False
    else:
        screen.fill("green")
        #BG_music.stop()
        pg.mixer.music.stop()
        gameOverText = font.render("GAME OVER", True, "white")
        gameOverTextTwo = font.render("Press 'R' Key To Reload", True, "white")
        screen.blit(gameOverText, (260, 275))
        screen.blit(gameOverTextTwo, (180, 360))
        pg.display.flip()
        clock.tick(FPS)


    #mx, my = pg.mouse.get_pos()
    #print(mx, my)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            GAME = False



pg.quit()
print("program ended")

