import tkinter as tk

class Piece:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.create_piece()

    def create_piece(self):
        self.canvas.create_oval(
            self.x * 100 + 10, self.y * 100 + 10,
            self.x * 100 + 90, self.y * 100 + 90,
            fill=self.color, outline="black"
        )
