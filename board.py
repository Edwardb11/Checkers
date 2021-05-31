import tkinter as tk
from piece import *
from tile import *
from main import *

class Game():
    def __init__(self):
        self.players = ['tan2', 'LightBlue1']
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
                        newPiece = Piece("LightBlue1", row_idx, col_idx)
                        newTile.addPiece(newPiece)
                    if row_idx in range(5, 8):
                        newPiece = Piece("tan2", row_idx, col_idx)
                        newTile.addPiece(newPiece)
                row.append(newTile)
            self.Board.append(row)

    def nextTurn(self):
        self.turn = (self.turn + 1) % 2

    def isSelected(self):
        return self.selected != (None, None)

    def select(self, row, col):
        if self.Board[row][col].isOccupied():
            piece = self.Board[row][col].piece
            if piece.color == self.players[self.turn]:
                self.selected = (row, col)
                return True
            else:
                self.selected = (None, None)
        return False

    #rename to move_tile
    def move_tile(self, row, col):
        assert self.isSelected()
        cur_row = self.selected[0]
        cur_col = self.selected[1]
        piece = self.Board[cur_row][cur_col].piece

        #Abstract function
        def  max_valid(x,y):
            return [(cur_row + i, cur_col + j)
                for i in x for j in y]

        if piece.isKing:
            max_valid_moves = max_valid([-1,1],[-1,1])
            max_valid_attacks = max_valid([-2,2],[-2,2])
        else:
            if self.turn == 0:
                max_valid_moves = max_valid([-1],[-1,1])
                max_valid_attacks = max_valid([-2],[-2,2])
            else:
                max_valid_moves = max_valid([1],[-1,1])
                max_valid_attacks = max_valid([2],[-2,2])

        #max_valid_moves -> basically here valid maximum movements are controlled
        #max_valid_attacks -> here the maximum valid attacks are controlled
        max_valid_moves = [pos for pos in max_valid_moves if pos[0] in range(
            8) and pos[1] in range(8)]
        max_valid_attacks = [
            pos for pos in max_valid_attacks if pos[0] in range(8) and pos[1] in range(8)]
        max_valid_moves = [
            pos for pos in max_valid_moves if not self.Board[pos[0]][pos[1]].isOccupied()]
        max_valid_attacks = [
            pos for pos in max_valid_attacks if not self.Board[pos[0]][pos[1]].isOccupied()]
        
        new_valid = []
        #scan to see if it is busy maximum valid attacks
        for pos in max_valid_attacks:
            middle = self.Board[int((cur_row + pos[0])//2)
                                ][int((cur_col + pos[1])//2)]
            if middle.isOccupied() and middle.piece.color != piece.color:
                new_valid.append(pos)
        max_valid_attacks = new_valid

        #Compare if it can be moved can be moved without killing or killing the piece
        if (row, col) in max_valid_moves:
            moved_piece = self.Board[cur_row][cur_col].removePiece()
            moved_piece.row = row
            moved_piece.col = col
            if moved_piece.color == self.players[0]:
                if moved_piece.row == 0:
                    moved_piece.isKing = True
            elif moved_piece.color == self.players[1]:
                if moved_piece.row == 7:
                    moved_piece.isKing = True
            self.Board[row][col].addPiece(moved_piece)
            self.nextTurn()
        elif (row, col) in max_valid_attacks:
            moved_piece = self.Board[cur_row][cur_col].removePiece()
            moved_piece.row = row
            moved_piece.col = col
            if moved_piece.color == self.players[0]:
                if moved_piece.row == 0:
                    moved_piece.isKing = True
            elif moved_piece.color == self.players[1]:
                if moved_piece.row == 7:
                    moved_piece.isKing = True
            self.Board[row][col].addPiece(moved_piece)
            killed_piece = self.Board[int(
                (row + cur_row)//2)][int((col + cur_col)//2)].removePiece()

        self.selected = (None, None)
