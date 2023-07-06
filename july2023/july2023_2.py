import numpy as np
import tkinter as tk

class GridTile:
    def __init__(self, master, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.color = "white"
        self.button = tk.Button(master, width=5, height=2, bg=self.color, command=self.toggle_color)
        self.button.grid(row=row, column=col)
        self.label = tk.Label(master, text=self.value)
        self.label.grid(row=row, column=col)

    def toggle_color(self):
        if self.color == "white":
            self.color = "gray"
        else:
            self.color = "white"
        self.button.configure(bg=self.color)

    def set_value(self, value):
        self.value = value
        self.label.configure(text=self.value)

def create_grid(matrix):
    n = len(matrix)
    root = tk.Tk()
    root.title("Interactive Grid")
    tiles = [[None for _ in range(n)] for _ in range(n)]
    for row in range(n):
        for col in range(n):
            tiles[row][col] = GridTile(root, row, col, matrix[row][col])
    return root, tiles

def main():
    # Example matrix
    matrix = np.array([
        [0,6,0,0,0,0,0],
        [0,0,0,0,0,0,3],
        [0,0,0,3,0,0,0],
        [0,0,6,1,5,0,0],
        [0,0,0,4,0,0,0],
        [5,0,0,0,0,0,0],
        [0,0,0,0,0,4,0]
    ])
    n = len(matrix)
    root, tiles = create_grid(matrix)

    while True:
        row = int(input("Enter the row index (0 to {}): ".format(n-1)))
        col = int(input("Enter the column index (0 to {}): ".format(n-1)))
        if row < 0 or row >= n or col < 0 or col >= n:
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
