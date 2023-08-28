__author__ = 'Eyal keysar'
import socket
import SQL_ORM

from constants import *

import queue, threading,time, random
from  tcp_by_size import send_with_size ,recv_by_size
DEBUG = True
exit_all = False




def handl_client(sock , tid, db):
    global exit_all
    
    print("New Client num " + str(tid))
    
    while not exit_all:
        try:
            data = recv_by_size(sock).decode()
            print("data from client:" + data)
            if data == "":
                print("Error: Seems Client DC")
                break
            to_send = do_action(data ,db)
            send_with_size(sock,str(to_send))

        except socket.error as  err:
            if err.errno == 10054:
                #'Connection reset by peer'
                print("Error %d Client is Gone. %s reset by peer." % (err.errno,str(sock)))
                break
            else:
                print("%d General Sock Error Client %s disconnected" % (err.errno,str(sock)))
                break

        except Exception as err:
            print("General Error:", str(err))
            break
    sock.close()


def do_action(data , db):
    """
    check what client ask and fill to send with the answer
    """
    to_send = "Not Set Yet"
    action = data[:6]
    data = data[7:]
    print("doing action on:" + action + " data:" + data)
    fields = data.split('|')

    if DEBUG:
        print("Got client request " + action + " -- " + str(fields))


    if action == "ADDAUT":
        if(len(fields) != 3):
            to_send = "ERR___R|001|" + " not enogh fields"
            return to_send
        
        new_author = SQL_ORM.Author(fields[0],fields[1],fields[2])
        res = db.insert_new_author(new_author)
        print("insert new author :" + str(new_author))
        
        if res != True:
            to_send = "ERR___R|002|" + " insert new author failed"
            return to_send
        to_send = "ADDAUTOK"

    elif action == "GETAUT":
        to_send = db.get_authors_as_strings()

    elif action == "GETBOK":
        to_send = db.get_books()

    elif action == "ADDBOK":
        if(len(fields) != 4):
            to_send = "ERR___R|001|" + " not enogh fields"
            return to_send
        new_book = SQL_ORM.Book(fields[0],fields[1],fields[2],fields[3])
        res = db.insert_new_book(new_book)
        print("insert new book :" + str(new_book))

        if res != True:
            to_send = "ERR___R|002|" + " insert new book failed"
            return to_send
        to_send = "ADDBOKOK"

    elif action == "RULIVE":
        to_send = "RULIVER|"+ "yes i am a live server"

    else:
        print("Got unknown action from client " + action)
        to_send = "ERR___R|001|"+ "unknown action"

    return to_send




def q_manager(q,tid):
    global exit_all
    
    print("manager start:" + str(tid))
    while not exit_all:
        item = q.get()
        print("manager got somthing:" + str(item))
        # do some work with it(item)


        q.task_done()
        time.sleep(0.3)
    print("Manager say Bye")
    


def main():
    global exit_all
    
    exit_all = False

    db = SQL_ORM.BookAuthorORM() # Bros just called it ORM
    db._drop_tables()
    db._create_tables()
    
    s = socket.socket()
    
    q = queue.Queue()

    q.put("Hi for start")
    
    
    manager = threading.Thread(target=q_manager, args=(q, 0))
    
    s.bind(("0.0.0.0", SERVER_PORT))
    s.listen(4)
    print("after listen")

    threads = []
    i = 1
    while True:
        cli_s , addr = s.accept()
        t = threading.Thread(target =handl_client, args=(cli_s, i,db))
        t.start()
        i+=1
        threads.append(t);



    exit_all = True
    for t in threads:
        t.join()
    manager.join()
    
    s.close()



if __name__ == "__main__":
    main()
