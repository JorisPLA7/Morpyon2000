import Joris2000
import poke
import random
global debug
debug = 1 ## augmente l'affichage d'infos en console, à manier avec modération .
global iterations
iterations = 50
global premier
premier = [0,5,7]

def victoire(mathDraw):
    #effectuer les sommes
    #return le numéro du gagnant sinon 0
    pass
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


class Bot():
    def __init__(self, number,iterations):
        self.iterations = iterations
        self.playerNumber = number
        if self.playerNumber == 1 : self.opponentNumber = 2
        if self.playerNumber == 2 : self.opponentNumber = 1

        self.mathVal = premier[number]

    def IA(self):
        self.liveDraw = currentGame.mathDraw
        for i in range(0,len(self.liveDraw)):
            for j in range(0,len(self.liveDraw[i])):
                if self.liveDraw[i][j]==0: #la case est libre
                    self.liveDraw[i][j]=premier[playerNumber]
                    scoreDraw[i][j] =self.montecarlo()

    def montecarlo(self):
        test=poke.meIfVictory(self.liveDraw)
        if test==playerNumber:
            score=self.iterations
            return score

        else :
            score=0
            for parties in range(0,self.iterations):
                while test==0:
                    for token in range(0,10): #paire , joueur 1 joue , impaire joueur 2
                        posx = random.randint(0,2)
                        posy = random.randint(0,2)
                        while moovePossible(posx,posy) == 0:
                            posx = random.randint(0,2)
                            posy = random.randint(0,2)
                        self.liveDraw[posx][posy]= premier[(token+self.playerNumber)%2)]
                        test = poke.meIfVictory()
                        if test == 0:
                            pass
                        if

                         while  == 0
                            pass
                        ###########################



class Human ():
    def __init__(self, number):
        premier = [0,5,7]
        self.playerNumber = number
        self.accepted = False
        self.mathVal = premier[number]

    def play(self, mathDraw, draw):
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
            print(mathDraw)
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
    player[1] = Human(1)
    player[2] = Human(2)
    #player[2] = Bot(2, 50'''iterations''')
    while 1:
        player[activePlayer].play(currentGame.mathDraw, currentGame.draw)
        activePlayer, inactivePlayer = inactivePlayer, activePlayer

if __name__ == '__main__':
    routine()
