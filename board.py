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

    def move(self, row, col):
        assert self.isSelected()
        cur_row = self.selected[0]
        cur_col = self.selected[1]
        piece = self.Board[cur_row][cur_col].piece
        if piece.isKing:
            max_valid_moves = [(cur_row + i, cur_col + j)
                               for i in [-1, 1] for j in [-1, 1]]
            max_valid_attacks = [(cur_row + i, cur_col + j)
                                 for i in [-2, 2] for j in [-2, 2]]
        else:
            if self.turn == 0:
                max_valid_moves = [(cur_row + i, cur_col + j)
                                   for i in [-1] for j in [-1, 1]]
                max_valid_attacks = [(cur_row + i, cur_col + j)
                                     for i in [-2] for j in [-2, 2]]
            else:
                max_valid_moves = [(cur_row + i, cur_col + j)
                                   for i in [1] for j in [-1, 1]]
                max_valid_attacks = [(cur_row + i, cur_col + j)
                                     for i in [2] for j in [-2, 2]]

        max_valid_moves = [pos for pos in max_valid_moves if pos[0] in range(
            8) and pos[1] in range(8)]
        max_valid_attacks = [
            pos for pos in max_valid_attacks if pos[0] in range(8) and pos[1] in range(8)]

        max_valid_moves = [
            pos for pos in max_valid_moves if not self.Board[pos[0]][pos[1]].isOccupied()]
        max_valid_attacks = [
            pos for pos in max_valid_attacks if not self.Board[pos[0]][pos[1]].isOccupied()]

        new_valid = []
        for pos in max_valid_attacks:
            middle = self.Board[int((cur_row + pos[0])//2)
                                ][int((cur_col + pos[1])//2)]
            if middle.isOccupied() and middle.piece.color != piece.color:
                new_valid.append(pos)
        max_valid_attacks = new_valid

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
