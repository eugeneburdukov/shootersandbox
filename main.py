import sys

import pygame
from random import randint

pygame.init()

clock = pygame.time.Clock()
text_font = pygame.font.Font('images/3997-font.otf', 70)
sound1 = pygame.mixer.Sound('images/bottle-open-14895-trim.mp3')
sound2 = pygame.mixer.Sound('images/match-sizzle-02-104778.mp3')
text_counter = "XLOP"
text_surface = text_font.render('Вымпил = ', False, 'White')
text_game_over = text_font.render("Игрок 2 не вымпил!", False, 'White')
text_game_over1 = text_font.render("Ты проиграл!", False, 'Red')
text_success1 = text_font.render("Ты победил! Началась", False, 'Green')
text_success2 = text_font.render("Чистая эмпирика!", False, 'White')

screen_width, screen_height = 1024, 774
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Does it have any sense?")
screencolor = (0, 0, 0)

back0 = pygame.image.load('images/backor0.png')
back1 = pygame.image.load('images/backor1.png')
back2 = pygame.image.load('images/backor2.png')
back3 = pygame.image.load('images/backor3.png')
back4 = pygame.image.load('images/backor4.png')
back5 = pygame.image.load('images/backor5.png')
back6 = pygame.image.load('images/backor6.png')
back7 = pygame.image.load('images/backor7.png')
back8 = pygame.image.load('images/backor8.png')
back9 = pygame.image.load('images/backor9.png')

fighter_image = pygame.image.load('images/player1.png')
alcohol_image = pygame.image.load('images/alcohol.png')
killer_image = pygame.image.load('images/player2.png')
killer1_image = pygame.image.load('images/player2_alternative.png')

counter = 0
smoke_counter = 0
image_counter = [back0, back1, back2, back3, back4, back5, back6, back7, back8, back9, back0]

fighter_image_width, fighter_image_height = fighter_image.get_size()
alcohol_image_width, alcohol_image_height = alcohol_image.get_size()
killer_image_width, killer_image_height = killer_image.get_size()
killer1_image_width, killer1_image_height = killer1_image.get_size()

fighter_is_moving_left, fighter_is_moving_right = False, False

fighter_x, fighter_y = screen_width / 2 - fighter_image_width / 2, screen_height - fighter_image_height
alcohol_x, alcohol_y = 0, 0
killer_x, killer_y = randint(0, screen_width - killer_image_width), 0
fighter_step = 5
alcohol_step = 5
killer_step = 2
alcohol_was_fired = False


player1_won = False
game_is_running = True

while game_is_running:
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

    if counter != len(image_counter) - 1:
        screen.blit(image_counter[counter], (0, 0))
    else:
        screen.blit(fighter_image, (0, 0))
        counter = 0
        smoke_counter = 0

    screen.blit(fighter_image, (fighter_x, fighter_y))

    if counter % 2:
        screen.blit(killer1_image, (killer_x, killer_y))
    else:
        screen.blit(killer_image, (killer_x, killer_y))

    if alcohol_was_fired:
        screen.blit(alcohol_image, (alcohol_x, alcohol_y))

    if alcohol_was_fired and \
            killer_x < alcohol_x < killer_x + killer_image_width - alcohol_image_width and \
            killer_y < alcohol_y < killer_y + killer_image_height - alcohol_image_height:
        alcohol_was_fired = False
        killer_x, killer_y = randint(0, screen_width - killer_image_width), 0
        counter = counter + 1
        smoke_counter = smoke_counter + 1
        sound1.play()

    if counter == len(image_counter) - 1:
        player1_won = True
        game_is_running = False

    if counter % 2:
        text_surface = text_font.render('Вымпил! = ' + str(counter) + " и закурил " + str(smoke_counter), False,
                                        'White')
        # print(smoke_counter)
        # sound2.play()
    else:
        text_surface = text_font.render('Вымпил! = ' + str(counter), False, 'White')
        # sound1.play()

    screen.blit(text_surface, (10, screen_height / 200))
    pygame.display.update()

    if killer_y + killer_image_height > fighter_y:
        game_is_running = False
    clock.tick(60)


if player1_won:
    screen.blit(text_success1, (70, 100))
    screen.blit(text_success2, (150, 200))
    pygame.display.update()
    pygame.time.wait(5000)
    pygame.quit()

else:
    screen.blit(text_game_over1, (150, 100))
    screen.blit(text_game_over, (150, 200))
    pygame.display.update()
    pygame.time.wait(5000)
    pygame.quit()