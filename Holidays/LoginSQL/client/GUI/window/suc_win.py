import tkinter as tk
from client.GUI.window.window_const import *

class SucWindow(tk.Toplevel):

    def __init__(self, parent, serverAPI):
        super().__init__(parent)
        
        self.serverAPI = serverAPI
    
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.title(MAIN_TITLE)
        self.resizable(False, False)

        self.title_label = tk.Label(
            self, text = "Login Successfully", bg = TITLE_BG_CLR, width=SCREEN_WIDTH, height=SIGN_IN_TITLE_HEIGHT, font = TITLE_TXT_FONT)
        

        self.title_label.pack()
