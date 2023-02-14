import random

#random.seed(0)

class Tile:
    def __init__(self):
        self.is_mine = False
        self.is_marked = False
        self.adjacent_mines = 0
        self.is_revealed = False

    def set_mine(self):
        self.is_mine = True

    def set_adjacent_mines(self, num_mines):
        self.adjacent_mines = num_mines

    def reveal(self):
        self.is_revealed = True

    def mark(self):
        self.is_marked = True

    def unmark(self):
        self.is_marked = False

    def __str__(self):
        if self.is_marked:
            return "M"
        elif not self.is_revealed:
            return " "
        elif self.is_mine:
            return "*"
        else:
            return str(self.adjacent_mines)


class GameBoard:
    def __init__(self, size, num_mines):
        self.size = size
        self.num_mines = num_mines
        self.board = [[Tile() for _ in range(size)] for _ in range(size)]
        self._place_mines()
        self._calculate_adjacent_mines()

    def _place_mines(self):
        indices = [(i, j) for i in range(self.size) for j in range(self.size)]
        mine_indices = random.sample(indices, self.num_mines)
        for i, j in mine_indices:
            self.board[i][j].set_mine()

    def _calculate_adjacent_mines(self):
        for i in range(self.size):
            for j in range(self.size):
                if not self.board[i][j].is_mine:
                    self.board[i][j].set_adjacent_mines(self._count_adjacent_mines(i, j))

    def _count_adjacent_mines(self, i, j):
        count = 0
        for ii in range(max(0, i-1), min(i+2, self.size)):
            for jj in range(max(0, j-1), min(j+2, self.size)):
                if self.board[ii][jj].is_mine:
                    count += 1
        return count

    def reveal(self, i, j):
        if self.board[i][j].is_mine:
            return False
        self.board[i][j].reveal()
        return True
    
    def get_adjacent_tiles(self, i, j):
        adjacent_tiles = []
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < self.size and 0 <= nj < self.size:
                    adjacent_tiles.append((ni, nj))
        return adjacent_tiles

    def mark(self, i, j):
        self.board[i][j].mark()

    def unmark(self, i, j):
        self.board[i][j].unmark()

    def is_solved(self):
        for i in range(self.size):
            for j in range(self.size):
                if not self.board[i][j].is_mine and not self.board[i][j].is_revealed:
                    return False
        return True

    def __str__(self):
        separator = " | "
        top_line = "    " + separator.join(str(i) for i in range(self.size))
        board_lines = [top_line]
        for i in range(self.size):
            row = [str(self.board[i][j]) for j in range(self.size)]
            board_lines.append(f"{i}{separator}{' | '.join(row)}")
        return "\n".join(board_lines)


if __name__ == "__main__":
    board = GameBoard(10, 10)
    board.reveal(8, 0)
    print(board)