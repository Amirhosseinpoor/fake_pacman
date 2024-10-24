#! /usr/bin/python3
import pygame
from random import randint, choice

pygame.init()
running = True
dt = 0
pygame.display.set_caption('Fake Pacman')

screen = pygame.display.set_mode((1280, 720))
image = pygame.image.load("11060986_47784.jpeg")
image1 = pygame.image.load("7110877_1082.jpeg")
image2 = pygame.image.load("28641068_2206_w023_n003_2471b_p1_2471.jpeg")
image3 = pygame.image.load("12024166_116Z_2012.w020.n001.870B.p15.870.jpeg")
screenUpdate = pygame.transform.scale(image, (1280, 720))

clock = pygame.time.Clock()
text_time = '120'.rjust(3)
counter = 120
pygame.time.set_timer(pygame.USEREVENT, 1000)

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(f'SCORE : {score}     TIME : {counter}', True, 'green')
textRect = text.get_rect()
textRect.center = (500, 300)
textRect = text.get_rect()
congratulations = ''
congratulations_text = font.render(f'{congratulations}', True, 'red')
congratulations_Rect = congratulations_text.get_rect()
congratulations_Rect.center = (500, 300)
congratulations_Rect = congratulations_text.get_rect()

x = randint(100, 1180)
y = randint(100, 620)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
top_right = False
top_left = True
bel_right = True
bel_left = True
food_pos = pygame.Vector2(x, y)
color = "brown"

j = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            if score == 11 and j == 0:
                counter += 1
                j += 1

            if score == 25 and j == 1:
                counter += 1
                j += 1

            if score == 46 and j == 2:
                counter += 1
                j += 1

            counter -= 1
            if counter > 0:
                text_time = str(counter).rjust(3)
            else:
                running = False

        if event.type == pygame.QUIT:
            running = False
    if 10 < score <= 24:
        screenUpdate = pygame.transform.scale(image1, (1280, 720))

    if 25 <= score <= 45:
        screenUpdate = pygame.transform.scale(image2, (1280, 720))

    if 46 <= score:
        screenUpdate = pygame.transform.scale(image3, (1280, 720))

    screen.blit(screenUpdate, (0, 0))
    pygame.draw.circle(screen, color, food_pos, 20, 13)
    pygame.draw.circle(screen, "yellow", player_pos, 30, 0, top_right, top_left, bel_left, bel_right)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    if keys[pygame.K_UP]:
        player_pos.y -= 200 * dt
        top_right = False
        top_left = True
        bel_right = True
        bel_left = True

    if keys[pygame.K_DOWN]:
        player_pos.y += 200 * dt
        top_right = True
        top_left = True
        bel_right = False
        bel_left = True

    if keys[pygame.K_LEFT]:
        player_pos.x -= 200 * dt
        top_right = True
        top_left = False
        bel_right = True
        bel_left = True

    if keys[pygame.K_RIGHT]:
        player_pos.x += 200 * dt
        top_right = False
        top_left = True
        bel_right = True
        bel_left = True

    if x - 30 < player_pos[0] < x + 30 and y - 30 < player_pos[1] < y + 30:
        x = randint(100, 1180)
        y = randint(100, 620)
        score += 1
        food_pos = pygame.Vector2(x, y)
        color = choice(["chocolate4", "dark orchid1", "dark golden rod1", "deep pink2", "dark orange", "green yellow"])

    if score == 11:
        congratulations = 'oK gOOd!! bUt coNtiNuE'
        congratulations_text = font.render(f'                                                       '
                                           f'                                       '
                                           f'{congratulations}', True, 'tomato3')
        screen.blit(congratulations_text, congratulations_Rect)

    if score == 25:
        congratulations = 'GoDD LIkE!!!'
        congratulations_text = font.render(f'                                                           '
                                           f'                                               '
                                           f'{congratulations}', True, 'yellow2')
        screen.blit(congratulations_text, congratulations_Rect)

    if score == 46:
        congratulations = 'mY niGGa broH'
        congratulations_text = font.render(f'                                                      '
                                           f'                                                   '
                                           f'{congratulations}', True, 'black')
        screen.blit(congratulations_text, congratulations_Rect)

    text = font.render(f'SCORE : {score}     TIME : {counter}', True, 'azure3')
    screen.blit(text, textRect)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
