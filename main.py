from operator import le
import pygame, sys
from settings import *
from button import Button
from tiles import Tile
from level import Level
from game_data import level_0


pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background2.jpg")
BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def win():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("Congrats", True, "White")
        PLAY_TEXT1 = get_font(45).render("You've completed", True, "White")
        PLAY_TEXT2 = get_font(45).render("STORE RIDER", True, "Red")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
        PLAY_RECT1 = PLAY_TEXT.get_rect(center=(440, 260))
        PLAY_RECT2 = PLAY_TEXT.get_rect(center=(570, 360))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)
        SCREEN.blit(PLAY_TEXT2, PLAY_RECT2)

        PLAY_BACK = Button(
            image=None,
            pos=(640, 460),
            text_input="BACK",
            font=get_font(75),
            base_color="White",
            hovering_color="Green",
        )

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def death():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("red")

        PLAY_TEXT = get_font(45).render("You've DIED", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))

        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(
            image=None,
            pos=(640, 460),
            text_input="BACK",
            font=get_font(75),
            base_color="White",
            hovering_color="Green",
        )

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def play():
    clock = pygame.time.Clock()
    level = Level(level_0, SCREEN)
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill((33, 11, 7))
        level.run()
        if level.win or level.death:
            break

        pygame.display.update()
        clock.tick(60)
    if level.win:
        win()
    elif level.death:
        death()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("STORE RIDER", True, "#5BCA2B")
        MENU_RECT = MENU_TEXT.get_rect(center=(600, 100))

        PLAY_BUTTON = Button(
            image=pygame.image.load("assets/Play Rect.png"),
            pos=(600, 400),
            text_input="PLAY",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        QUIT_BUTTON = Button(
            image=pygame.image.load("assets/Quit Rect.png"),
            pos=(600, 550),
            text_input="QUIT",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
