import tkinter as tk


from windows_constants import *
from login_window import LoginWindow
from register_window import RegisterWindow


class MainWindow(tk.Toplevel):

    def __init__(self, parent, window_handler, serverAPI):
        super().__init__(parent)

        self.serverAPI = serverAPI
        self.window_handler = window_handler

        self.geometry(f"{MAIN_WIN_WIDTH}x{MAIN_WIN_HEIGHT}")
        self.title(MAIN_WIN_TITLE)
        self.resizable(False, False)

        self.title_label = tk.Label(
            self, text = MAIN_WIN_TITLE, bg = TITLE_BG_CLR, width=SCREEN_WIDTH, height=SIGN_IN_TITLE_HEIGHT, font = TITLE_TXT_FONT)
        
        self.login_button = tk.Button(
            self, text = LOGIN_WIN_TITLE, command=self.login_command, font=BTN_FONT, bg=BTN_BG_CLR, width=BTN_WIDTH, height=BTN_HEIGHT, activebackground=BTN_CLR_ON_CLICK)
        
        self.register_button = tk.Button(
            self, text = REGISTER_WIN_TITLE,command=self.register_command , font=BTN_FONT, bg=BTN_BG_CLR, width=BTN_WIDTH, height=BTN_HEIGHT, activebackground=BTN_CLR_ON_CLICK)

        self.title_label.pack()
        self.login_button.pack()
        self.register_button.pack()

    def login_command(self):
        pass

    def register_command(self):
        pass

