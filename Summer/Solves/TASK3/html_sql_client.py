__author__ = 'Eyal Keysar'

import serverAPI

import threading


def manu():
    print ("1. Update User\n" + \
          "2. Insert User\n" + \
          "3. Delete User\n" + \
          "4. Get All Users\n>" +\
          "9. exit\n\n>")

    data = input("Enter Num> ")

    if data == "9":
        return "q"
    elif data == "1":
        name = input("Enter name > ")
        password = input("Enter name > ")
        #
        #
        #
        return "UPDUSR|" + name + "|" + password + "|yossi|zahav|kefar saba|123123123|a@net.il|0"
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
        data = server.recv()

        if data =="":
            print ("seems server dissconnected")
            break

        print ("Got>>" + data)

if __name__ == "__main__":
    main()
    
