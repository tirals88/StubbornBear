import pygame, random, sys
from pygame.locals import *

Lc = 1 #Level const

FPS = 25*Lc
WINDOWWIDTH = 480
WINDOWHEIGHT = 640
BOXSIZE = 120
GAPSIZE = 15
BOARDWIDTH = 3
BOARDHEIGHT = 3
XMARGIN = int((WINDOWWIDTH -(BOARDWIDTH * (BOXSIZE + GAPSIZE)))/2)
YMARGIN = int((WINDOWHEIGHT -(BOARDHEIGHT * (BOXSIZE + GAPSIZE)))/2)

# Color Lists
GRAY     = (125, 125, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE

SCORE = 0
tick_C = 40

# Character Lists
BearImg = pygame.image.load("stubborn_bear.png")
Hit_BImg = pygame.image.load("Hit_bear.png")

PandaImg = pygame.image.load("Panda.png")
Hit_PImg = pygame.image.load("Hit_panda.png")

JellyImg = pygame.image.load("Jelly.png")
Hit_JImg = pygame.image.load("Hit_jelly.png")

pygame.font.init()
font = pygame.font.SysFont("comicsansms", 40)

num_lst = [1,2,3]
random.shuffle(num_lst)
num_1 = num_lst[0]
num_2 = num_lst[1]
num_3 = num_lst[2]

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption('Stubborn Bear')
    boxx = None
    boxy = None
    randBoxes = generateNoneBoxes(0)
    
    DISPLAYSURF.fill(BGCOLOR)

    event_key = [[K_KP7, K_KP4, K_KP1], 
                [K_KP8, K_KP5, K_KP2], 
                [K_KP9, K_KP6, K_KP3]]
    SCORE = 0
    tick_C = 40
    randBoxes = generateNoneBoxes(0)
    while True:
        keyPressed = False
        
        if SCORE >= 1000:
            Lc = 2
        elif SCORE >= 3000:
            Lc = 4
        elif SCORE >= 5000:
            Lc = 6
        elif SCORE < 1000:
            Lc = 1
        else:
            Lc = 2.1
        FPS = 25*Lc

        if SCORE < 0 :
            SCORE = 0
        score  = "Score : " + str(SCORE)
        text = font.render(score, True, (0, 128, 0))

        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(text, (XMARGIN, YMARGIN/2))

        drawBoard(randBoxes, DISPLAYSURF, tick_C)
        if tick_C == 40:
            tick_C = 0
        else: tick_C += 1

    
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                for i in range(3):
                    if event.key in event_key[i]:
                        boxx = i
                        boxy = event_key[i].index(event.key)
                        if randBoxes[boxx][boxy][0] == num_1:
                            if randBoxes[boxx][boxy][2] == 0:
                                SCORE += 100
                                randBoxes[boxx][boxy][2] = 1
                                randBoxes[boxx][boxy][1] = 0

                        if randBoxes[boxx][boxy][0] == num_2:
                            if randBoxes[boxx][boxy][2] == 0:
                                SCORE += 100
                                randBoxes[boxx][boxy][2] = 1
                                randBoxes[boxx][boxy][1] = 0

                        if randBoxes[boxx][boxy][0] == num_3:
                            if randBoxes[boxx][boxy][2] == 0:
                                SCORE -= 200
                                randBoxes[boxx][boxy][2] = 1
                                randBoxes[boxx][boxy][1] = 0

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def generateNoneBoxes(num):
    # 처음 게임 보드 생성
    randBoxes = []
    for i in range(BOARDHEIGHT):
        lineBox = []
        for j in range(BOARDWIDTH):
            lineBox.append([num,0,0])
        randBoxes.append(lineBox)

    return randBoxes
def ReBoxes(randBoxes, boxx, boxy):
    randBoxes[boxx][boxy] = [0, 0, 0]

def drawBoard(randBoxes, DISPLAYSURF, tick_C):
    #게임 화면 그리기
    if tick_C == 40:
        getRandNum(randBoxes)


    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsofBox(boxx, boxy)
            if randBoxes[boxx][boxy][0] == 0 :
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
            else:
                if randBoxes[boxx][boxy][0] == 1:
                    if randBoxes[boxx][boxy][2] == 0:
                        if randBoxes[boxx][boxy][1] == 50:
                            ReBoxes(randBoxes, boxx, boxy)
                            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
                        else:
                            DISPLAYSURF.blit(BearImg, (left, top))
                            randBoxes[boxx][boxy][1] += 1
                            
                    if randBoxes[boxx][boxy][2] == 1:
                        if not randBoxes[boxx][boxy][1] == 30:
                            DISPLAYSURF.blit(Hit_BImg, (left, top))
                            randBoxes[boxx][boxy][1] += 1
                        else :
                            ReBoxes(randBoxes, boxx, boxy)
                            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
                if randBoxes[boxx][boxy][0] == 2:
                    if randBoxes[boxx][boxy][2] == 0:
                        if randBoxes[boxx][boxy][1] == 50:
                            ReBoxes(randBoxes, boxx, boxy)
                            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
                        else:
                            DISPLAYSURF.blit(PandaImg, (left, top))
                            randBoxes[boxx][boxy][1] += 1
                    if randBoxes[boxx][boxy][2] == 1:
                        if not randBoxes[boxx][boxy][1] == 30:
                            DISPLAYSURF.blit(Hit_PImg, (left, top))
                            randBoxes[boxx][boxy][1] += 1
                        else :
                            ReBoxes(randBoxes, boxx, boxy)
                            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
                if randBoxes[boxx][boxy][0] == 3:
                    if randBoxes[boxx][boxy][2] == 0:
                        if randBoxes[boxx][boxy][1] == 50:
                            ReBoxes(randBoxes, boxx, boxy)
                            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
                        else:
                            DISPLAYSURF.blit(JellyImg, (left, top))
                            randBoxes[boxx][boxy][1] += 1
                    if randBoxes[boxx][boxy][2] == 1:
                        if not randBoxes[boxx][boxy][1] == 30:
                            DISPLAYSURF.blit(Hit_JImg, (left, top))
                            randBoxes[boxx][boxy][1] += 1
                        else :
                            ReBoxes(randBoxes, boxx, boxy)
                            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
                

def leftTopCoordsofBox(boxx, boxy):
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    left = abs(left)
    top = abs(top)
    return (left, top)

def getRandNum(randBoxes):
    #선택 된 3 개의 박스를 장애물과 표적을 랜덤으로 표현
    choseBoxes = ThreeOfNine(randBoxes)
    for x in choseBoxes:
        boxx = x[0]
        boxy = x[1]
        randBoxes[boxx][boxy][0] = random.randint(1,3)

def ThreeOfNine(randBoxes):
    #9 개 중에서 3 개의 박스 선택
    choseBoxes = []
    sampleBoxes = []
    j = random.randint(0,8)
    while not len(sampleBoxes)==3:
        a = j//3
        b = j%3

        if (j in sampleBoxes) or (randBoxes[a][b][0] != 0):
            j = random.randint(0,8)
        else: 
            sampleBoxes.append(j)

    for j in sampleBoxes:
        a = j//3
        b = j%3
        ch_tuple = (a,b)
        
        choseBoxes.append(ch_tuple)
    choseBoxes.sort()

    return choseBoxes
     # 다시 randBoxes 초기화

    #pygame.time.wait(3000) # 1000ms = 1s
    
main()