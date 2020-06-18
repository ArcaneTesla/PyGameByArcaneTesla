import pygame, sys, random
FPS = 60  # кадров в сек

pygame.init()

#Переменные для сокращения кода
fpsClock = pygame.time.Clock()


window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)

# Переменные движения
direction = False
iteractionFlag = False
myStep = 20

#Игровые Переменные
FPS = 60
OxStatus = 100
CorpStatus = 100
ReactorStatus = 100
remcompl = 3
frametime = 0
background_alpha = 255
BackAnim = True

#Переменные спрайтов
background = pygame.image.load('sprite/BG.png').convert()
background2 = pygame.image.load('sprite/BG2.png').convert()
sprite = pygame.image.load('sprite/1.png').convert()  # Подвижная картинка
spaceship = pygame.image.load('sprite/ship.png').convert()
HUD = pygame.image.load('sprite/HUD.png').convert()
icon = pygame.image.load('icon.png').convert()
quest = pygame.image.load('sprite/quest.png').convert()
flame = pygame.image.load('sprite/Flame.png').convert()
flame2 = pygame.image.load('sprite/Flame2.png').convert()

#Музыка и звуки
pygame.mixer.init()
pygame.mixer.music.load("Dreamstate Logic - Earthbound.mp3")
pygame.mixer.music.play()

#Игровой Текст
pygame.font.SysFont('arial', 14)
f1 = pygame.font.Font(None, 48)
f2 = pygame.font.Font(None, 82)
text1 = f1.render('Ничего не происходит', 1, (255, 255, 255))
KeyStatus = False

# Начальные координаты объектов
i = 1
spriteX = 474
spriteY = 615
spaceship_x = 200
spaceship_y = 300

# барьерные блоки
barriers = []

barrier1 = pygame.Surface((12, 270))
barrier1.set_alpha(1)
barrier1Rect = pygame.Rect(455, 455, barrier1.get_width(), barrier1.get_height())
barriers.append((barrier1, barrier1Rect))

barrier2 = pygame.Surface((12, 150))
barrier2.set_alpha(1)
barrier2Rect = pygame.Rect(1676, 579, barrier2.get_width(), barrier2.get_height())
barriers.append((barrier2, barrier2Rect))

#блоки для взаимодействий
interaction = pygame.image.load('sprite/Chair_active.png').convert()
interactionRect = pygame.Rect(1570, 645, interaction.get_width(), interaction.get_height())

questtextlist = ["Текст плохого события1", "Текст плохого события2", "Текст плохого события3", "Текст нейтрального события", "Текст хорошего события1", "Текст хорошего события2", "Текст хорошего события3", "Текст события дозаправки"]

#Функция проверяет новую позицию
def newPosition(key_pressed, spriteX, spriteY):
    global myStep

    if key_pressed[pygame.K_LEFT]:
            spriteX -= myStep
    elif key_pressed[pygame.K_RIGHT]:
            spriteX += myStep
    return spriteX, spriteY

#функция отрисовки
def draw_Window():

    global iteractionFlag
    global key_pressed
    global OxStatusText
    global frametime
    global background_alpha
    global BackAnim
    global questtext

    if BackAnim == True:
        background_alpha -= 5
        if background_alpha <= 100:
            BackAnim = False
    elif BackAnim == False:
        background_alpha += 5
        if background_alpha >= 255:
            BackAnim = True

    background.set_alpha(background_alpha)
    window.blit(background2, (0, 0))
    window.blit(background, (0, 0))
    window.blit(HUD, (0, 0))
    window.blit(spaceship, (spaceship_x, spaceship_y))
    window.blit(text1, (20, 900))

    if spriteRectNew.colliderect(interactionRect):
        window.blit(interaction, (1574, 642))

    window.blit(sprite, (spriteRect.x, spriteRect.y))
    window.blit(OxStatusText, (660, 1000))
    window.blit(CorpStatusText, (875, 1000))
    window.blit(ReactorStatusText, (1090, 1000))
    window.blit(remcomplText, (20,20))

    if BackAnim == False:
        window.blit(flame2, (173, 450))
        window.blit(flame2, (173, 600))
    else:
        window.blit(flame, (176, 450))
        window.blit(flame, (176, 600))

    if iteractionFlag == True:
        window.blit(quest, (200, 200))
        window.blit(questtext, (220, 220))

    pygame.display.set_icon(icon)
    pygame.display.update()

# Цикл игры
MainCycle = True

while MainCycle:
    fpsClock.tick(30) # Частота обновления экрана
    key_pressed = pygame.key.get_pressed()

    spriteRect = pygame.Rect(spriteX, spriteY, sprite.get_width(), sprite.get_height()) #Текущее место расположения игрока
    oldPos = (spriteX, spriteY) #Сохраняем старые координаты
    spriteX, spriteY = newPosition(key_pressed, spriteX, spriteY)  #Новые координаты
    spriteRectNew = pygame.Rect(spriteX, spriteY, sprite.get_width(), sprite.get_height()) #Новое место расположения картинки

    CorpStatusText = f2.render(str(CorpStatus), 1, (255, 255, 255))
    ReactorStatusText = f2.render(str(ReactorStatus), 1, (255, 255, 255))
    OxStatusText = f2.render(str(OxStatus), 1, (255, 255, 255))
    remcomplText = f2.render(str(remcompl), 1, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MainCycle = False
            sys.exit()
        if key_pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        if spriteRectNew.colliderect(interactionRect) and key_pressed[pygame.K_e]:
            questrandom = random.choice(questtextlist)
            questtext = f1.render(questrandom, 1, (255, 255, 255))
            iteractionFlag = True
            OxStatus -= 5
            if questrandom == questtextlist[5]:
                OxStatus = 100
            if questrandom in questtextlist[0:3]:
                ReactorStatus -= 10
                CorpStatus -= 10
            if questrandom in questtextlist[4:7]:
                CorpStatus += 5
                ReactorStatus += 5

        if key_pressed[pygame.K_h] and remcompl > 0:
            remcompl -= 1
            ReactorStatus = 100
            CorpStatus = 100

    for barrier in barriers:
        if spriteRectNew.colliderect(barrier[1]):
            (spriteX, spriteY) = oldPos


    if spriteRectNew.colliderect(interactionRect) and key_pressed[pygame.K_q]:
        iteractionFlag = False
    elif spriteRectNew.colliderect(interactionRect) and iteractionFlag == True:
        text1 = f1.render('Нажмите Q чтобы выйти', 1, (255, 255, 255))
    elif spriteRectNew.colliderect(interactionRect):
        text1 = f1.render('Нажмите E', 1, (255, 255, 255))
    else:
        text1 = f1.render(' ', 1, (255, 255, 255))

    if OxStatus <= 0:
        text1 = f1.render('Топливо закончилось Вы проиграли!', 1, (255, 255, 255))
    if CorpStatus <= 0:
        text1 = f1.render('Нарушена целостность корпуса Вы проиграли!', 1, (255, 255, 255))
    if ReactorStatus <= 0:
        text1 = f1.render('Система жизниобспечения вышла из строя Вы проиграли!', 1, (255, 255, 255))

    draw_Window()# Рисуем всё на экране

pygame.quit()