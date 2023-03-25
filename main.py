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
        self.stopped = False

        # text

        tk.Label(self.root, text="App SMS Console", font=('Arial', 40)).pack()

        self.label_commands = tk.Label(self.root, text=f"Commands sent since start: {self.number}", font=('Arial', 16))
        self.label_commands.pack()

        tk.Button(self.root, text="Refresh", font=('Arial', 14), command=self.button1_refresh).pack()
        self.stop_button = tk.Button(self.root, text="STOP", font=('Arial', 14), command=self.button2_refresh)
        self.stop_button.pack()

        # run

        self.root.mainloop()


    def button1_refresh(self):

        self.update_commands_sent()
        self.root.update()


    def button2_refresh(self):

        if self.stopped:
            self.stopped = False
            self.root.title("App SMS Console")
            self.stop_button.config(text="STOP")
        else:

            user_response = messagebox.askyesnocancel(message="Are you sure you want to stop the service?")
            if user_response:
                self.stopped = True
                self.root.title("App SMS Console - STOPPED")
                self.stop_button.config(text="RESUME")


    def update_commands_sent(self):
        self.number += 1
        self.label_commands.config(text=f"Commands sent since start: {self.number}", font=('Arial', 16))


MainView()
