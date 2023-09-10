import sqlite3

import pickle
    # https://docs.python.org/2/library/sqlite3.html
    # https://www.youtube.com/watch?v=U7nfe4adDw8


__author__ = 'Eyal Keysar'


# List of strings in Queries that have potential to be SQL injection
SQL_INJECTION_POSSIBLE = ['--']


class Author(object):
    def __init__(self, author_first_name, author_last_name, nationality):
        self.author_id = None
        self.first_name = author_first_name
        self.last_name = author_last_name
        self.nationality = nationality

    def __str__(self):
        return "Author:id:" + str(self.author_id) + ":first name:" + self.first_name + ":last name:" + self.last_name + ":nationality:" + self.nationality
    
class Book(object):
    def __init__(self, book_name, genre, price, author_id):
        self.book_id = None
        self.book_name = book_name
        self.genre = genre
        self.price = price
        self.author_id = author_id

    

    def set_book_name(self, book_name):
        self.book_name = book_name
    def set_genre(self, genre):
        self.genre = genre
    def set_price(self, price):
        self.price = price
    def set_author_id(self, author_id):
        self.author_id = author_id

    def __str__(self):
        return "Book: id:" + str(self.book_id) + ": name:" + self.book_name + ": genre:" + self.genre + ": price:" + str(self.price) + ": author id:" + str(self.author_id)

    
class BookAuthorORM():
    def __init__(self):
        self.conn = None  # will store the DB connection
        self.cursor = None   # will store the DB connection cursor

    def _create_tables(self):
        self.open_DB()
        self.current.execute("PRAGMA foreign_keys = ON;")
        self.current.execute("CREATE TABLE IF NOT EXISTS Authors (Authorid INT PRIMARY KEY, Fname TEXT, Lname TEXT, Nationality TEXT);")
        self.current.execute("CREATE TABLE IF NOT EXISTS Books (Bookid INT PRIMARY KEY, Bookname TEXT, Genre TEXT, Price TEXT, Authorid INT, FOREIGN KEY (Authorid) REFERENCES Authors(Authorid));")
        self.commit()
        self.close_DB()

    def _drop_tables(self):
        self._drop_only_books()
        self._drop_only_authors()
        
    def _drop_only_books(self):
        self.open_DB()
        self.current.execute("DROP TABLE IF EXISTS Books;")
        self.commit()
        self.close_DB()
    def _drop_only_authors(self):
        self.open_DB()
        self.current.execute("DROP TABLE IF EXISTS Authors;")
        self.commit()
        self.close_DB()

    def open_DB(self):
        self.conn = sqlite3.connect('./BookAuthor.db')
        self.current = self.conn.cursor()
        self.current.execute("PRAGMA foreign_keys = ON;") # Enforce foreign key constraints

    def close_DB(self):
        self.conn.close()
    def commit(self):
        self.conn.commit()

    #All read SQL

    def get_authors(self):
        self.open_DB()

        authors=[]
        sql= "SELECT * FROM Authors"
        self.current.execute(sql)
        res = self.current.fetchall()
        for line in res:
            cur_author = Author(line[1],line[2],line[3])
            cur_author.author_id = line[0]
            authors.append(cur_author)
        self.close_DB()
        return authors
    
    def get_authors_as_strings(self):
        authors_as_obj = self.get_authors()
        authors_as_str = []
        for author in authors_as_obj:
            authors_as_str.append(str(author))
        return authors_as_str
    
    def get_books(self):
        self.open_DB()

        books=[]
        sql= "SELECT * FROM Books"
        self.current.execute(sql)
        res = self.current.fetchall()
        for line in res:
            cur_book = Book(line[1],line[2],line[3], line[4])
            cur_book.book_id = line[0]
            books.append(str(cur_book))
        self.close_DB()
        return books

    def get_book_by_author_id(self, author_id):

        for x in SQL_INJECTION_POSSIBLE:
            if(x in author_id):
                print("SQL INJECTION POSSIBLE")
                return ["SQL INJECTION DETECTED"]
        
        self.open_DB()
        books = []
        sql = "SELECT * FROM Books WHERE Authorid = " + str(author_id)
        self.current.execute(sql)
        res = self.current.fetchall()
        for line in res:
            cur_book = Book(line[1],line[2],line[3], line[4])
            cur_book.book_id = line[0]
            books.append(str(cur_book))
        self.close_DB()
        return books
    
    def get_book_by_author_name(self, author_fname, author_lname):
        for x in SQL_INJECTION_POSSIBLE:
            if(x in author_fname or x in author_lname):
                print("SQL INJECTION POSSIBLE")
                return ["SQL INJECTION DETECTED"]
        self.open_DB()
        books = []
        
        sql = "SELECT * FROM Books WHERE Authorid IN (SELECT Authorid FROM Authors WHERE Fname = '" + author_fname + "' AND Lname = '" + author_lname + "')"
        self.current.execute(sql)
        res = self.current.fetchall()
        for line in res:
            cur_book = Book(line[1],line[2],line[3], line[4])
            cur_book.book_id = line[0]
            books.append(str(cur_book))
        self.close_DB()
        return books
    
    def get_book_by_genre(self, genre):
        for x in SQL_INJECTION_POSSIBLE:
            if(x in genre):
                print("SQL INJECTION POSSIBLE")
                return ["SQL INJECTION DETECTED"]
        self.open_DB()
        books = []
        sql = "SELECT * FROM Books WHERE Genre = '" + genre + "'"
        self.current.execute(sql)
        res = self.current.fetchall()
        for line in res:
            cur_book = Book(line[1],line[2],line[3], line[4])
            cur_book.book_id = line[0]
            books.append(str(cur_book))
        self.close_DB()
        return books
    
    def get_book_by_price(self, min_price, max_price):
        for x in SQL_INJECTION_POSSIBLE:
            if(x in min_price or x in max_price):
                print("SQL INJECTION POSSIBLE")
                return ["SQL INJECTION DETECTED"]
        self.open_DB()
        books = []
        sql = "SELECT * FROM Books"
        self.current.execute(sql)
        res = self.current.fetchall()
        for line in res:
            cur_book = Book(line[1],line[2],line[3], line[4])
            cur_book.book_id = line[0]
            if(float(cur_book.price) >= float(min_price) and float(cur_book.price) <= float(max_price)):
                books.append(str(cur_book))
        self.close_DB()
        return books
    
    def get_book_by_name(self, book_name):
        for x in SQL_INJECTION_POSSIBLE:
            if(x in book_name):
                print("SQL INJECTION POSSIBLE")
                return ["SQL INJECTION DETECTED"]
        self.open_DB()
        books = []
        sql = "SELECT * FROM Books WHERE Bookname = '" + book_name + "'"
        self.current.execute(sql)
        res = self.current.fetchall()
        for line in res:
            cur_book = Book(line[1],line[2],line[3], line[4])
            cur_book.book_id = line[0]
            books.append(str(cur_book))
        self.close_DB()
        return books
    
    def get_authors_by_nationality(self, nationality):
        for x in SQL_INJECTION_POSSIBLE:
            if(x in nationality):
                print("SQL INJECTION POSSIBLE")
                return ["SQL INJECTION DETECTED"]
        self.open_DB()
        authors = []
        sql = "SELECT * FROM Authors WHERE Nationality = '" + nationality + "'"
        self.current.execute(sql)
        res = self.current.fetchall()
        for line in res:
            cur_author = Author(line[1],line[2],line[3])
            cur_author.author_id = line[0]
            authors.append(cur_author)
        self.close_DB()
        return authors
    


    #__________________________________________________________________________________________________________________
    #__________________________________________________________________________________________________________________
    #______end of read start write ____________________________________________________________________________________
    #__________________________________________________________________________________________________________________
    #__________________________________________________________________________________________________________________
    #__________________________________________________________________________________________________________________


    #All write SQL

    def insert_new_book(self, book):
        book_name = book.book_name
        genre = book.genre
        price = book.price
        author_id = book.author_id

        self.open_DB()

        sql = "SELECT MAX(Bookid) FROM Books"
        self.current.execute(sql)
        res = self.current.fetchone()
        res = res[0]
        if(res == None):
            res = '-1'
        new_id = int(res) + 1
        book.book_id = new_id
        print("new book in id: " + str(new_id))


        sql = "INSERT INTO Books (Bookid, Bookname, Genre, Price, Authorid) " 
        sql += "VALUES ("+str(new_id)+",'"+book_name+"','"+genre+"','"+str(price)+"',"+str(author_id)+");"
        print(sql)
        self.current.execute(sql)
        res = self.current.fetchone()

        self.commit()
        self.close_DB()

        return True

    def insert_new_author(self, author):

        Fname = author.first_name
        Lname = author.last_name
        Nationality = author.nationality

        self.open_DB()
        sql = "SELECT MAX(Authorid) FROM Authors"
        self.current.execute(sql)
        res = self.current.fetchone()
        res = res[0]
        if(res == None):
            res = '-1'
        new_id = int(res) + 1
        print("new author in id: " + str(new_id))

        sql = "INSERT INTO Authors (Authorid, Fname, Lname, Nationality) "
        sql += "VALUES (" + str(new_id) + ", '"+Fname+"', '"+Lname+"', '"+Nationality+"');"
        self.current.execute(sql)
        res = self.current.fetchone()

        self.commit()
        self.close_DB()

        return True


def main_test():

    db = BookAuthorORM()

    author = Author('jane', 'smith', 'USA')


    book1 = Book("Harry Potter", "Fantasy", "1", 0)

    db._drop_tables()
    db._create_tables()

    db.insert_new_author(author)
    db.insert_new_book(book1)

    res = db.get_authors()
    for i in res:
        print(i)

    res = db.get_books()
    for i in res:
        print(i)

if __name__ == "__main__":
    main_test()


