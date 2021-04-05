import tkinter as tk
from piece import *
from tile import *
from main import *

class Game():
    def __init__(self):
        self.players = ['red', 'yellow']
        self.tile_colors = ['white', 'black']
#         self.num_pieces = {color:12 for color in self.players}
        self.turn = 0
        self.selected = (None, None)
        self.Board = []
        for row_idx in range(8):
            row = []
            for col_idx in range(8):
                newTile = Tile(row_idx, col_idx,
                               self.tile_colors[(row_idx + col_idx) % 2])
                if newTile.color == self.tile_colors[1]:
                    if row_idx in range(0, 3):
                        newPiece = Piece("yellow", row_idx, col_idx)
                        newTile.addPiece(newPiece)
                    if row_idx in range(5, 8):
                        newPiece = Piece("red", row_idx, col_idx)
                        newTile.addPiece(newPiece)
                row.append(newTile)
            self.Board.append(row)
