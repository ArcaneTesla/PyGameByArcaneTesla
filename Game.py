import pygame, sys, time
FPS = 60  # кадров в сек

# Переменные
direction = False
isJump = False
iteractionFlag = False
jumpCount = 4
FPS = 60
myStep = 20
OxStatus = 100
CorpStatus = 100
ReactorStatus = 100

pygame.init()

fpsClock = pygame.time.Clock()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)

background = pygame.image.load('sprite/BG.png')  # Фон
sprit = pygame.image.load('sprite/1.png')  # Подвижная картинка
sprite = pygame.transform.scale(sprit, (sprit.get_width() * 3, sprit.get_height() * 3))
spaceship = pygame.image.load('sprite/ship.png')
HUD = pygame.image.load('sprite/HUD.png')
pygame.mixer.init()
pygame.mixer.music.load("Dreamstate Logic - Earthbound.mp3")
pygame.mixer.music.play()
pygame.font.SysFont('arial', 36)
f1 = pygame.font.Font(None, 80)
text1 = f1.render('Ничего не происходит', 1, (255, 255, 255))
CorpStatusText = f1.render(str(CorpStatus), 1, (255, 255, 255))
ReactorStatusText = f1.render(str(ReactorStatus), 1, (255, 255, 255))
quest = pygame.image.load('sprite/quest.png')
KeyStatus = False

# Начальные координаты объектов
i = 1
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
barrier1.set_alpha(1)
barrier1Rect = pygame.Rect(455, 455, barrier1.get_width(), barrier1.get_height())
barriers.append((barrier1, barrier1Rect))

barrier2 = pygame.Surface((1230, 12))
barrier2.set_alpha(1)
barrier2Rect = pygame.Rect(455, 717, barrier2.get_width(), barrier2.get_height())
barriers.append((barrier2, barrier2Rect))

barrier3 = pygame.Surface((12, 150))
barrier3.set_alpha(1)
barrier3Rect = pygame.Rect(1676, 579, barrier3.get_width(), barrier3.get_height())
barriers.append((barrier3, barrier3Rect))

interaction = pygame.Surface((96,96))
interaction.fill((255,0,0))
interactionRect = pygame.Rect(1570, 645, interaction.get_width(), interaction.get_height())

class Quest():

    def __init__(self, x, y, text, option1, option2, option3):
        self.x = x
        self.y = y
        self.text = text
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3

    '''def draw(self):
        global iteractionFlag
        if iteractionFlag == True:
            window.blit(quest, (200, 200))'''






def newPosition(key_pressed, spriteX, spriteY):
    # Функция пересчитывает координаты новой позиции игрока и проверяет столкновения с блоками
    global myStep

    if key_pressed[pygame.K_LEFT]:
            spriteX -= myStep
    elif key_pressed[pygame.K_RIGHT]:
            spriteX += myStep
    return spriteX, spriteY

'''def collisionDetected():
    global blocks
    global spriteRectNew
    colFlag = False
    # Проверка столкновений со всеми блоками в массиве блоков
    for block in blocks:
        if spriteRectNew.colliderect(block[1]):
            colFlag = True
    return colFlag'''

def draw_Window():

    global iteractionFlag

    window.blit(background, (0, 0))
    window.blit(HUD, (0, 0))
    window.blit(spaceshipScale, (spaceship_x, spaceship_y))
    window.blit(interaction, (1570, 614))
    window.blit(text1, (600, 50))
    window.blit(sprite, (spriteRect.x, spriteRect.y))
    window.blit(OxStatusText, (660, 1000))
    window.blit(CorpStatusText, (875, 1000))
    window.blit(ReactorStatusText, (1090, 1000))

    if iteractionFlag == True:
        window.blit(quest, (200, 200))

    for barrier in barriers:
        window.blit(barrier[0], (barrier[1].x, barrier[1].y))

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
            KeyStatus = event.key
        if event.type == pygame.KEYUP:
            KeyStatus = False


    spriteRect = pygame.Rect(spriteX, spriteY, sprite.get_width(), sprite.get_height()) #Текущее место расположения игрока

    oldPos = (spriteX, spriteY) #Сохраняем старые координаты

    spriteX, spriteY = newPosition(key_pressed, spriteX, spriteY)  #Новые координаты

    spriteRectNew = pygame.Rect(spriteX, spriteY, sprite.get_width(), sprite.get_height()) #Новое место расположения картинки

    for barrier in barriers:
        if spriteRectNew.colliderect(barrier[1]):
            (spriteX, spriteY) = oldPos


    if spriteRectNew.colliderect(interactionRect) and key_pressed[pygame.K_e]:
        text1 = f1.render('Красный квадрат нажат', 1, (255, 255, 255))
        i = i + 1
        print(i)
        if i % 2 == 0:
            iteractionFlag = True
        elif i % 2 != 0:
            iteractionFlag = False



    elif spriteRectNew.colliderect(interactionRect):
        text1 = f1.render('Нажмите E', 1, (255, 255, 255))
    else:
        text1 = f1.render('Ничего не происходит', 1, (255, 255, 255))



    OxStatusText = f1.render(str(OxStatus), 1, (255, 255, 255))
    if key_pressed[pygame.K_DOWN]:
        OxStatus -= 1
        if OxStatus <= 0:
            OxStatus = 0
    if key_pressed[pygame.K_UP]:
        OxStatus += 1
        if OxStatus >= 100:
            OxStatus = 100
    if OxStatus == 0:
        text1 = f1.render('Топливо закончилось Вы проиграли!', 1, (255, 255, 255))

    draw_Window()# Рисуем всё на экране

pygame.quit()