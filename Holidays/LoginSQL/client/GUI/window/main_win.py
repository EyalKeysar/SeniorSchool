import tkinter as tk
from client.GUI.window.window_const import *
from client.GUI.window.login_win import LoginWindow
from client.GUI.window.register_win import RegisterWindow
from client.GUI.window.suc_win import SucWindow

class MainWindow(tk.Toplevel):

    def __init__(self, parent, window_handler, serverAPI):
        super().__init__(parent)
        
        self.serverAPI = serverAPI
        
        self.window_handler = window_handler
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.title(MAIN_TITLE)
        self.resizable(False, False)

        self.title_label = tk.Label(
            self, text = SIGN_IN_TITLE_TXT, bg = TITLE_BG_CLR, width=SCREEN_WIDTH, height=SIGN_IN_TITLE_HEIGHT, font = TITLE_TXT_FONT)
        
        self.login_button = tk.Button(
            self, text = "Login", command=self.login_command, font=BTN_FONT, bg=BTN_BG_CLR, width=BTN_WIDTH, height=BTN_HEIGHT, activebackground=BTN_CLR_ON_CLICK)
        
        self.register_button = tk.Button(
            self, text = "Register",command=self.register_command , font=BTN_FONT, bg=BTN_BG_CLR, width=BTN_WIDTH, height=BTN_HEIGHT, activebackground=BTN_CLR_ON_CLICK)

        self.title_label.pack()
        self.login_button.pack()
        self.register_button.pack()

    def login_command(self):
        self.window_handler.PushWindow(LoginWindow, self.serverAPI, self.window_handler)
        
    def register_command(self):
        self.window_handler.PushWindow(RegisterWindow, self.serverAPI, self.window_handler)