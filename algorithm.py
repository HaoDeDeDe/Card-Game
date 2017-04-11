import numpy as np

currentValue = np.zeros((27,27))
continueOrNot = np.zeros((27, 27))

'''
Function name: EValueofGame
Parameters: None
Function usage: Prints and returns the expected value of the game before drawing the first card. Also generates 3 matrices.
                If currently there are C black cards and D red cards facing down,
                then restValue[C,D] gives the expected gain from the rest of the game,
                     currentValue[C,D] gives the current expected value of the game,
                     continueOrNot[C,D] shows whether the player should continue drawing cards or not
'''
def EValueofGame():

    currentValue[0,0] = 0
    continueOrNot[0,0] = np.argmax([0,0])

    # C = number of black cards facing down; D = number of red cards facing down
    # k = C + D
    for k in range(1, 53):
        if k <= 26:
            for C in range(k+1):
                D = k - C
                black = 0
                red = 0
                if C > 0:
                    black = currentValue[C-1, D]
                if D > 0:
                    red = currentValue[C, D-1]
                C = float(C)
                D = float(D)
                valueIfPlay = C/(C+D)*(black) + D/(C+D)*(red)
                C = int(C)
                D = int(D)
                valueNotPlay = (D-C)/1
                if valueNotPlay-valueIfPlay >= 0:
                    currentValue[C, D] = valueNotPlay
                    continueOrNot[C, D] = 0
                else:
                    currentValue[C, D] = valueIfPlay
                    continueOrNot[C, D] = 1
        else:
            for C in range(k-26, 27):
                D = k - C
                black = 0
                red = 0
                if C > 0:
                    black = currentValue[C - 1, D]
                if D > 0:
                    red = currentValue[C, D - 1]
                C = float(C)
                D = float(D)
                valueIfPlay = C / (C + D) * (black) + D / (C + D) * (red)
                C = int(C)
                D = int(D)
                valueNotPlay = (D - C)/1
                if valueNotPlay - valueIfPlay >= 0:
                    currentValue[C,D] = valueNotPlay
                    continueOrNot[C, D] = 0
                else:
                    currentValue[C,D] = valueIfPlay
                    continueOrNot[C, D] = 1

    print("\nThe expected value of the game before drawing the first card is: %0.5f" % (currentValue[26,26]) )
    return(currentValue[26,26])



'''
Function name: stateAndPolicy
Parameters: X = the number of cards in hand
            Y = the number of black cards in hand
Function usage: Prints the current expected value of the game and whether the players should continue drawing cards,
                given that the players has X cards in hand, of which Y are black
'''
def stateAndPolicy(X, Y):
    C = 26 - Y
    D = 26 - (X-Y)
    print("\nThe current expected value of the game is: %0.5f" % (currentValue[C, D]) )
    if continueOrNot[C,D] == 1:
        print("\nPlease continue drawing cards")
    else:
        print("\nPlease stop drawing cards")


if __name__ =='__main__':
    EValueofGame()
    X = 48
    Y = 23
    stateAndPolicy(X,Y)