## ce programme analyse un plateau de morpion et détermine la présence d'une victoire ou d'un match nul.

def meIfVictory(mathDraw):

    def attrib(a):
        winner = 0
        if a == 15:
            return 1
        if a == 21:
            return 2
        else:
            return 0
    winner = 0
    ##lignes
    winner += attrib(sum(mathDraw[0]))
    winner += attrib(sum(mathDraw[1]))
    winner += attrib(sum(mathDraw[2]))

    ##colonnes
    winner += attrib(sum( [mathDraw[i][0] for i in range(0,3)] ))
    winner += attrib(sum( [mathDraw[i][1] for i in range(0,3)] ))
    winner += attrib(sum( [mathDraw[i][2] for i in range(0,3)] ))

    ##diagonnales
    #\ :
    winner += attrib(sum( [mathDraw[i][i] for i in range(0,3)] ))
    #/ :
    winner += attrib(sum( [mathDraw[i][2-i] for i in range(0,3)] ))


    return winner # 0 = aucun, 1 = P1, 2 = P2

if __name__ == '__main__':
    print(meIfVictory([[5,5,5],[7,0,7],[7,0,5]]))
