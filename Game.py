import pygame, sys, time
FPS = 60  # кадров в сек

# Переменные
direction = False
isJump = False
jumpCount = 4
FPS = 60
myStep = 10

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

barriers = []

barrier1 = pygame.Surface((12, 270))
barrier1.fill((0, 0, 0))
barrier1Rect = pygame.Rect(455, 455, barrier1.get_width(), barrier1.get_height())
barriers.append((barrier1, barrier1Rect))

barrier2 = pygame.Surface((1230, 12))
barrier2.fill((0, 0, 0))
barrier2Rect = pygame.Rect(455, 717, barrier2.get_width(), barrier2.get_height())
barriers.append((barrier2, barrier2Rect))

barrier3 = pygame.Surface((12, 150))
barrier3.fill((0, 0, 0))
barrier3Rect = pygame.Rect(1676, 579, barrier3.get_width(), barrier3.get_height())
barriers.append((barrier3, barrier3Rect))


def newPosition(key_pressed, spriteX, spriteY):
    # Функция пересчитывает координаты новой позиции игрока и проверяет столкновения с блоками
    global myStep
    global isJump
    global jumpCount

    if key_pressed[pygame.K_LEFT]:
            spriteX -= myStep
    elif key_pressed[pygame.K_RIGHT]:
            spriteX += myStep
    return spriteX, spriteY

def collisionDetected():
    global blocks
    global spriteRectNew
    colFlag = False
    # Проверка столкновений со всеми блоками в массиве блоков
    for block in blocks:
        if spriteRectNew.colliderect(block[1]):

            colFlag = True
    return colFlag

def draw_Window():

    window.blit(background, (0, 0))
    window.blit(spaceshipScale, (spaceship_x, spaceship_y))

    for barrier in barriers:
        window.blit(barrier[0], (barrier[1].x, barrier[1].y))

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


    spriteRect = pygame.Rect(spriteX, spriteY, sprite.get_width(), sprite.get_height()) #Текущее место расположения игрока

    oldPos = (spriteX, spriteY) #Сохраняем старые координаты

    spriteX, spriteY = newPosition(key_pressed, spriteX, spriteY)  #Новые координаты

    spriteRectNew = pygame.Rect(spriteX, spriteY, sprite.get_width(), sprite.get_height()) #Новое место расположения картинки

    for barrier in barriers:
        if spriteRectNew.colliderect(barrier[1]):
            (spriteX, spriteY) = oldPos
            print('Колизия')#Колизия

    draw_Window()# Рисуем всё на экране

pygame.quit()