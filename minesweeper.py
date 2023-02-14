import tkinter as tk
from board import GameBoard

class MinesweeperGUI:
    def __init__(self, size=10, num_mines=10):
        self.size = size
        self.num_mines = num_mines
        self.game_board = GameBoard(size, num_mines)
        self.revealed = set()
        self.flagged = set()

        self.root = tk.Tk()
        self.root.title("Minesweeper")

        self.tiles = []
        for i in range(size):
            row = []
            for j in range(size):
                tile_button = tk.Button(self.root, text=" ", width=2, height=1,
                                        command=lambda i=i, j=j: self._on_tile_click(i, j),
                                        relief="raised")
                tile_button.bind("<Button-3>", lambda event, i=i, j=j: self._on_right_click(i, j))
                tile_button.grid(row=i, column=j)
                row.append(tile_button)
            self.tiles.append(row)

        self.status_label = tk.Label(self.root, text=" ")
        self.status_label.grid(row=size, columnspan=size)

    def _on_tile_click(self, i, j):
        if (i, j) in self.revealed or (i, j) in self.flagged:
            return
        if not self.game_board.reveal(i, j):
            self.status_label.config(text="Game Over")
            self._reveal_board()
        else:
            self.revealed.add((i, j))
            self.tiles[i][j].config(text=str(self.game_board.board[i][j]))
            if self.game_board.board[i][j].adjacent_mines == 0:
                for (ni, nj) in self.game_board.get_adjacent_tiles(i, j):
                    self._on_tile_click(ni, nj)
            if self.game_board.is_solved():
                self.status_label.config(text="You Win!")
                self._reveal_board()

    def _on_right_click(self, i, j):
        if (i, j) in self.revealed:
            return
        if (i, j) in self.flagged:
            self.flagged.remove((i, j))
            self.tiles[i][j].config(text=" ")
        else:
            self.flagged.add((i, j))
            self.tiles[i][j].config(text="F")

    def _reveal_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.game_board.board[i][j].is_mine:
                    self.tiles[i][j].config(text="X")
                else:
                    self.tiles[i][j].config(text=str(self.game_board.board[i][j]))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = MinesweeperGUI()
    gui.run()
