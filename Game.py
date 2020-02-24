import pygame
import random
import time

pygame.init()

#Окно
okno = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("SpaceJorney")

pygame.mixer.music.load('Test.mp3')
pygame.mixer.music.play()

walkRight = [pygame.image.load('sprite/1R.png'),pygame.image.load('sprite/2R.png'),
pygame.image.load('sprite/3R.png'),pygame.image.load('sprite/4R.png'),
pygame.image.load('sprite/5R.png'),pygame.image.load('sprite/6R.png')]

walkLeft = [pygame.image.load('sprite/1L.png'),pygame.image.load('sprite/2L.png'),
pygame.image.load('sprite/3L.png'),pygame.image.load('sprite/4L.png'),
pygame.image.load('sprite/5L.png'),pygame.image.load('sprite/6L.png')]

playerStand = pygame.image.load('sprite/0.png')
background = pygame.image.load('sprite/BG.png')
background2 = pygame.image.load('sprite/BG2.png')
spaceship = pygame.image.load('sprite/ship.png')
spaceshipScale = pygame.transform.scale(spaceship, (1050, 346))

clock = pygame.time.Clock()

#Переменные(записать их в конфиг)
player_x = 750
player_y = 580
widht = 50
height = 50
speed = 5
time = int(time.time())

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0


def drawOkno():
    # Персонаж и окно
    global animCount

    okno.blit(background, (0, 0))
    okno.blit(spaceshipScale, (500, 500))

    if animCount + 1 >= 30:
        animCount = 0
    if left:
        okno.blit(walkLeft[animCount // 5], (player_x,player_y))
        animCount += 1
    elif right:
        okno.blit(walkRight[animCount // 5], (player_x,player_y))
        animCount += 1
    else:
        okno.blit(playerStand, (player_x, player_y))

    pygame.display.update()

#def Chekc_collison(barrier):
    #for barrier in barriers:
        #if y


run = True
while run:
    clock.tick(30)

    for event in pygame.event.get(): #Взять из масива ивентов
        if event.type == pygame.QUIT: #Закрытие окна
            run = False

    #Управление
    knopka = pygame.key.get_pressed() #Отслеживание нажатой кнопки
    if knopka[pygame.K_LEFT] and player_x > 5:
        player_x -= speed
        left = True
        right = False
    elif knopka[pygame.K_RIGHT] and player_x < 1915:
        player_x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
        if knopka[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                player_y += (jumpCount ** 2) / 2
            else:
                player_y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    drawOkno()
pygame. quit()