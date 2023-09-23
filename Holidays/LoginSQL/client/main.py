import tkinter as tk
from client.GUI.WindowHandler import WindowHandler
from client.GUI.window.main_win import MainWindow
from shared.serverAPI import ServerAPI


def main():
    
    serverAPI = ServerAPI()
    
    root = tk.Tk()
    root.withdraw()
    window_handler = WindowHandler(root)
    window_handler.ChangeWindow(MainWindow, window_handler, serverAPI)
    root.mainloop()
    
if __name__ == "__main__":
    main()