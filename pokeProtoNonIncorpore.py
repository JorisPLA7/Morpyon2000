## ce programme analyse un plateau de morpion et détermine la présence d'une victoire ou d'un match nul.

def meIfVictory():
    def attrib(a):
        winner = 0
        if a == 15:
            winner = 1
        if a == 21:
            winner = 2
        print(winner)

    mathDraw = [[7,5,7],[7,5,7],[7,5,7]]
    ##lignes
    attrib(sum(mathDraw[0]))
    attrib(sum(mathDraw[1]))
    attrib(sum(mathDraw[2]))

    ##colonnes
    attrib(sum( [mathDraw[i][0] for i in range(0,3)] ))
    attrib(sum( [mathDraw[i][1] for i in range(0,3)] ))
    attrib(sum( [mathDraw[i][2] for i in range(0,3)] ))

    ##diagonnales
    #\ :
    attrib(sum( [mathDraw[i][i] for i in range(0,3)] ))
    #/ :
    attrib(sum( [mathDraw[i][2-i] for i in range(0,3)] ))


    #return winner # 0 = aucun, 1 = P1, 2 = P2

if __name__ == '__main__':
    meIfVictory()
