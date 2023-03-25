import tkinter as tk
from tkinter import messagebox
import threading
import time


def do_stuff():
    while True:
        time.sleep(1)
        print("mark")



class MainView:

    number = 0

    def __init__(self):

        # initialization

        self.root = tk.Tk()
        self.root.protocol('WM_DELETE_WINDOW', self.display_closing_message)
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

        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Close")
        self.menu_bar.add_cascade(menu=self.file_menu, label="File")
        # self.root.config(menu=self.menu_bar)

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


    def display_closing_message(self):
        user_response = messagebox.askyesnocancel(message="Are you sure you want to quit? Doing so will stop the service.")
        if user_response:
            self.root.destroy()


service_thread = threading.Thread(target=do_stuff, daemon=True)
service_thread.start()

MainView()
