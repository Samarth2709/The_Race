import pygame
import time

black = (0, 0, 0)
white = (255, 255, 255)
bright_blue = (25, 128, 255)
blue = (0, 0, 225)


def level5():
    pygame.init()
    game_size = (775, 230)

    gameDisplay = pygame.display.set_mode(game_size, pygame.RESIZABLE)
    pygame.display.set_caption("Impossible Game: Level 5")
    wind_size = pygame.Surface.get_size(gameDisplay)

    clock = pygame.time.Clock()

    user_obj_img = pygame.image.load('playeravatar.png')
    user_obj_img.convert_alpha()
    user_size = pygame.Surface.get_size(user_obj_img)

    game_map_img = pygame.image.load('gamemap.png')
    map_size = pygame.Surface.get_size(game_map_img)

    obsta_img = pygame.image.load('obstacle_game.png')
    if wind_size[0] / game_size[0] < wind_size[1] / game_size[1]:
        game_map_img = pygame.transform.rotozoom(game_map_img, 0, int(wind_size[0] / game_size[0]))

    elif wind_size[0] / game_size[0] >= wind_size[1] / game_size[1]:
        game_map_img = pygame.transform.rotozoom(game_map_img, 0, int(wind_size[1] / game_size[1]))

    x_change_a, x_change_d, y_change_w, y_change_s = 0, 0, 0, 0

    x_user = 20
    y_user = 56

    ob_x1 = 250
    ob_y1 = 35

    ob_x2 = 575
    ob_y2 = 80

    ob_x3 = 250
    ob_y3 = 125

    ob_x4 = 575
    ob_y4 = 170

    ob_x5 = 290
    ob_y5 = 35

    ob_x6 = 400
    ob_y6 = 35

    spawn_user = (20, 56)
    refresh_rate = 144
    move_amount = (280 / refresh_rate)
    # pygame.Surface.get_sizee() --> (width, height)
    # pygame.transform.scale(IMAGE, (width, height))
    level5.crash = False
    level5.end_game = False
    stop_move = False
    level5.retry = False
    while not level5.crash:
        wind_size = pygame.Surface.get_size(gameDisplay)
        for event in pygame.event.get():
            print(event)

            if event.type == pygame.QUIT:
                level5.crash = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    level5.crash = True
                    level5.end_game = True

                if event.key == pygame.K_w and not stop_move:
                    y_change_w = -move_amount
                if event.key == pygame.K_a and not stop_move:
                    x_change_a = -move_amount
                if event.key == pygame.K_s and not stop_move:
                    y_change_s = move_amount
                if event.key == pygame.K_d and not stop_move:
                    x_change_d = move_amount

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    x_change_a = 0
                elif event.key == pygame.K_w:
                    y_change_w = 0
                elif event.key == pygame.K_d:
                    x_change_d = 0
                elif event.key == pygame.K_s:
                    y_change_s = 0

        # BORDER LOGIC CONDITIONS FOR EACH LINE IN MAP IMG
        line1c = (x_user + x_change_a >= 18)  # ONLY ALLLOW IF RIGHT OF LINE 1
        line2c = (y_user + y_change_s + 28 <= 200)
        line3c = (x_user + x_change_d + 28 <= 600 or x_user + x_change_d >= 655) or (y_user + 28 <= 90)
        line4c = (y_user + y_change_s + 28 < 90) or (x_user + 30 <= 601 or x_user >= 655)
        line5c = (x_user + x_change_a >= 655 or x_user + x_change_a + 28 < 600) or (y_user + 28 <= 90)
        line6c = (y_user + y_change_s + 28 <= 158) or (x_user <= 654)
        line7c = (x_user + x_change_d + 28 <= 730)
        line8c = (y_user + y_change_w >= 28)
        line9c = (x_user + x_change_a > 235 or x_user + x_change_a < 110) or (y_user >= 122)
        line10c = (y_user + y_change_w >= 122) or (x_user > 235 or x_user + 28 <= 105)
        line11c = (x_user + x_change_d + 28 < 104 or x_user + x_change_d > 110) or (y_user >= 122)
        line12c = (y_user + y_change_w >= 56) or (x_user >= 115)
        # y_user + y_change_s+ 28 < pygame.Surface.get_size(gameDisplay)[1]
        if line1c and line5c and line9c:
            x_user += x_change_a
        if line3c and line7c and line11c:
            x_user += x_change_d
        if line8c and line10c and line12c:
            y_user += y_change_w
        if line2c and line4c and line6c:
            y_user += y_change_s

        # game_map_img = pygame.transform.scale(game_map_img, (wind_size[0]-20, wind_size[1]-20))
        # MOVE OBSTACLE*************(655, 90)(730, 155)
        if ob_x1 <= 250:
            forward_ob1 = True
            backward_ob1 = False
        elif ob_x1 >= 575:
            forward_ob1 = False
            backward_ob1 = True
        if ob_y5 <= 40:
            down = True
            up = False
        elif ob_y5 >= 170:
            down = False
            up = True
        if down:
            ob_y5 += move_amount
            ob_y6 += move_amount
        elif up:
            ob_y5 -= move_amount
            ob_y6 -= move_amount
        if forward_ob1:
            ob_x1 += (move_amount * 2)
            ob_x2 -= (move_amount * 2)
            ob_x3 += (move_amount * 2)
            ob_x4 -= (move_amount * 2)
        elif backward_ob1:
            ob_x1 -= (move_amount * 1.2)
            ob_x2 += (move_amount * 1.2)
            ob_x3 -= (move_amount * 1.2)
            ob_x4 += (move_amount * 1.2)
        # ***********************1.2)****

        # CHECK IF USER HITS OBSTACLE*************
        check_ob1_col = ((ob_x1 + 30 >= x_user >= ob_x1) or (ob_x1 + 30 >= x_user + 15 >= ob_x1) or (
                    ob_x1 + 30 >= x_user + 30 >= ob_x1)) and (
                                    (ob_y1 + 30 >= y_user >= ob_y1) or (ob_y1 + 30 >= y_user + 15 >= ob_y1) or (
                                        ob_y1 + 30 >= y_user + 30 >= ob_y1))
        check_ob2_col = ((ob_x2 + 30 >= x_user >= ob_x2) or (ob_x2 + 30 >= x_user + 15 >= ob_x2) or (
                    ob_x2 + 30 >= x_user + 30 >= ob_x2)) and (
                                    (ob_y2 + 30 >= y_user >= ob_y2) or (ob_y2 + 30 >= y_user + 15 >= ob_y2) or (
                                        ob_y2 + 30 >= y_user + 30 >= ob_y2))
        check_ob3_col = ((ob_x3 + 30 >= x_user >= ob_x3) or (ob_x3 + 30 >= x_user + 15 >= ob_x3) or (
                    ob_x3 + 30 >= x_user + 30 >= ob_x3)) and (
                                    (ob_y3 + 30 >= y_user >= ob_y3) or (ob_y3 + 30 >= y_user + 15 >= ob_y3) or (
                                        ob_y3 + 30 >= y_user + 30 >= ob_y3))
        check_ob4_col = ((ob_x4 + 30 >= x_user >= ob_x4) or (ob_x4 + 30 >= x_user + 15 >= ob_x4) or (
                    ob_x4 + 30 >= x_user + 30 >= ob_x4)) and (
                                    (ob_y4 + 30 >= y_user >= ob_y4) or (ob_y4 + 30 >= y_user + 15 >= ob_y4) or (
                                        ob_y4 + 30 >= y_user + 30 >= ob_y4))
        check_ob5_col = ((ob_x5 + 30 >= x_user >= ob_x5) or (ob_x5 + 30 >= x_user + 15 >= ob_x5) or (
                    ob_x5 + 30 >= x_user + 30 >= ob_x5)) and (
                                    (ob_y5 + 30 >= y_user >= ob_y5) or (ob_y5 + 30 >= y_user + 15 >= ob_y5) or (
                                        ob_y5 + 30 >= y_user + 30 >= ob_y5))
        check_ob6_col = ((ob_x6 + 30 >= x_user >= ob_x6) or (ob_x6 + 30 >= x_user + 15 >= ob_x6) or (
                    ob_x6 + 30 >= x_user + 30 >= ob_x6)) and (
                                    (ob_y6 + 30 >= y_user >= ob_y6) or (ob_y6 + 30 >= y_user + 15 >= ob_y6) or (
                                        ob_y6 + 30 >= y_user + 30 >= ob_y6))

        if check_ob1_col or check_ob2_col or check_ob3_col or check_ob4_col or check_ob5_col or check_ob6_col:
            x_user = 20
            y_user = 56  # RESETS USER POSITION BACK TO SPAWN

        # ***************************************
        # CHECK IF IN FINISH****************************
        if 730 >= x_user + 15 >= 655 and 90 <= y_user + 15 <= 155:
            stop_move = True
            gameDisplay.fill(white)
            message_display("Game Completed!", gameDisplay, game_size[0] / 2, game_size[1] / 2, 50)
            button(gameDisplay, "Retry", game_size[0] / 2+50, game_size[1] / 2 + 25, 50, 50, blue, bright_blue, cont)
            button(gameDisplay, "End Game", game_size[0] / 2 - 100, game_size[1] / 2 + 25, 100, 50, blue, bright_blue,
                   next_level)
            if level5.retry:
                stop_move = False
                x_user = 20
                y_user = 56
                level5.retry = False

            pygame.display.update()


        else:
            # ********************************************
            # DISPLAY OBJECTS****************
            gameDisplay.fill(white)
            gamemap(gameDisplay, game_map_img, 10, 10)
            user_obj(gameDisplay, user_obj_img, x_user, y_user)
            obsta(gameDisplay, obsta_img, ob_x1, ob_y1)
            obsta(gameDisplay, obsta_img, ob_x2, ob_y2)
            obsta(gameDisplay, obsta_img, ob_x3, ob_y3)
            obsta(gameDisplay, obsta_img, ob_x4, ob_y4)
            obsta(gameDisplay, obsta_img, ob_x5, ob_y5)
            obsta(gameDisplay, obsta_img, ob_x6, ob_y6)
        # ************

        pygame.display.update()
        clock.tick(refresh_rate)

    pygame.quit()


def user_obj(gameDisplay, user_obj_img, x, y):
    gameDisplay.blit(user_obj_img, (x, y))


def gamemap(gameDisplay, game_map_img, x, y):
    gameDisplay.blit(game_map_img, (x, y))


def obsta(gameDisplay, obsta_img, x, y):
    gameDisplay.blit(obsta_img, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text, gameDisplay, x, y, size_font):
    largeText = pygame.font.Font('freesansbold.ttf', size_font)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)


def cont():
    level5.retry = True


def next_level():
    level5.crash = True


def button(display, msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(display, ac, (x, y, w, h))
        if click[0] == True:
            print(click)
            action()
    else:
        pygame.draw.rect(display, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    display.blit(textSurf, textRect)


if __name__ == "__main__":
    level5()
