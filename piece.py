class Piece():
    def __init__(self, color, row, column):
        self.color = color
        self.row = row
        self.column = column
        self.isKing = False

    def promote(self):
        self.isKing |= True
        
# | = performs an in-place + operation between pairs of objects. In particular, between:
      #joints: a union operation
      #dicta: an update operation
      #counters: a join operation (multigame)
      # numbers: a bitwise OR, binary operation