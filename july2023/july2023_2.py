import numpy as np
import tkinter as tk

class GridTile:
    def __init__(self, master, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.color = "white"
        self.button = tk.Button(master, text=str(self.value), width=5, height=2, bg=self.color, command=self.toggle_color)
        self.button.grid(row=row, column=col)
        self.button.bind("<Button-3>", self.reset_color)

    def toggle_color(self):
        if self.color == "white":
            self.color = "gray"
        elif self.color == "gray":
            self.color = "#ffd4d4"
        else:
            self.color = "gray"
        self.button.configure(bg=self.color)

    def reset_color(self, event):
        self.color = "white"
        self.button.configure(bg=self.color)

    def set_value(self, value):
        self.value = value
        self.button.configure(text=str(self.value))


def create_grid(matrix):
    n_rows, n_cols = matrix.shape
    root = tk.Tk()
    root.title("Interactive Grid")
    tiles = [[None for _ in range(n_cols)] for _ in range(n_rows)]
    for row in range(n_rows):
        for col in range(n_cols):
            tiles[row][col] = GridTile(root, row, col, matrix[row][col])
    return root, tiles

def main():
    matrix = np.array([
        [6,  6,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  6,  6],
        [6,  0,  0,  0,  0,  0,  0,  0,  0,  8, 12,  0,  0,  0,  0,  0,  0,  0,  0,  6],
        [0,  0,  0, 10, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 12, 12,  0,  0,  0],
        [0,  0,  0, 10,  0,  0, 10, 10,  0,  0,  0,  0, 11, 11,  0,  0,  4,  0,  0,  0],
        [0,  0,  0,  0,  0,  0, 10,  0,  0,  0,  0,  0,  0, 11,  0,  0,  0,  0,  0,  0],
        [0, 15,  0,  0,  0,  0,  0,  0,  0,  3,  4,  0,  0,  0,  0,  0,  0,  0,  3,  0],
        [0,  4,  0,  0,  0,  0,  0,  0,  0,  6,  5,  0,  0,  0,  0,  0,  0,  0, 12,  0],
        [0,  0,  0,  0,  0,  0,  9,  0,  0,  0,  0,  0,  0,  8,  0,  0,  0,  0,  0,  0],
        [0,  0,  0, 15,  0,  0,  9,  9,  0,  0,  0,  0,  8,  8,  0,  0,  8,  0,  0,  0],
        [0,  0,  0,  1,  9,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  7,  0,  0,  0],
        [4,  0,  0,  0,  0,  0,  0,  0,  0, 12,  8,  0,  0,  0,  0,  0,  0,  0,  0,  4],
        [4,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  4],
    ])
        
    n_rows, n_cols = matrix.shape
    root, tiles = create_grid(matrix)

    while True:
        row = int(input("Enter the row index (0 to {}): ".format(n_rows-1)))
        col = int(input("Enter the column index (0 to {}): ".format(n_cols-1)))
        if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            print("Invalid row or column index.")
            continue
        value = input("Enter the value (empty string or an integer between 1 and 20): ")
        if value != "" and not value.isdigit() or (value.isdigit() and (int(value) < 1 or int(value) > 20)):
            print("Invalid value.")
            continue
        matrix[row][col] = value
        tiles[row][col].set_value(value)

    root.mainloop()

if __name__ == '__main__':
    main()

