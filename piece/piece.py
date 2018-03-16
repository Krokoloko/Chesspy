class Piece:
    def __init__(self,letPos,numPos,color,state,icon):
        self.letPos = letPos
        self.numPos = numPos
        self.color = color
        self.state = state
        self.icon = icon
        print(type(self).__name__)

    def passive(self):
        pass
    def update(self,board):
        pass
    #Returns true if you're allowed to go to the chosen position.
    def moveOption(self,board):
        pass

    #Returns true if you're allowed to attack.
    def attackOption(self,board):
        pass
    #Changes the position of the piece
    def setPos(self,x,y):
        self.letPos = x
        self.numPos = y

# All the sub classes from the Piece class down bellow.

class Queen(Piece):
    def __init__(self,letPos,numPos,color,state):
        super().__init__(letPos,numPos,color,state)

    def moveOption(self,board,letSug,numSug):
        pass      

    def setPos(self,x,y):
        super().setPos(x, y)

class King(Piece):
    def __init__(self,letpos,numpos,color,state):
        super().__init__(letPos, numPos, color, state)

    def moveOption(self,board):
        pass
    def setPos(self,x,y):
        super().setPos(x, y)

class Pawn(Piece):
    def __init__(self,letpos,numpos,color,state):
        super().__init__(letPos, numPos, color, state)

    def moveOption(self,board):
        pass

    def setPos(self,x,y):
        super().setPos(x, y)

class Bishop(Piece):
    def __init__(self,letpos,numpos,color,state):
        super().__init__(letPos, numPos, color, state)

    def moveOption(self,board):
        pass

    def setPos(self,x,y):
        super().setPos(x, y)

class Knight(Piece):
    def __init__(self,letpos,numpos,color,state):
        super().__init__(letPos, numPos, color, state)

    def moveOption(self,board):
        pass

    def setPos(self,x,y):
        super().setPos(x, y)

class Rook(Piece):
    def __init__(self,letpos,numpos,color,state):
        super().__init__(letPos, numPos, color, state)

    def moveOption(self,board):
        pass

    def setPos(self,x,y):
        super().setPos(x, y)
