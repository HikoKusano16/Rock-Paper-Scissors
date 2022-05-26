import random as rd
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()

moves = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

def menu():
    with open("txtfiles\wins.txt", 'r') as f:
        global win
        win = int(f.read())
    with open("txtfiles\loss.txt", 'r') as f:
        global lose
        lose = int(f.read())
    with open("txtfiles\draws.txt", 'r') as f:
        global draw
        draw = int(f.read())
    
    def menu1():
        print('Game\nRules\nScore\nQuit\n')
        global main
        main = input('Please, type your option: ')

    menu1()
    
    global main
    if main == 'Game' or main == 'game' or main == 'G' or main == 'g':
        os.system('cls')
        play()    
    elif main == 'rules' or main == 'Rules' or main == 'R' or main == 'r':
        os.system('cls')
        input("The rules are simple. Type in a capital letter your move. The enemy will then randomly select their move.\nIf you picked the correct move, you win. Otherwise, you lose.\nHere's a list of what beats what: \nRock beats Scissors and Lizard\nPaper beats Rock and Spock\nScissors beat Paper and Lizard\nLizard beats Paper and Spock\nSpock beats Rock and Scissors\nIf you type 'Score', it will show you how many times you've won and lost. And that's about it. Good luck and enjoy :)\nPress 'Enter' to return")
        os.system('cls')
        main = None
        menu()
    elif main == 'Score' or main == 'score' or main == 'S' or main == 's':
        os.system('cls')
        print('You have', win, 'victorys, and', lose, 'losses, and', draw, 'draws.')
        clr = input("Press 'Enter' to return, or type 'Clear' to clear your score: ")
        if clr == 'Clear' or clr == 'clear':
            win = 0
            lose = 0
            draw = 0
            reg = open("txtfiles\wins.txt", "w")
            reg.write(str(win))
            reg.close()
            reg = open("txtfiles\loss.txt", "w")
            reg.write(str(lose))
            reg.close()
            reg = open("txtfiles\draws.txt", "w")
            reg.write(str(lose))
            reg.close()
            os.system('cls')
            main = None
            menu()
        else:
            os.system('cls')
            main = None
            menu()
    elif main == 'Quit' or main == 'quit' or main == 'Q' or main == 'q':
        quit()
    else:
        os.system('cls')
        print('Command was not recognized. Please try again')
        main = None
        menu()

def play():
    def start():
        global plact
        global enemact
        global draw
        plact = input("Please select your move: [R]ock, [P]aper, [S]cissors, [L]izard, Sp[O]ck: ")
        enemact = rd.choice(moves)
    
    def playon(playp, playe):
        print('You played', playp, '| The enemy played', playe)
        
    start()
    
    if plact == 'R':
        playon('Rock', enemact)
    elif plact == 'P':
        playon('Paper', enemact)
    elif plact == 'S':
        playon('Scissors', enemact)
    elif plact == 'L':
        playon('Lizard', enemact)
    elif plact == 'O':
        playon('Spock', enemact)
    else:
        os.system('cls')
        print('The move was not recognized. Please try again')
        play()
    
    def worl():
        global win
        global lose
        global draw
        if plact == 'R' and enemact == 'Rock' or plact == 'P' and enemact == 'Paper' or plact == 'S' and enemact == 'Scissors' or plact == 'L' and enemact == 'Lizard' or plact == 'O' and enemact == 'Spock':
            print(Back.BLUE + 'Draw!')
            print(Style.RESET_ALL)
            draw = draw + 1
            reg = open("txtfiles\draws.txt", "w")
            reg.write(str(draw))
            reg.close()
        if plact == 'R' and enemact == 'Scissors' or plact == 'R' and enemact == 'Lizard':
            print(Back.GREEN + 'You Won!')
            print(Style.RESET_ALL)
            win = win + 1
            reg = open("txtfiles\wins.txt", "w")
            reg.write(str(win))
            reg.close()
        elif plact == 'P' and enemact == 'Rock' or plact == 'P' and enemact == 'Spock':
            print(Back.GREEN + 'You Won!')
            print(Style.RESET_ALL)
            win = win + 1
            reg = open("txtfiles\wins.txt", "w")
            reg.write(str(win))
            reg.close()
        elif plact == 'S' and enemact == 'Paper' or plact == 'S' and enemact == 'Lizard':
            print(Back.GREEN + 'You Won!')
            print(Style.RESET_ALL)
            win = win + 1
            reg = open("txtfiles\wins.txt", "w")
            reg.write(str(win))
            reg.close()
        elif plact == 'L' and enemact == 'Paper' or plact == 'L' and enemact == 'Spock':
            print(Back.GREEN + 'You Won!')
            print(Style.RESET_ALL)
            win = win + 1
            reg = open("txtfiles\wins.txt", "w")
            reg.write(str(win))
            reg.close()
        elif plact == 'O' and enemact == 'Rock' or plact == 'O' and enemact == 'Scissors':
            print(Back.GREEN + 'You Won!')
            print(Style.RESET_ALL)
            win = win + 1
            reg = open("txtfiles\wins.txt", "w")
            reg.write(str(win))
            reg.close()
        elif plact == 'R' and enemact == 'Paper' or plact == 'R' and enemact == 'Spock':
            print(Back.RED + 'You Lost!')
            print(Style.RESET_ALL)
            lose = lose + 1
            reg = open("txtfiles\loss.txt", "w")
            reg.write(str(lose))
            reg.close()
        elif plact == 'P' and enemact == 'Scissors' or plact == 'P' and enemact == 'Lizard':
            print(Back.RED + 'You Lost!')
            print(Style.RESET_ALL)
            lose = lose + 1
            reg = open("txtfiles\loss.txt", "w")
            reg.write(str(lose))
            reg.close()
        elif plact == 'S' and enemact == 'Rock' or plact == 'S' and enemact == 'Spock':
            print(Back.RED + 'You Lost!')
            print(Style.RESET_ALL)
            lose = lose + 1
            reg = open("txtfiles\loss.txt", "w")
            reg.write(str(lose))
            reg.close()
        elif plact == 'L' and enemact == 'Rock' or plact == 'L' and enemact == 'Scissors':
            print(Back.RED + 'You Lost!')
            print(Style.RESET_ALL)
            lose = lose + 1
            reg = open("txtfiles\loss.txt", "w")
            reg.write(str(lose))
            reg.close()
        elif plact == 'O' and enemact == 'Paper' or plact == 'O' and enemact == 'Lizard':
            print(Back.RED + 'You Lost!')
            print(Style.RESET_ALL)
            lose = lose + 1
            reg = open("txtfiles\loss.txt", "w")
            reg.write(str(lose))
            reg.close()
    
    worl()
    
    trag = input('Would you like to try again? [Y/N]:\n')
    
    if trag == 'Y' or trag == 'y':
        os.system('cls')
        play()
    elif trag == 'N' or trag == 'n':
        os.system('cls')
        menu()

menu()