import tkinter as tk
from tkinter import messagebox


class MainView:

    number = 0

    def __init__(self):

        # initialization

        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.maxsize(500, 500)
        self.root.minsize(500, 500)
        self.root.title("App SMS Console")

        # text

        tk.Label(self.root, text="App SMS Console", font=('Arial', 40)).pack()


        self.label_commands = tk.Label(self.root, text=f"Commands sent since start: {self.number}", font=('Arial', 16))
        self.label_commands.pack()

        # button. displays message when pressed

        tk.Button(self.root, text="Refresh", font=('Arial', 14), command=self.button_refresh).pack()


        # run

        self.root.mainloop()


    def button_refresh(self):

        # messagebox.showinfo(message="test")

        self.update()
        self.root.update()
        # self.label_commands = tk.Label(self.root, text="t", font=('Arial', 16))
        # self.label_commands.pack()

    def update(self):
        self.number += 1
        self.label_commands.config(text=f"Commands sent since start: {self.number}", font=('Arial', 16))


MainView()
