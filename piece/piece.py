class Piece:
    def __init__(self,letPos,numPos,typePiece,color):
        self.letPos = letPos
        self.numPos = numPos
        self.typePiece = typePiece
        self.color = color
        self.state = 'alive'
