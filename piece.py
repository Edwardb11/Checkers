class Piece():
    def __init__(self, color, row, column):
        self.color = color
        self.row = row
        self.column = column
        self.isKing = False

    def promote(self):
        self.isKing |= True
