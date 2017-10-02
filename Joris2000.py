
def __init__(self, number):
    self.playerNumber = number
    premier = [0,5,7]
    self.accepted = False
    self.mathVal = premier[number]

def think(self, mathDraw):
    self.startingMathDraw = mathDraw
    self.startingDraw = draw

def tryHard(self, liveDraw):
    self.liveDraw = liveDraw
    fini = 0
    for x in range (0,3):
        for y in range (0,3):
            if currentGame.moovePossible((x,y)):
                self.liveDraw[x][y] = premier[self.playerNumber]
                results = poke.meIfVictory(liveDraw)
                posibilitiesMap[x,y] +=1
                if results != 0 :
                    if results != self.playerNumber:
                        hotMap[x,y] -=1
                    if results == self.playerNumber:
                        hotMap[x,y] +=1

                if results == 0 :
                    self.tryHard(livedraw)
    print(hotMap)
    print(posibilitiesMap)





if __name__ == '__main__':
    import poke
    myAI = AI(1)
    myAI.tryHard([[7,5,7],[7,7,5],[5,0,0]])

#a = [[5,5,5],[7,0,7],[7,0,5]]
