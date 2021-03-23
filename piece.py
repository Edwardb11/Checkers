class Piece():
    def __init__(self, color, row, column):
        self.color = color
        self.row = row
        self.column = column
        self.isKing = False

    def promote(self):
        self.isKing |= True
        
        #|=realiza una operación + in situ entre pares de objetos. En particular, entre:
    #conjuntos : una operación sindical
    #dicta : una operación de actualización
    #contadores : una operación de unión (de multijuegos)
    #números : un OR bit a bit , operación binaria