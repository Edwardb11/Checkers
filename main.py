from board import *
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas( self, width=640, height=640, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.Game = Game()
        self.rows = 8
        self.columns = 8
#         self.tiles = {}
        self.canvas.bind("<Configure>", self.redraw)
        self.status = tk.Label(self, anchor="w")
        self.status.pack(side="bottom", fill="x")
        #self.tile_colors = ['white', 'black']

    def redraw(self, event=None):
        self.canvas.delete("rect")
        cellwidth = int(self.canvas.winfo_width()/self.columns)
        cellheight = int(self.canvas.winfo_height()/self.columns)
        for row, row_tiles in enumerate(self.Game.Board):
            for column, tile in enumerate(row_tiles):
                x1 = column*cellwidth
                y1 = row * cellheight
                x2 = x1 + cellwidth
                y2 = y1 + cellheight
                tile.gui_tile = self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill=tile.color, tags="rect")
                if tile.isOccupied():
                    if tile.piece.isKing:
                        oval = self.canvas.create_oval(
                            x1, y1, x2, y2, fill=tile.piece.color, width=10)
                        self.canvas.tag_bind(
                            oval, "<1>", lambda event, row=row, column=column: self.clicked(row, column))
                    else:
                        oval = self.canvas.create_oval(
                            x1, y1, x2, y2, fill=tile.piece.color)
                        self.canvas.tag_bind(
                            oval, "<1>", lambda event, row=row, column=column: self.clicked(row, column))
                self.canvas.tag_bind(tile.gui_tile, "<1>", lambda event,
                                     row=row, column=column: self.clicked(row, column))
