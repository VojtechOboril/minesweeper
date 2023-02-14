from minesweeper import MinesweeperGUI
import tkinter as tk

class Menu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Minesweeper Menu")
        
        self.size_label = tk.Label(self.root, text="Board size:")
        self.size_label.pack()
        self.size_scale = tk.Scale(self.root, from_=5, to=25, orient=tk.HORIZONTAL)
        self.size_scale.set(10)
        self.size_scale.pack()
        
        self.mines_label = tk.Label(self.root, text="Number of mines:")
        self.mines_label.pack()
        self.mines_scale = tk.Scale(self.root, from_=5, to=100, orient=tk.HORIZONTAL)
        self.mines_scale.set(10)
        self.mines_scale.pack()
        
        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack()
        
        self.root.mainloop()
    
    def start_game(self):
        size = self.size_scale.get()
        num_mines = self.mines_scale.get()
        self.root.destroy()
        game = MinesweeperGUI(size, num_mines)

if __name__ == "__main__":
    menu = Menu()