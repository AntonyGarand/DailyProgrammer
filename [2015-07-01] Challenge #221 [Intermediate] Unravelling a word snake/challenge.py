# challenge.py
# 2015-09-03

class wordSnake:
    __input = None
    __words = None
    #Format: X,Y
    __length = None

    # __init__
    # Creates a new wordSnake with an input (Grid)
    # inpt: Array of lines containing spaces and letter.
    # INPT must be Square or it will crash. 
    def __init__(self, inpt):
        self.__input= inpt
        self.__length = [len(self.__input[0]), len(self.__input)]
        self.__words = []

    # findAndDeleteWord
    # Finds the next word from a starting points, and deletes it while advancing.
    # coordStart: [X,Y] coordinates of the first letter of a word. 
    def findAndDeleteWord(self, coordStart):
        #Direction: [X,Y]
        direction = [0,-1]
        X = coordStart[0]
        Y = coordStart[1]
        letters = [self.__input[Y][X]]
        
        copy = list(self.__input[Y])
        copy[X] = " "
        self.__input[Y] = "".join(copy)

        #Finding direction
        if(X + 1 < self.__length[0] and self.__input[Y][X+1] != " "):
            direction = [1,0]
            
        elif(Y + 1 < self.__length[1] and self.__input[Y+1][X] != " "):
            direction = [0,1]
        elif(X - 1 >= 0 and self.__input[Y][X-1] != " "):
            direction = [-1,0]

        #Looping though the word, deleting its previous characters
        while(True):
            #Checking if we're still in range
            if(direction[0] + X < self.__length[0] and direction[0] + 1 >= 0 and direction[1] + Y < self.__length[1] and direction[1] + 1 >= 0):
                char = self.__input[Y+direction[1]][X+direction[0]] 
                #Checking if the next character is valid
                if(char == " "):
                    break
                #Adding the next char
                letters.append(char);
                X = direction[0] + X
                Y = direction[1] + Y
                #If the next char is not out of bound
                if(direction[0] + X < self.__length[0] and direction[0] + 1 >= 0 and direction[1] + Y < self.__length[1] and direction[1] + 1 >= 0):
                    #If the next char is not a space, replace it
                    char = self.__input[Y+direction[1]][X+direction[0]] 
                    if char == " ":
                        continue
                    copy = list(self.__input[Y])
                    copy[X] = " "
                    self.__input[Y] = "".join(copy)

            else:
                break
        return [[X,Y],"".join(letters)]
    
    # checkRemain
    # checking the amount of remaining letters on the grid
    # It will count the amount of letters remaining, looping though all of them
    # Will return True if there is more than 1 characters
    # TODO: Add a check with the last coordinates. 
    # Would optimize the speed and
    # Will prevent grids with floating letters from looping forever
    def checkRemain(self):
        count = 0
        for line in self.__input:
            for char in line:
                if char != " ": 
                    count = count + 1

        return count > 1

    # solve
    # Will Solve the grid, returning the array of words found
    def solve(self):
        lastCoords = [0,0]
        while(self.checkRemain()):
            ans = self.findAndDeleteWord(lastCoords)
            self.__words.append(ans[1])
            lastCoords = ans[0]

        return self.__words

    # printGrid
    # Prints the grid
    # Debugging purpose
    def printGrid(self):
        print "\n".join(self.__input)

inpt = """8
W    DINOSAUR
I    E      E
Z  CAR  Y   A
A  I    L   C
R  D    T  OT
D  R    B  V  
R  O    U  A 
YAWN    SGEL """.split("\n");
del inpt[0]

solver = wordSnake(inpt)
print " ".join(solver.solve());

