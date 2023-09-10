import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import serverAPI


class ClientGUI:
    def __init__(self, root):
        self.server = serverAPI.ServerAPI()
        self.server.connect()

        self.root = root
        self.root.title("Library Client")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Library Client")
        self.label.pack(pady=10)

        self.output_label = tk.Label(self.root, text="", wraplength=300)
        self.output_label.pack(pady=10)

        # Define the menu options as a list of dictionaries
        self.menu_options = [
            {"label": "Get All Authors", "command": self.get_all_authors},
            {"label": "Insert Author", "command": self.insert_author},
            {"label": "Get All Books", "command": self.get_all_books},
            {"label": "Insert Book", "command": self.insert_book},
            {"label": "Get Books by Author ID", "command": self.get_books_by_author_id},
            {"label": "Get Books by Author Name", "command": self.get_books_by_author_name},
            {"label": "Get Books by Genre", "command": self.get_books_by_genre},
            {"label": "Get Books in Price Range", "command": self.get_books_in_price_range},
            {"label": "Get Book by Name", "command": self.get_book_by_name}
        ]

        # Create buttons and associate them with commands dynamically
        for option in self.menu_options:
            button = tk.Button(self.root, text=option["label"], command=option["command"])
            button.pack()

        self.quit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.quit_button.pack()

    # Define functions for menu options
    def get_all_authors(self):
        self.send_receive("GETAUT-")

    def insert_author(self):
        # Create a separate window or dialog for entering author details
        author_window = tk.Toplevel(self.root)
        author_window.title("Insert Author")

        first_name_label = tk.Label(author_window, text="First Name:")
        first_name_label.pack()
        first_name_entry = tk.Entry(author_window)
        first_name_entry.pack()

        last_name_label = tk.Label(author_window, text="Last Name:")
        last_name_label.pack()
        last_name_entry = tk.Entry(author_window)
        last_name_entry.pack()

        nationality_label = tk.Label(author_window, text="Nationality:")
        nationality_label.pack()
        nationality_entry = tk.Entry(author_window)
        nationality_entry.pack()

        insert_button = tk.Button(author_window, text="Insert", command=lambda: self.insert_author_data(
            first_name_entry.get(), last_name_entry.get(), nationality_entry.get(), author_window))
        insert_button.pack()

    def get_all_books(self):
        self.send_receive("GETBOK-")

    def insert_book(self):
        # Create a separate window or dialog for entering book details
        book_window = tk.Toplevel(self.root)
        book_window.title("Insert Book")

        book_name_label = tk.Label(book_window, text="Book Name:")
        book_name_label.pack()
        book_name_entry = tk.Entry(book_window)
        book_name_entry.pack()

        # Add more entry fields for genre, price, and author ID
        genre_label = tk.Label(book_window, text="Genre:")
        genre_label.pack()
        genre_entry = tk.Entry(book_window)
        genre_entry.pack()

        price_label = tk.Label(book_window, text="Price:")
        price_label.pack()
        price_entry = tk.Entry(book_window)
        price_entry.pack()

        author_id_label = tk.Label(book_window, text="Author ID:")
        author_id_label.pack()
        author_id_entry = tk.Entry(book_window)
        author_id_entry.pack()


        insert_button = tk.Button(book_window, text="Insert", command=lambda: self.insert_book_data(
            book_name_entry.get(), genre_entry.get(), price_entry.get(), author_id_entry.get(), book_window))
        insert_button.pack()

    def get_books_by_author_id(self):
        author_id = simpledialog.askstring("Author ID", "Enter Author ID:")
        if author_id:
            data = f"GBBAID-{author_id}"
            self.send_receive(data)

    def get_books_by_author_name(self):
        author_first_name = simpledialog.askstring("Author First Name", "Enter Author Name:")
        author_last_name = simpledialog.askstring("Author Last Name", "Enter Author Last Name:")
        if author_first_name and author_last_name:
            data = f"GBBYAN-{author_first_name}|{author_last_name}"
            self.send_receive(data)

    def get_books_by_genre(self):
        genre = simpledialog.askstring("Genre", "Enter Genre:")
        if genre:
            data = f"GBBGEN-{genre}"
            self.send_receive(data)

    def get_books_in_price_range(self):
        min_price = simpledialog.askstring("Min Price", "Enter Min Price:")
        max_price = simpledialog.askstring("Max Price", "Enter Max Price:")
        if min_price and max_price:
            data = f"GBBPRI-{min_price}|{max_price}"
            self.send_receive(data)

    def get_book_by_name(self):
        book_name = simpledialog.askstring("Book Name", "Enter Book Name:")
        if book_name:
            data = f"GBBNAM-{book_name}"
            self.send_receive(data)

    
    

    # Define other functions for menu options
    # ...

    def insert_author_data(self, first_name, last_name, nationality, author_window):
        data = f"ADDAUT-{first_name}|{last_name}|{nationality}"
        self.send_receive(data)
        author_window.destroy()

    def insert_book_data(self, book_name, genre, price, author_id, book_window):
        data = f"ADDBOK-{book_name}|{genre}|{price}|{author_id}"
        self.send_receive(data)
        book_window.destroy()

    def send_receive(self, data):
        self.server.send(data)
        response = self.server.recv().decode()
        if response:
            self.output_label.config(text="Received: " + response)
        else:
            messagebox.showerror("Error", "Server disconnected.")
            self.root.quit()

def main():
    root = tk.Tk()
    client_gui = ClientGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
