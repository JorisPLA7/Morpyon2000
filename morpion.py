import Joris2000
import poke
import random
global debug
debug = 1 ## augmente l'affichage d'infos en console, à manier avec modération .
global premier
premier = [0,5,7]

class Game():
    def __init__(self):
        self.draw = [[emptyChar for n in range (3)] for m in range (3)]
        self.mathDraw = [[0 for n in range (0,3)] for m in range (0,3)]
        self.activePlayer = 1
        self.inactivePlayer = 2

    def movePossible(self, place):
        print(place)
        
        if (not place == (99,99)) and self.draw[place[0]][place[1]] != emptyChar:
            return False
        if place[0] >2 or place[0] <0 or place[1] >2 or place[1] <0 :
            return False
        else :
            return True
        

    def finish(self, mathPlayerVal, move):
        self.draw[move[0]][move[1]] = playerChar[activePlayer]
        self.mathDraw[move[0]][move[1]] = mathPlayerVal
        results = poke.me(self.mathDraw)
        if results > 0:
            print('PAY ATTENTION ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !')
            if results == 1:
                print('player 1 win the game !')
            if results == 2:
                print('player 2 win the game !')


class AI():
    def __init__(self, playerNumber, iterations):
        
        self.playerNumber = playerNumber
        self.place =[0,0]
        if self.playerNumber == 1: self.opponentNumber = 2
        else : self.opponentNumber = 1
        
        self.iterations = iterations    
    def movePossible(self):
        
        if self.liveDraw[self.place[0]][self.place[1]] != 0 :
            return False
        elif self.place[0] >2 or self.place[0] <0 or self.place[1] >2 or self.place[1] <0 :
            return False
        else :
            return True
    
    def play(self, mathDraw, osefDraw):
        self.liveDraw = mathDraw ############## attention on devrait plutot l'appeler liveMathDraw
        issou = 0
        self.scoreDraw = [[0 for issou in range(len(self.liveDraw))] for j in range(len(self.liveDraw[issou]))]
        
        for i in range(3):
            for j in range(3):
                self.place =[i,j]
                self.liveDraw = mathDraw
                if True: #la case est libre
                    
                    self.liveDraw[i][j]= premier[self.playerNumber]
                    self.scoreDraw[i][j] = self.montecarlo()
        
        scoremax=-self.iterations**2
        for cx in range(3):
            for cj in range(3):
                if self.scoreDraw[cx][cj] > scoremax and currentGame.mathDraw[cx][cj]==0:
                    scoremax = self.scoreDraw[cx][cj]
                  
                    self.place =[cx,cj]
        print(self.scoreDraw) 
        currentGame.finish(premier[self.playerNumber], self.place)

                
                
                
    def montecarlo(self):
        test=poke.me(self.liveDraw)
        if test== self.playerNumber:
            score=self.iterations
            return score
        
        else :
            score=1
            for parties in range(self.iterations):
                tour  = self.playerNumber #avec le +1 le joueur opposant commencera
                compt_tour=1              
                while poke.me(self.liveDraw)==0:
                    compt_tour+=1  
                    stack = 0
                    for i in self.liveDraw : stack += i.count(0) # on décompte les cases vides 
                    if stack == 0:
                        break #on break si le draw est plein .
                    self.place=[random.randint(0,2),random.randint(0,2)]
                    
                    while self.movePossible()== False :
                        
                        self.place=[random.randint(0,2),random.randint(0,2)]
                    self.liveDraw[self.place[0]][self.place[1]] = premier[tour%2+1] #on fait jouer le joueur selon le numéro de tour mod2 soit en alternance 1 ou 2
                    tour+=1#on change de joueur
                        
                if poke.me(self.liveDraw)==self.playerNumber :
                    score += 1/compt_tour
                elif poke.me(self.liveDraw)==self.opponentNumber : 
                    score= score+1
                else :
                    score=-1
            
            return score
        
        


class Human ():
    def __init__(self, number):
        premier = [0,5,7]
        self.playerNumber = number
        self.accepted = False
        self.mathVal = premier[number]

    def play(self, mathDraw, draw):
        
        if True: #poinx python attribué à Matéo
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
                move = self.inputToCoord(input('press a number from 1 to 9 to play.  '))
                self.accepted = currentGame.movePossible(move)

        currentGame.finish(self.mathVal, move)
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
    player[2] = AI(2, 700)
    while 1:
        print("It's player{}'s Turn :".format(activePlayer))

        player[activePlayer].play(currentGame.mathDraw, currentGame.draw)
        for i in range(3):
            for j in range(3):
                currentGame.mathDraw[i][j] = premier[playerChar.index(currentGame.draw[i][j])]
        activePlayer, inactivePlayer = inactivePlayer, activePlayer

if __name__ == '__main__':
    routine()
