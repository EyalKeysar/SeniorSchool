__author__ = 'Eyal Keysar'

import serverAPI

import threading


def manu():
    print ( "1. Get All Authors             " + "2. Insert Author\n" + \
            "3. Get All Books               " + "4. Insert Book by author id\n" + \
            "5. Get Books by author id      " + "6. Get Books by author name\n" + \
            "7. Get Books by genre          " + "8. Get Books in price range\n" + \
            "9. Get Book by name            " + "10. Get Authors by nationality\n" + \
            "11. exit\n\n>")

    data = input("Enter Num> ")

    if data == "11":
        return "q"
    
    elif data == "1":
        return "GETAUT-"
    
    elif data == "2":
        first_name = input("Enter Authors first name > ")
        last_name = input("Enter Authors last name > ")
        nationality = input("Enter Authors nationality > ")
        return "ADDAUT-" + first_name + "|" + last_name + "|" + nationality
    
    elif data == "3":
        return "GETBOK-"
    
    elif data == "4":
        book_name = input("Enter Book name > ")
        genre = input("Enter Book genre > ")
        price = input("Enter Book price > ")
        author_id = input("Enter Book author id > ")
        return "ADDBOK-" + book_name + "|" + genre + "|" + price + "|" + author_id
    
    elif data == "5":
        return "GBBAID-" + input("Enter Author id > ")
    
    elif data == "6":
        return "GBBYAN-" + input("Enter Author first name > ") + "|" + input("Enter Author last name > ")
    
    elif data == "7":
        return "GBBGEN-" + input("Enter Book genre > ")
    
    elif data == "8":
        return "GBBPRI-" + input("Enter min price > ") + "|" + input("Enter max price > ")
    
    elif data == "9":
        return "GBBNAM-" + input("Enter Book name > ")
    
    elif data == "10":
        return "GANATI-" + input("Enter Nationality > ")

    else:
        return "RULIVE"


def main():

    server = serverAPI.ServerAPI()

    server.connect()


    while True:
        data = manu()

        if data == "q":
            break

        server.send(data)

        data = server.recv().decode()

        if data =="":
            print ("seems server dissconnected")
            break

        print ("Got>>" + data)

if __name__ == "__main__":
    main()
    
