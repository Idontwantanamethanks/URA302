# tic_tac_toe
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.board = [" "]*9
        self.current_player = "X"
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            b = tk.Button(self.master, text=" ", font=('Arial', 20), width=5, height=2,
                          command=lambda i=i: self.make_move(i))
            b.grid(row=i//3, column=i%3)
            self.buttons.append(b)

    def make_move(self, idx):
        if self.board[idx] == " ":
            self.board[idx] = self.current_player
            self.buttons[idx].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        combos = [
            [0,1,2], [3,4,5], [6,7,8],   # rows
            [0,3,6], [1,4,7], [2,5,8],   # columns
            [0,4,8], [2,4,6]             # diagonals
        ]
        for c in combos:
            if all(self.board[i]==player for i in c):
                return True
        return False

    def check_tie(self):
        return all(space != " " for space in self.board)

    def reset_board(self):
        self.board = [" "]*9
        for b in self.buttons:
            b.config(text=" ")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()

# todo_list
import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoList:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.tasks = []

        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)

        self.entry = tk.Entry(self.frame, width=30)
        self.entry.grid(row=0, column=0, padx=5)
        tk.Button(self.frame, text="Add Task", command=self.add_task).grid(row=0, column=1, padx=5)
        tk.Button(self.frame, text="View Tasks", command=self.view_tasks).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(self.frame, text="Delete Task", command=self.delete_task).grid(row=1, column=1, padx=5, pady=5)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Task '{task}' added.")
        else:
            messagebox.showerror("Error", "Task cannot be empty.")

    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("Tasks", "No tasks in the list.")
        else:
            tasks_str = "\n".join([f"{i+1}. {task}" for i, task in enumerate(self.tasks)])
            messagebox.showinfo("Tasks", tasks_str)

    def delete_task(self):
        if not self.tasks:
            messagebox.showinfo("Error", "No tasks to delete.")
            return
        idx = simpledialog.askinteger("Delete Task", "Enter task number to delete:")
        if idx is not None and 1 <= idx <= len(self.tasks):
            removed = self.tasks.pop(idx-1)
            messagebox.showinfo("Deleted", f"Task '{removed}' deleted.")
        else:
            messagebox.showerror("Error", "Invalid task number.")

if __name__ == "__main__":
    root = tk.Tk()
    ToDoList(root)
    root.mainloop()


# robot_path_planning
import tkinter as tk
from tkinter import simpledialog, messagebox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from queue import PriorityQueue

class RobotPathPlanning:
    def __init__(self, master):
        self.master = master
        self.master.title("Robot Path Planning (A*)")
        self.grid = None
        self.start = None
        self.end = None

        tk.Button(master, text="Setup Grid & Obstacles", command=self.setup_grid).pack(pady=5)
        tk.Button(master, text="Find Path", command=self.find_path).pack(pady=5)

    def setup_grid(self):
        rows = simpledialog.askinteger("Input", "Enter number of rows:")
        cols = simpledialog.askinteger("Input", "Enter number of columns:")
        self.grid = np.zeros((rows, cols), dtype=int)

        num_obs = simpledialog.askinteger("Input", "Enter number of obstacles:")
        for _ in range(num_obs):
            r = simpledialog.askinteger("Obstacle", f"Obstacle row (0-{rows-1}):")
            c = simpledialog.askinteger("Obstacle", f"Obstacle col (0-{cols-1}):")
            self.grid[r, c] = 1

        self.start = (
            simpledialog.askinteger("Start", "Start row:"),
            simpledialog.askinteger("Start", "Start col:")
        )
        self.end = (
            simpledialog.askinteger("End", "Destination row:"),
            simpledialog.askinteger("End", "Destination col:")
        )

        # Display grid using pandas
        df = pd.DataFrame(self.grid)
        print("Grid:\n", df)

    def heuristic(self, a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    def find_path(self):
        if self.grid is None or self.start is None or self.end is None:
            messagebox.showerror("Error", "Grid or start/end points not set.")
            return

        rows, cols = self.grid.shape
        open_set = PriorityQueue()
        open_set.put((0, self.start))
        came_from = {}
        g_score = {self.start: 0}

        while not open_set.empty():
            current = open_set.get()[1]
            if current == self.end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(self.start)
                path.reverse()
                self.plot_path(path)
                return

            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                    if self.grid[neighbor]==1:
                        continue
                    tentative_g = g_score[current] + 1
                    if neighbor not in g_score or tentative_g < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g
                        f_score = tentative_g + self.heuristic(neighbor, self.end)
                        open_set.put((f_score, neighbor))

        messagebox.showinfo("Result", "No valid path found.")

    def plot_path(self, path):
        plt.figure()
        grid_plot = self.grid.copy()
        for r,c in path:
            grid_plot[r,c] = 2
        plt.imshow(grid_plot, cmap='gray_r')

        plt.scatter(self.start[1], self.start[0], marker='o', color='green', s=100, label='Start')
        plt.scatter(self.end[1], self.end[0], marker='x', color='blue', s=100, label='Destination')

        plt.title("Robot Path Planning (A*)")
        plt.legend()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    RobotPathPlanning(root)
    root.mainloop()

