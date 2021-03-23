
class Tile():
    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.piece = None
        self.color = color
        self.gui_tile = None
    
    def addPiece(self, piece):
        self.piece = piece
        
    def removePiece(self):
        toRemove = self.piece
        self.piece = None
        return toRemove
    
    def isOccupied(self):
        return self.piece != None
tile_colors = ['white', 'black']    