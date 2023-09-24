from collections.abc import Callable, Sequence
import tkinter as tk
import tkinter.messagebox
from typing import Any

from client.GUI.window.window_const import *
from client.GUI.window.suc_win import SucWindow

class RegisterWindow(tk.Toplevel):
    def __init__(self, parent, serverAPI, window_handler):
        super().__init__(parent)
        
        self.serverAPI = serverAPI
        self.window_handler = window_handler

        self.geometry(f"{REGISTER_WINDOW_WIDTH}x{REGISTER_WINDOW_HEIGHT}")
        self.title("Register")
        self.resizable(False, False)
        self.attributes("-topmost", True)
        
        self.username_label = tk.Label(self, text="Username", font=LOGIN_TXT_FONT)
        self.username_entry = tk.Entry(self, width=LOGIN_TXT_INPUT_WIDTH, font=LOGIN_TXT_FONT)
        self.password_label = tk.Label(self, text="Password", font=LOGIN_TXT_FONT)
        self.password_entry = tk.Entry(self, show="●", width=LOGIN_TXT_INPUT_WIDTH, font=LOGIN_TXT_FONT)
        self.password_confirm_label = tk.Label(self, text="Confirm Password", font=LOGIN_TXT_FONT)
        self.password_confirm_entry = tk.Entry(self, show="●", width=LOGIN_TXT_INPUT_WIDTH, font=LOGIN_TXT_FONT)
        self.register_button = tk.Button(self, text="Register", command=self.register)

        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.password_confirm_label.pack()
        self.password_confirm_entry.pack()
        self.register_button.pack()



    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        password_confirm = self.password_confirm_entry.get()
        
        if(password != password_confirm):
            tk.messagebox.showerror("Error", "Passwords do not match")
            return
        
        res = self.serverAPI.register(username, password)
        if(res):
            tk.messagebox.showinfo("Success", "Register successful")
            self.window_handler.ChangeWindow(SucWindow, self.serverAPI)
        else:
            tk.messagebox.showerror("Error", "Register failed")
        


        

