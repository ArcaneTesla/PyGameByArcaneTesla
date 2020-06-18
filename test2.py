while MainCycle:

spriteRect = pygame.Rect(spriteX, spriteY, sprite.get_width(),
                         sprite.get_height())  # Текущее место расположения игрока

oldPos = (spriteX, spriteY)  # Сохраняем старые координаты

spriteX, spriteY = newPosition(key_pressed, spriteX, spriteY)  # Новые координаты

spriteRectNew = pygame.Rect(spriteX, spriteY, sprite.get_width(),
                            sprite.get_height())  # Новое место расположения картинки

    for barrier in barriers:
        if spriteRectNew.colliderect(barrier[1]):
            (spriteX, spriteY) = oldPos

#блоки для взаимодействий
interactions = []
interaction1 = pygame.image.load('sprite/Chair_active.png').convert()
interaction1Rect = pygame.Rect(1570, 645, interaction1.get_width(), interaction1.get_height())
interactions.append((interaction1, interaction1Rect))

    for interaction in interactions:
        if spriteRectNew.colliderect(interaction[1]) and key_pressed[pygame.K_e]:
            ###Что-то должно выполняться###
