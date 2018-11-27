import pygame
import position as Position
import perso as Perso
from random import randint
from labyManager import LabyManager
from constantes import*

"""laby mean maze, as we have to know"""
"""declared outside of main () because used in methods"""
continuePlaying = True
gameEnded = False
win = False
pygame.init()
screen = pygame.display.set_mode((cote_fenetre, cote_fenetre))

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE) 
    """text and color of the font"""
    """to declare his location after"""
    return textSurface, textSurface.get_rect() 
    


def message_display(text):
    """font = pygame.font.Font('freesansbold.ttf', 15)"""
    pygame.font.init() 
    """initialize (inside the methode) the font module"""
    font = pygame.font.Font('fonts/3270Medium.ttf', 15) 
    """creation of a fonte"""
    TextSurf, TextRect = text_objects(text, font)
    """TextSurf, TextRect = font.render(text, True, WHITE),textSurface.get_rect()"""
    TextRect.center = ((cote_fenetre / 2),(cote_fenetre / 2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

def confirm_dialog(text):
    screen.fill(BLACK)   
    message_display(text)  
    """displayed message, text as parameter"""  
    pygame.display.update() 
    """update of the whole screen as there is no parameter"""
    isRunning = True 
    """infinite loop : only yes to quit her"""
    answer = False
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            elif event.type == pygame.KEYDOWN:
                isRunning = False
                """Answer determine the start() or quit() in handle_game_end()"""
                if event.key == pygame.K_y:
                    answer = True
                    """1 funct° (inspite of 2 to manage 2 no) : yes as pivot value."""
    return answer 
    

def wait_for_key_pressed():
    """infinite loop : only to quit her => quit or any keydown"""
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
    """global : variables will also be understood outside the method"""
    global win
    global continuePlaying
    global gameEnded
    continuePlaying = True
    win = False
    """instance "lm" has attributes and instance methods conferred by the class"""
    lm = LabyManager() 
    lm.initializeGame()
    perso = Perso.Perso(lm.initPosition)
    """.txt changed by pictures, each location of 1*30 size (15 locati° : sprites)"""
    lm.displayLaby(screen)
    """Exit loop if perso on exitPos °, alive and with desire to play"""
    while not (perso.pos == lm.exitPosition) and perso.alive and continuePlaying:
        """Reloading after moving .txt dc images on locations"""
        lm.displayLaby(screen)
        """Title and counter (updated via the movement loop) of recovered objects"""
        pygame.display.set_caption("MacGyver have: " + lm.nbInGameObjets() + "/3 objects. Use arrows to move")
        """Update (re-loading images) in the pygame display"""
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                """Quit Generates Loop Output with Will to Quit"""
                continuePlaying = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT :
                    """classic movement command of perso, instance lm passed in parameter"""
                    perso.goLeft(lm)
                    """displacement method as a consequence of the movement"""
                elif event.key == pygame.K_RIGHT:
                    perso.goRight(lm)
                elif event.key == pygame.K_UP:
                    perso.goUp(lm)
                elif event.key == pygame.K_DOWN:
                    perso.goDown(lm)
                elif event.key == pygame.K_ESCAPE:
                    """Escape generates Loop Output with Will to Quit"""
                    continuePlaying = False
                    break
        """Values ​​returned if break"""
        """Otherwise returned if (exitPos ° + alive) or if (Death due to combat without objects)"""
    win = perso.alive #and perso.hasAllObjects()
    gameEnded = True

def start_game():
    global gameEnded
    gameEnded = False
    while not gameEnded:
        """directional method that also returns values ​​of win and gameEnded"""
        game_loop()
    handle_game_end()


def handle_game_end():
    """Have the output values ​​of the game_loop () thanks to the global"""
    global win
    global continuePlaying
    """if want stop i.e. quit or escape pressed in game_loop"""
    if not continuePlaying:
        confirmed = confirm_dialog("Are you sure you want to quit? (y / n)")
        if confirmed:
            quit_game() #with Yes pressed (yes as "pivot value")
        else:
            start_game() #with quit or any keydown**
       
            """Otherwise play = True, so test of win (so alive with the objects)"""     
    else:       
        if win:
            confirmed = confirm_dialog("Congratulations! You won! Play again? (y / n)")
            if confirmed:
                start_game() #with Yes pressed (yes as "pivot value")
            else:
                quit_game() #with quit or any keydown**
            
            """Otherwise, perso.alive = False i.e. lost guardian confrontation"""
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
