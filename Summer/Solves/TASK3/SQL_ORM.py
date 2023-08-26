import sqlite3

import pickle
    # https://docs.python.org/2/library/sqlite3.html
    # https://www.youtube.com/watch?v=U7nfe4adDw8


__author__ = 'Eyal Keysar'



class Author(object):
    def __init__(self, author_id, author_first_name, author_last_name, nationality):
        self.author_id = author_id
        self.first_name = author_first_name
        self.last_name = author_last_name
        self.nationality = nationality

    def __str__(self):
        return "Author:" + self.author_id + ":" + self.first_name + ":" + self.last_name + ":" + self.nationality
    
class Book(object):
    def __init__(self, book_name, genre, price, author_id):
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
        return "Book:" + self.book_name + ":" + self.genre + ":" + str(self.price) + ":" + self.author_id

    
class BookAuthorORM():
    def __init__(self):
        self.conn = None  # will store the DB connection
        self.cursor = None   # will store the DB connection cursor

    def open_DB(self):
        """
        will open DB file and put value in:
        self.conn (need DB file name)
        and self.cursor
        """
        self.conn = sqlite3.connect('BookAuthor.db')
        self.current = self.conn.cursor()
        
        
    def close_DB(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    #All read SQL

    def GetBook(self,book_name):
        self.open_DB()

        book=None
        sql= "SELECT * FROM Books WHERE Bookname='"+book_name+"'"
        res= self.current.execute(sql)

        if(res == None):
            return None
        
        res = res.split("|")

        self.close_DB()
        return book
    
    def GetAuthor(self, first_name, last_name):
        self.open_DB()

        author=None
        sql= "SELECT * FROM Authors WHERE Fname='"+first_name+"' AND Lname='"+last_name+"'"
        res= self.current.execute(sql)

        if(res == None):
            return None

        res = res.split("|")

        author = Author(res[0],res[1],res[2],res[3])

        self.close_DB()
        return author


    # def GetUser(self,username):
    #     self.open_DB()

    #     usr=None
    #     # sql= "SELECT ................ "
    #     res= self.current.execute(sql)

    #     self.close_DB()
    #     return usr

    def GetAuthors(self):
        pass
    def GetBooks(self):
        self.open_DB()
        books=[]
        self.close_DB()
        return books
    
    # def GetAccounts(self):
    #     pass
    # def GetUsers(self):
    #     self.open_DB()
    #     usrs=[]
    #     self.close_DB()
    #     return usrs

    def get_book_authors_nationality(self,book_name):
        pass

    def get_user_balance(self,username):
        self.open_DB()

        sql="SELECT a.Balance FROM Accounts a , Users b WHERE a.Accountid=b.Accountid and b.Username='"+username+"'"
        res = self.current.execute(sql)
        for ans in res:
            balance =  ans[0]
        self.close_DB()
        return balance


    #__________________________________________________________________________________________________________________
    #__________________________________________________________________________________________________________________
    #______end of read start write ____________________________________________________________________________________
    #__________________________________________________________________________________________________________________
    #__________________________________________________________________________________________________________________
    #__________________________________________________________________________________________________________________


    #All write SQL

    def insert_new_book(self, book_name, genre, price, author_id):
        self.open_DB()

        sql = "SELECT MAX(Bookid) FROM Books"
        res = self.current.execute(sql)
        if(res == None):
            res = '-1'
        new_id = res + 1

        sql = "INSERT INTO Books VALUES ("+str(new_id)+",'"+book_name+"','"+genre+"',"+str(price)+","+str(author_id)+")"


        self.close_DB()

    def insert_new_author(self, ):
        pass

    def update_user(self,user):
        self.open_DB()

        self.close_DB()
        return True

    def update_account(self,account):
        pass

    def delete_user(self,username):
        pass

    def delete_account(self,accountID):
        pass


def main_test():

    db = BookAuthorORM()

    book1 = Book("Harry Potter", "Fantasy", "1", 100)

    user1= User("Yos","12345","yossi","zahav","kefar saba","123123123","1111",1,'11')


    db.delete_user(user1.user_name)
    users = db.get_users()

    for u in users :
        print(u)


if __name__ == "__main__":
    main_test()


