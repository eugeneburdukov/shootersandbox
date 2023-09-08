import sys

import pygame
from random import randint

pygame.init()

screen_width, screen_height = 1024, 768
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Does it have any sense?")
screencolor = (248, 248, 248)

fighter_image = pygame.image.load('images/player1.png')
alcohol_image = pygame.image.load('images/alcohol.png')
killer_image = pygame.image.load('images/player2.png')

fighter_image_width, fighter_image_height = fighter_image.get_size()
alcohol_image_width, alcohol_image_height = alcohol_image.get_size()
killer_image_width, killer_image_height = killer_image.get_size()

fighter_is_moving_left, fighter_is_moving_right = False, False

fighter_x, fighter_y = screen_width / 2 - fighter_image_width / 2, screen_height - fighter_image_height
alcohol_x, alcohol_y = 0, 0
killer_x, killer_y = randint(0, screen_width - killer_image_width), 0
fighter_step = 2
alcohol_step = 5
killer_step = 0.5
alcohol_was_fired = False

while True:
    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            sys.exit()
        if x.type == pygame.KEYDOWN:
            if x.key == pygame.K_LEFT:
                fighter_is_moving_left = True
            if x.key == pygame.K_RIGHT:
                fighter_is_moving_right = True
            if x.key == pygame.K_SPACE:
                alcohol_was_fired = True
                alcohol_x = fighter_x + fighter_image_width / 2 - alcohol_image_width / 2
                alcohol_y = fighter_y - alcohol_image_height
        if x.type == pygame.KEYUP:
            if x.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if x.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    if fighter_is_moving_left and fighter_x >= fighter_step:
        fighter_x -= fighter_step

    if fighter_is_moving_right and fighter_x <= screen_width - fighter_image_width - fighter_step:
        fighter_x = fighter_x + fighter_step

    killer_y = killer_y + killer_step

    if alcohol_was_fired and alcohol_y + alcohol_image_height < 0:
        alcohol_was_fired = False

    if alcohol_was_fired:
        alcohol_y = alcohol_y - alcohol_step

    screen.fill(screencolor)
    screen.blit(fighter_image, (fighter_x, fighter_y))
    screen.blit(killer_image, (killer_x, killer_y))
    if alcohol_was_fired:
        screen.blit(alcohol_image, (alcohol_x, alcohol_y))

    if alcohol_was_fired and \
            killer_x < alcohol_x < killer_x + killer_image_width - alcohol_image_width and \
            killer_y < alcohol_y < killer_y + killer_image_height - alcohol_image_height:
        alcohol_was_fired = False
        killer_x, killer_y = randint(0, screen_width - killer_image_width), 0

    pygame.display.update()
