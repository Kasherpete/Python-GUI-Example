import tkinter as tk
from tkinter import messagebox


class MainView:


    def __init__(self):

        # initialization

        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.maxsize(500, 500)
        self.root.minsize(500, 500)
        self.root.title("App SMS Console")

        # text

        self.label = tk.Label(self.root, text="App SMS Console", font=('Arial', 40))
        self.label.pack()

        self.label_commands = tk.Label(self.root, text="Commands sent since start:", font=('Arial', 16))
        self.label_commands.pack()

        # button. displays message when pressed

        self.button = tk.Button(self.root, text="Refresh", font=('Arial', 14), command=self.button_refresh)
        self.button.pack()

        # run

        self.root.mainloop()


    def button_refresh(self):

        messagebox.showinfo(message="test")


        # self.label_commands = tk.Label(self.root, text="t", font=('Arial', 16))
        # self.label_commands.pack()


MainView()
