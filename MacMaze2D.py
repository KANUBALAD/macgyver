import pygame
import position as Position
import perso as Perso
from random import randint
from labyManager import LabyManager
from constantes import*


continuePlaying = True
gameEnded = False
win = False
pygame.init()
screen = pygame.display.set_mode((cote_fenetre, cote_fenetre))

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()


def message_display(text):
    #font = pygame.font.Font('freesansbold.ttf', 15)
    pygame.font.init()
    font = pygame.font.Font('fonts/3270Medium.ttf', 15)
    TextSurf, TextRect = text_objects(text, font)
    TextRect.center = ((cote_fenetre / 2),(cote_fenetre / 2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

def confirm_dialog(text):
    screen.fill(BLACK)
    message_display(text)
    pygame.display.update()
    isRunning = True
    answer = False
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            elif event.type == pygame.KEYDOWN:
                isRunning = False
                if event.key == pygame.K_y:
                    answer = True
    return answer

def wait_for_key_pressed():
    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            elif event.type == pygame.KEYDOWN:
                isRunning = False


def quit_game():
    screen.fill(BLACK)
    message_display("Thank you for playing Mac Maze. See you soon!")
    wait_for_key_pressed()
    screen.fill(BLACK)
    message_display("Press any key to quit.")
    wait_for_key_pressed()
    pygame.quit()


def game_loop():
    global win
    global continuePlaying
    global gameEnded
    continuePlaying = True
    win = False
    lm = LabyManager()
    lm.initializeGame()
    perso = Perso.Perso(lm.initPosition)
    lm.displayLaby(screen)
    while not (perso.pos == lm.exitPosition) and perso.alive and continuePlaying:
        lm.displayLaby(screen)
        pygame.display.set_caption("MacGyver has: " + lm.nbInGameObjets() + "/3 objects. Use arrows to move")
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuePlaying = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT :
                    perso.goLeft(lm)
                elif event.key == pygame.K_RIGHT:
                    perso.goRight(lm)
                elif event.key == pygame.K_UP:
                    perso.goUp(lm)
                elif event.key == pygame.K_DOWN:
                    perso.goDown(lm)
                elif event.key == pygame.K_ESCAPE:
                    continuePlaying = False
                    break
    win = perso.alive and perso.hasAllObjects()
    gameEnded = True

def start_game():
    global gameEnded
    gameEnded = False
    while not gameEnded:
        game_loop()
    handle_game_end()


def handle_game_end():
    global win
    global continuePlaying

    if not continuePlaying:
        confirmed = confirm_dialog("Are you sure you want to quit? (y / n)")
        if confirmed:
            quit_game()
        else:
            start_game()
    else:
        if win:
            confirmed = confirm_dialog("Congratulations! You won! Play again? (y / n)")
            if confirmed:
                start_game()
            else:
                quit_game()
        else:
            confirmed = confirm_dialog("You are dead, try again? (y / n)")
            if confirmed:
                start_game()
            else:
                quit_game()

def main():
    start_game()


if __name__ == "__main__":
    main()
