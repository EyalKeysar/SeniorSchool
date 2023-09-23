import tkinter as tk


from windows_constants import *

class SucWindow(tk.Toplevel):

    def __init__(self, parent, window_handler, serverAPI):
        super().__init__(parent)

        self.serverAPI = serverAPI
        self.window_handler = window_handler

        self.geometry(f"{MAIN_WIN_WIDTH}x{MAIN_WIN_HEIGHT}")
        self.title(MAIN_WIN_TITLE)
        self.resizable(False, False)

        self.title_label = tk.Label(
            self, text = SUC_TITLE, bg = TITLE_BG_CLR, width=SCREEN_WIDTH, height=SIGN_IN_TITLE_HEIGHT, font = TITLE_TXT_FONT)
        self.title_label.pack()


