import Joris2000
import poke
global debug
debug = 0 ## augmente l'affichage d'infos en console, à manier avec modération .


class Game():
    def __init__(self):
        self.draw = [[emptyChar for n in range (0,3)] for n in range (0,3)]
        self.mathDraw = [[0 for n in range (0,3)] for n in range (0,3)]
        self.activePlayer = 1
        self.inactivePlayer = 2

    def moovePossible(self,place):
        if self.draw[place[0]][place[1]] != emptyChar:
            return False
        if place[0] >2 or place[0] <0 or place[1] >2 or place[1] <0 :
            return False
        else :
            return True

    def finish(self, mathPlayerVal, moove):
        self.draw[moove[0]][moove[1]] = playerChar[activePlayer]
        self.mathDraw[moove[0]][moove[1]] = mathPlayerVal
        results = poke.meIfVictory(self.mathDraw)
        if results > 0:
            print('PAY ATTENTION ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !')
            if results == 1:
                print('player 1 win the game !')
            if results == 2:
                print('player 2 win the game !')
class Player ():
    def __init__(self, number, controller):
        premier = [0,5,7]
        self.playerNumber = number
        self.controller = controller
        self.accepted = False
        self.mathVal = premier[number]

    def play(self, mathDraw, draw):
        if self.controller == 'AI':
            pass
        if self.controller == 'human':
            print("It's player{}'s Turn :".format(self.playerNumber))
            print('{}|{}|{}'.format(draw[0][0],draw[1][0],draw[2][0]))
            print('-----')
            print('{}|{}|{}'.format(draw[0][1],draw[1][1],draw[2][1]))
            print('-----')
            print('{}|{}|{}'.format(draw[0][2],draw[1][2],draw[2][2]))
            if debug :
                print("visible /\ , mathématique \/")
                print('{}|{}|{}'.format(mathDraw[0][0],mathDraw[1][0],mathDraw[2][0]))
                print('-----')
                print('{}|{}|{}'.format(mathDraw[0][1],mathDraw[1][1],mathDraw[2][1]))
                print('-----')
                print('{}|{}|{}'.format(mathDraw[0][2],mathDraw[1][2],mathDraw[2][2]))


            while not self.accepted:
                moove = self.inputToCoord(input('press a number from 1 to 9 to play.  '))
                self.accepted = currentGame.moovePossible(moove)
            currentGame.finish(self.mathVal, moove)
            self.accepted = False


    def inputToCoord(self, inputNumber):
        if inputNumber == '1' : return (0,2)
        if inputNumber == '2' : return (1,2)
        if inputNumber == '3' : return (2,2)
        if inputNumber == '4' : return (0,1)
        if inputNumber == '5' : return (1,1)
        if inputNumber == '6' : return (2,1)
        if inputNumber == '7' : return (0,0)
        if inputNumber == '8' : return (1,0)
        if inputNumber == '9' : return (2,0)
        else: return (99,99)

def routine():
    global emptyChar
    global activePlayer
    global inactivePlayer
    global currentGame
    global playerChar
    global player
    activePlayer = 1
    inactivePlayer = 2
    emptyChar = ' '
    playerChar = [' ','X','O']
    currentGame = Game()
    player = {}
    player[1] = Player(1, 'human')
    player[2] = Player(2, 'human')
    while 1:
        player[activePlayer].play(currentGame.mathDraw, currentGame.draw)
        activePlayer, inactivePlayer = inactivePlayer, activePlayer

if __name__ == '__main__':
    routine()
