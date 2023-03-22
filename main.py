import tkinter as tk
from tkinter import messagebox


class MainView:


    def __init__(self):

        # initialization

        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("App SMS Console")

        # text

        self.label = tk.Label(self.root, text="test", font=('Arial', 14))
        self.label.pack()

        # button. displays message when pressed

        self.button = tk.Button(self.root, text="Click", font=('Arial', 14), command=self.button_click)
        self.button.pack()

        # run

        self.root.mainloop()


    def button_click(self):
        tk.messagebox.showinfo(title="Message", message="Hello")


MainView()
