class Board:
    def __init__(self):
        self.boardRows = ['A','B','C','D','E','F','G','H']
        self.boardCols = ['1','2','3','4','5','6','7','8']
        self.letters = 8
        self.numbers = 8
        self.boardMatrix = [[0 for x in range(self.letters)]for y in range(self.numbers)]

    def PrintBoard(self):
        print(" ", end=" ")
        for val in self.boardCols:
            print(val, end=" ")
        print("")

        for row in self.boardMatrix:
            for rval in self.boardRows:
                print(rval, end=" ")
                for val in row:
                    print(val, end=" ")
                print('')
            break
