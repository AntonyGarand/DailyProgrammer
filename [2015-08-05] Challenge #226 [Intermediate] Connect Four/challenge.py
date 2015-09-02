# -*- coding: utf-8 -*-
"""
challenge.py
2015/08/31

Plays the Connect Four game
//TODO: CheckWin
X is the uppercase 
O is the lowercase
"""

class game():
    
    __grid = None
    __directions = None    
    
    def __init__(self):
        self.__grid = [[0]*6,[0]*6,[0]*6,[0]*6,[0]*6,[0]*6,[0]*6]
        self.__directions = [[1,0],[1,1],[0,1],[1,-1]]

    """
    game.move(row)
    Add a piece on the said row
    Row: a-g A-G, depending on the player
    """
    def move(self, row):
        player = str.isupper(row)
        row = ord(row)
        value = 0
        if(player):
            row = row - 65
            value = 1
        else:
            row = row - 97
            value = 2
        depth = self.findSpot(row)
        self.__grid[row][depth] = value
        coords = [row,depth]
        return self.checkWin(coords)
    """
    game.checkWin()
    Checks if the key on the [x,y] position won
    position: [x,y] int where 0<x<8 0<y<6
    """ 
    def checkWin(self, position):

        for direction in self.__directions:
            win = self.checkDirection(direction, position)
            if(win[0]):
                return win
        

        return [False]
    """
    game.checkDirection(direction, position)
    Checks if the direction and current position is winning
    direction: [x,y] direction to test
    position: [x,y] current aposition
    returns: Array
            Index 1: Is there at least 4 in a row (Win)? (Bool)
            Index 2: Player that won (X or O)
            Index 3: Cases where the player won
    """ 
    def checkDirection(self, direction, position):
        x = position[0]
        y = position[1]
        
        toX = direction[0]
        toY = direction[1]

        count = 1

        limitX = 7
        limitY = 6

        char = self.__grid[x][y]
        
        moves = [[x,y]]

        normal = True
        reverse = True
        #Checking the normal size 
        for i in range(1, 5):
            if(normal):
                newX = x + (toX * i) 
                newY = y + (toY * i)
                #Checking if we're not out of bound
                if( newX >= 0 and newY >= 0 and newX < limitX and newY < limitY): 
                    #If it it our key, add 1 to the count.
                    if( self.__grid[x + (toX * i)][y + (toY * i)]  == char):
                        count = count + 1 
                        moves.append([newX,newY])
                    #Otherwise, stop looking on this side.
                    else:
                        normal = False
                else:
                    normal = False
            #Checking the opposite side
            if(reverse):
                newX = x - (toX * i) 
                newY = y - (toY * i)
                if( ( newX >= 0) and (newY >= 0) and ( newX < limitX) and ( newY < limitY)):
                    #If it it our key, add 1 to the count.
                    if(self.__grid[newX][newY]  == char):
                        count = count + 1 
                        moves.insert(0,[newX,newY])
                    #Otherwise, stop looking on this side.
                    else:
                        reverse = False
                else:
                    reverse = False

            if (count >= 4):
                player = "X"
                if(char == 2):
                    player = "O"
                
                for i in range(len(moves)):
                    letter = chr(moves[i][1]+97)
                    pos = 5-moves[i][0]+1
                    moves[i] = letter + str(pos)


                return [True, player , " ".join(moves)] 


        return [False]
    """
    game.findSpot(row)
    Checks the top available spot on a certain row
    """
    def findSpot(self, row):
        #Checking the grid's values, stop at the first non-0 characters
        for i in range(6):
            if(self.__grid[row][i] != 0):
                return i-1
        return 5
    """
    game.printGrid()
    Prints the game grid on inversed X,Y format
    """
    def printGrid(self):
        print "   6 5 4 3 2 1"
        for i in range(7):
            joined = ' '.join(str(self.__grid[i])).replace(",   ","")[2:-2]
            print(chr(97 + i) +"  " +  joined)



input ='''D  d
D  c
C  c
C  c
G  f
F  d
F  f
D  f
A  a
E  b
E  e
B  g
G  g
B  a'''.replace("\n","  ").split("  ")

play = game()
current = 0
for i in input:
    current = current + 1
    win = play.move(i)
    play.printGrid()
    if(win[0]):
        print str(win[1]) + " won at move " + str(current/2) + "(with " + str(win[2]) + ")"
        print "Victory"
        
        break

