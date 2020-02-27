import pygame, sys, time
FPS = 60  # кадров в сек

# Переменные
direction = False
isJump = False
FPS = 60
myStep = 10
jumpCount = 8

pygame.init()

fpsClock = pygame.time.Clock()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.HWSURFACE)

background = pygame.image.load('sprite/BG.png')  # Фон
sprit = pygame.image.load('sprite/1.png')  # Подвижная картинка
sprite = pygame.transform.scale(sprit, (sprit.get_width() * 3, sprit.get_height() * 3))
spaceship = pygame.image.load('sprite/ship.png')
pygame.mixer.init()
pygame.mixer.music.load("Test.mp3")
pygame.mixer.music.play()

# Начальные координаты объектов

spriteX = 474
spriteY = 614
spaceship_x = 200
spaceship_y = 300
spaceship_widht = 525
spaceship_height = 173

spaceshipScale = pygame.transform.scale(spaceship, (spaceship_widht * 3, spaceship_height * 3))

# барьерные блоки

blocks = []
block1 = pygame.Surface((12, 138))
block1.fill((255, 0, 0))
block1Rect = pygame.Rect(1409, 453, block1.get_width(), block1.get_height())
blocks.append((block1, block1Rect))
#
block2 = pygame.Surface((12, 270))
block2.fill((0, 255, 0))
block2Rect = pygame.Rect(455, 455, block2.get_width(), block2.get_height())
blocks.append((block2, block2Rect))
#
block3 = pygame.Surface((1230, 12))
block3.fill((0, 0, 255))
block3Rect = pygame.Rect(455, 717, block3.get_width(), block3.get_height())
blocks.append((block3, block3Rect))

block4 = pygame.Surface((966, 12))
block4.fill((0, 244, 255))
block4Rect = pygame.Rect(455, 453, block4.get_width(), block4.get_height())
blocks.append((block4, block4Rect))

block5 = pygame.Surface((279, 12))
block5.fill((23, 22, 55))
block5Rect = pygame.Rect(1409, 579, block5.get_width(), block5.get_height())
blocks.append((block5, block5Rect))

block6 = pygame.Surface((12, 150))
block6.fill((70, 55, 255))
block6Rect = pygame.Rect(1676, 579, block6.get_width(), block6.get_height())
blocks.append((block6, block6Rect))


def newPosition(key_pressed, spriteX, spriteY):
    # Функция пересчитывает координаты новой позиции игрока и проверяет столкновения с блоками
    global myStep
    global jumpCount
    global isJump
    pygame.display.update()
    if key_pressed[pygame.K_LEFT]:
            spriteX -= myStep
    elif key_pressed[pygame.K_RIGHT]:
            spriteX += myStep
    if not (isJump):
        if key_pressed[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                spriteY += (jumpCount ** 2) / 2
            else:
                spriteY -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 8
    return spriteX, spriteY


def collisionDetected():
    global blocks
    global spriteRectNew
    colFlag = False
    # Проверка столкновений со всеми блоками в массиве блоков
    for block in blocks:
        if spriteRectNew.colliderect(block[1]):
            collisionDir = direction
            colFlag = True
    return colFlag

def draw_Window():

    window.blit(background, (0, 0))
    window.blit(spaceshipScale, (spaceship_x, spaceship_y))

    for block in blocks:
        window.blit(block[0], (block[1].x, block[1].y))

    window.blit(sprite, (spriteRect.x, spriteRect.y))
    pygame.display.update()

# Цикл игры
MainCycle = True
while MainCycle:
    fpsClock.tick(FPS) # Частота обновления экрана
    key_pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MainCycle = False
            sys.exit()
        if key_pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            direction = pygame.key.get_pressed()
        if event.type == pygame.KEYUP:
            direction = False

    spriteRect = pygame.Rect(spriteX, spriteY, sprite.get_width(), sprite.get_height()) #Текущее место расположения игрока
    oldPos = (spriteX, spriteY) #Сохраняем старые координаты
    spriteX, spriteY = newPosition(key_pressed, spriteX, spriteY)  #Новые координаты
    spriteRectNew = pygame.Rect(spriteX, spriteY, sprite.get_width(), sprite.get_height()) #Новое место расположения картинки
    if collisionDetected():
        (spriteX, spriteY) = oldPos #Колизия

    draw_Window()# Рисуем всё на экране

pygame.quit()