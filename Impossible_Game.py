from Levels import pylevel1, pylevel2, pylevel3, pylevel4, pylevel5
import pygame


def main():
    pygame.init()
    game_size = (775, 230)
    refresh_rate = 60
    gameMenu = pygame.display.set_mode(game_size, pygame.RESIZABLE)
    pygame.display.set_caption("Impossible Game: Menu")
    clock = pygame.time.Clock()

    main.quit = False
    quit_game = False
    while not main.quit:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                main.quit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game = True
                    main.quit = True
        gameMenu.fill(white)
        message_display("The Impossible Game", gameMenu, game_size[0] / 2, (game_size[1] / 2) - 25, 50)
        button(gameMenu, "Play", game_size[0] / 2-40, (game_size[1] / 2) + 15, 80, 50, bright_blue, blue)
        pygame.display.update()
        clock.tick(refresh_rate)
    pygame.quit()
    if not quit_game:
        pylevel1.level1()
        if not pylevel1.level1.end_game:
            pylevel2.level2()
            if not pylevel2.level2.end_game:
                pylevel3.level3()
                if not pylevel3.level3.end_game:
                    pylevel4.level4()
                    if not pylevel4.level4.end_game:
                        pylevel5.level5()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text, gameDisplay, x, y, size_font):
    largeText = pygame.font.Font('freesansbold.ttf', size_font)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)


def button(display, msg, x, y, w, h, ic, ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(display, ac, (x, y, w, h))
        if click[0] == True:
            print(click)
            main.quit = True
    else:
        pygame.draw.rect(display, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    display.blit(textSurf, textRect)


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
bright_blue = (25, 128, 255)
blue = (0, 0, 225)

if __name__ == "__main__":
    main()
