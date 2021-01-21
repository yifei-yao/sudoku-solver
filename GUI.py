import tkinter as tk
from engine import solve


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.frame1 = tk.LabelFrame(self)
        self.frame1.grid(row=0, column=0)

        # setup Tkinter control variables
        self.variables = list()
        for i in range(9):
            new_row = list()
            for j in range(9):
                new_row.append(None)
            self.variables.append(new_row)

        # add the grids
        for i in range(3):
            for j in range(3):
                new_frame = tk.LabelFrame(self.frame1, bd=1)
                new_frame.grid(row=i, column=j)
                for x in range(3):
                    for y in range(3):
                        tv = tk.StringVar()
                        new_entry = tk.Entry(new_frame, width=2, bd=1, justify=tk.CENTER, textvariable=tv)
                        new_entry.grid(row=x, column=y)
                        self.variables[3 * i + x][3 * j + y] = tv

        self.frame2 = tk.Frame(self)
        self.frame2.grid(row=1, column=0)

        # add the buttons
        self.clear = tk.Button(self.frame2, text="clear", command=self.clear)
        self.clear.grid(row=0, column=0)

        self.solve = tk.Button(self.frame2, text="solve", command=self.press_solve)
        self.solve.grid(row=0, column=1)

    def clear(self):
        for i in range(9):
            for j in range(9):
                self.variables[i][j].set("")

    def press_solve(self):
        arr = list()
        for i in range(9):
            list1 = list()
            for j in range(9):
                list1.append(0)
            arr.append(list1)
        for i in range(9):
            for j in range(9):
                try:
                    number = int(self.variables[i][j].get())[0]
                    arr[i][j] = number
                except:
                    pass
        solved = solve(arr)
        for i in range(9):
            for j in range(9):
                self.variables[i][j].set(solved[i][j])
