import tkinter as tk

# Canvas settings
CELL_SIZE = 30
ROWS = 10
COLUMNS = 10
ERASER_SIZE = 40

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Eraser")
        self.canvas = tk.Canvas(root, width=COLUMNS*CELL_SIZE, height=ROWS*CELL_SIZE, bg="white")
        self.canvas.pack()

        self.cells = []  # To store cell rectangles
        self.create_grid()

        # Eraser
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="gray", outline="black")

        # Mouse events
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def create_grid(self):
        """Create blue cell grid"""
        for row in range(ROWS):
            row_cells = []
            for col in range(COLUMNS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white")
                row_cells.append(rect)
            self.cells.append(row_cells)

    def move_eraser(self, event):
        """Move eraser and erase blue cells"""
        x1 = event.x - ERASER_SIZE / 2
        y1 = event.y - ERASER_SIZE / 2
        x2 = event.x + ERASER_SIZE / 2
        y2 = event.y + ERASER_SIZE / 2

        # Move eraser rectangle
        self.canvas.coords(self.eraser, x1, y1, x2, y2)

        # Check collision with cells
        for row in self.cells:
            for cell in row:
                cell_coords = self.canvas.coords(cell)
                if self.check_collision(x1, y1, x2, y2, cell_coords):
                    self.canvas.itemconfig(cell, fill="white")

    def check_collision(self, x1, y1, x2, y2, cell_coords):
        """Check if eraser overlaps a cell"""
        cx1, cy1, cx2, cy2 = cell_coords
        return not (x2 < cx1 or x1 > cx2 or y2 < cy1 or y1 > cy2)


# Run the app
root = tk.Tk()
app = EraserApp(root)
root.mainloop()
