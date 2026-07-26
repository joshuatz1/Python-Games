# Write your code here :-)
import pygame as pg

#constants
SW, SH = 900, 1000
SCREENSIZE = (SW, SH)
FPS = 60

#star pygame
pg.init()
screen = pg.display.set_mode(SCREENSIZE)
clock = pg.time.Clock()

font = pg.font.Font(None, 64)

playerIMG = pg.image.load("assets/images/burger.png")
playerIMG = pg.transform.scale(playerIMG, (27, 27))



#colours
white = (225, 232, 230)
blue = (36, 42, 128)
red = (219, 42, 42)
orange = (143, 76, 64)
purple = (90, 33, 107)
#pg.Rect(SW//2-250//2, SH//2-150//2, 250, 150),

def reset():
    global allWalls,walls,walls2, walls3, walls4, player, GAME, running, counter, centerwall, topwalls1, bottomwalls1, twalls, sidewalls

    wallThink = 20
    #wall = (x, y, length, width (uniform))
    #80 dist inc w dwww

    #LT, BG
    walls = [pg.Rect(0, 0, 900, wallThink), pg.Rect(100, 100, 150, wallThink), pg.Rect(100, 100, wallThink, 100), pg.Rect(100, 200, 150, wallThink),
    pg.Rect(250, 100, wallThink, 120), pg.Rect(0, 980, 900, wallThink), pg.Rect(0, 0, wallThink, 980), pg.Rect(880, 0, wallThink, 980)]

    #LB
    walls2 = [pg.Rect(100, 700, 150, wallThink), pg.Rect(100, 700, wallThink, 100), pg.Rect(100, 800, 150, wallThink),
    pg.Rect(250, 700, wallThink, 120)]

    #RT
    walls3 = [pg.Rect(650, 100, 150, wallThink), pg.Rect(780, 100, wallThink, 100), pg.Rect(650, 200, 150, wallThink),
    pg.Rect(630, 100, wallThink, 120)]

    #RB
    walls4 =[pg.Rect(650, 700, 150, wallThink), pg.Rect(780, 700, wallThink, 100), pg.Rect(650, 800, 150, wallThink),
    pg.Rect(630, 700, wallThink, 120)]

    topwalls1 = [pg.Rect(350, 200, 200, wallThink), pg.Rect(440, 200, wallThink, 150)]

    centerwall = [ pg.Rect(325, 425, wallThink, 150), pg.Rect(575, 425, wallThink, 150),
    pg.Rect(325, 575, 270, wallThink), pg.Rect(325, 425, 270, wallThink)]

    bottomwalls1 = [pg.Rect(350, 680, 200, wallThink), pg.Rect(440, 680, wallThink, 150)]

    twalls = [pg.Rect(220, 890, 200, wallThink), pg.Rect(340, 800, wallThink, 110), pg.Rect(490, 890, 200, wallThink), pg.Rect(550, 800, wallThink, 110),
    pg.Rect(150, 290, 200, wallThink), pg.Rect(240, 310, wallThink, 110), pg.Rect(570, 290, 200, wallThink), pg.Rect(660, 310, wallThink, 110)]

    sidewalls = [pg.Rect(120, 415, wallThink, 200), pg.Rect(130, 515, 130, wallThink), pg.Rect(760, 415, wallThink, 200),
    pg.Rect(650, 515, 130, wallThink)]




    allWalls = walls3 + walls2 + walls + walls4 + centerwall + topwalls1 + bottomwalls1 + twalls + sidewalls


    player = pg.Rect(SW//2 - 25//2, SH//2 - 25//2 , 32, 32)
    #pg.Rect(90, 140, wallThink, 200), pg.Rect(160, 140, wallThink, 150), pg.Rect(180, 140, 200, wallThink), pg.Rect(380, 140, wallThink, 150),
    #pg.Rect(90, 140, wallThink, 280), pg.Rect(450, 140, wallThink, 150), pg.Rect(30, 200, wallThink, 300), pg.Rect(0, 200, 30, wallThink),
    #pg.Rect(467, 140, 333, wallThink), pg.Rect(730, 90, wallThink, 50), pg.Rect(90, 415, 240, wallThink), pg.Rect(160, 350, 150, wallThink),
    #pg.Rect(160, 270, 150, wallThink), pg.Rect(30, 480, 150, wallThink), pg.Rect(180, 480, 220, wallThink), pg.Rect(310, 350, 90, wallThink),
    #pg.Rect(380, 370, wallThink, 130), pg.Rect(400, 350, 150, wallThink), pg.Rect(450, 270, 100, wallThink), pg.Rect(445, 415, 360, wallThink),
    #pg.Rect(550, 270, 250, wallThink), pg.Rect(550, 350, 180, wallThink), pg.Rect(445, 480, 360, wallThink), pg.Rect(0, 980, 900, wallThink),
    #pg.Rect(445, 500, wallThink, 40), pg.Rect(525, 540, wallThink, 40), pg.Rect(605, 500, wallThink, 40), pg.Rect(685, 540, wallThink, 40)]




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
        running = True
        player[0] = 450
        player[1] = 450

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



        for i in allWalls:
            pg.draw.rect(screen, "aquamarine", i)
            if player.colliderect(i):
                #running = False
                pass
            if player[0] > SW or player[0] < 0:
                running = False

        for i in centerwall: #for testing walls / delete after
            pg.draw.rect(screen, "green", i)
        for i in topwalls1:
            pg.draw.rect(screen, "yellow", i)

        pg.display.flip()
        clock.tick(FPS)
        if keys[pg.K_2]:
            Menu = True
            running = False
    else:
        screen.fill("green")
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

    mx, my = pg.mouse.get_pos()
    L, M, R = pg.mouse.get_pressed()
    print(mx, my,)
    print( L, M, R)





pg.quit()
print("program ended")
