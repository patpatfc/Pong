import pygame
import sys
import random
import time

screen = pygame.display.set_mode ((800, 600))
pygame.init ()
pygame.display.set_caption ("pong")
y = 295
m = 395
x = 250
z = 250
changex = 0
changezup = 0
changezdown = 0
ilkadam = 0
ikinciadam = 0
ychange = random.randint (3, 5)
mchange = random.randint (3, 5)
black = (0, 0, 0)
white = (255, 255, 255)
px = (120, 120, 120)
# topzaman = 0

while True:
    screen.fill (black)
    myfont = pygame.font.SysFont ("monospace", 70)
    label = myfont.render (str (ilkadam), 1, px)
    screen.blit (label, (5, 5))
    myfont = pygame.font.SysFont ("monospace", 70)
    gey = myfont.render (str (ikinciadam), 1, px)
    screen.blit (gey, (770, 5))
    pygame.draw.rect (screen, white, (10, x, 10, 100))
    pygame.draw.rect (screen, white, (780, z, 10, 100))
    pygame.draw.ellipse (screen, white, (m, y, 10, 10))
    y += ychange
    m += mchange
    b = random.uniform (0.9, 1.1)
    pygame.display.update ()
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit ()
            sys.exit ()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and z > 0:
                changezup = -5
            if event.key == pygame.K_DOWN and z < 700:
                changezdown = 5
            if event.key == pygame.K_w and x < 700:
                changex = -5
            if event.key == pygame.K_s:
                changex = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                changezup = 0
            elif event.key == pygame.K_DOWN:
                changezdown = 0
            if event.key == pygame.K_s or event.key == pygame.K_w:
                changex = 0

    x += changex
    z += changezdown + changezup
    if m < 0:
        ikinciadam += 1
        y = 295
        m = 395
        x = 250
        z = 250
        # topzaman = 0
        ychange = random.randint (3, 6)
        mchange = random.randint (3, 6)
        time.sleep (1)
    elif m > 800:
        ilkadam += 1
        y = 295
        m = 395
        x = 250
        z = 250
        ychange = random.randint (3, 6)
        mchange = random.randint (3, 6)
        # topzaman = 0
        time.sleep (1)
    if y < 0:
        ychange = ychange * -b
    elif y > 592:
        ychange = ychange * -b
    if x < y < x + 100 and 10 < m < 20:
        mchange = mchange * -b
        ychange *= 1.1
        mchange *= 1.1
    elif z < y < z + 100 and 772 < m < 780:
        mchange = mchange * -b
        ychange *= 1.1
        mchange *= 1.1

    if x == 700:
        for event in pygame.event.get ():
            if event.key == pygame.K_w:
                changex = 0

    # print(topzaman)
    # topzaman = time.time()
    # if 10 < topzaman < 10.02:
    #   mchange = mchange * 1.5
    #  ychange = ychange * 1.5
    # if 15 < topzaman < 15.02:
    #   mchange = mchange * 1.5
    #  ychange = ychange * 1.5
    # if 20 < topzaman < 20.2:
    #   mchange = mchange * 1.5
    #  ychange = ychange * 1.5
    # if 25 < topzaman < 25.02:
    #   mchange = mchange * 1.5
    #  ychange = ychange * 1.5
    # if 30 < topzaman < 30.02:
    #   mchange = mchange * 1.5
    #  ychange = ychange * 1.5
    # if 35 < topzaman < 35.02:
    #   mchange = mchange * 1.5
    #  ychange = ychange * 1.5
    # if 1489435125.4949398 < topzaman < 1489436125.4949398:
    #   mchange = mchange * 1.5
    #  ychange = ychange * 1.5

