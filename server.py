import socket
from socket import *
from _thread import *
import pickle
from game import Game


server = '127.0.0.1'
port = 7228

s = socket(AF_INET, SOCK_STREAM)

try:
    s.bind((server, port))
except s.error as e:
    str(e)

s.listen(5)
print("Waiting for a connection, Server Started")

games = {}
ThreadCount = 0


def threaded_client(conn, p, gameId):
    global ThreadCount
    conn.send(str.encode(str(p)))
    print("player : ", p)

    reply = ""
    while True:
        try:
            # row, col = [int(i) for i in c.recv(10).decode('utf-8').split('\n')]

            data = conn.recv(10).decode()
            if(('\n') in data):
                row, col = [int(i) for i in data.split('\n')]
            if (data != "get"):
                print("eiiih from player :", p)
            if gameId in games:
                game = games[gameId]
                #print("outside if No data then break here : ", data)

                if not data:
                    print("No data then break here : ", data)
                    break
                else:
                    if data == "reset":
                        game.resetWent()

                    elif (data != "get") :
                        game.set_move(p, row, col)
                
                    #print("before sendall : ", pickle.dumps(game))
                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection from player", p)
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    ThreadCount -= 1
    print("hell I am thread count",ThreadCount)
    conn.close()

while True:
    conn, address = s.accept()
    print('Connect to: ' + address[0] + ':' +str(address[1]))

    ThreadCount += 1
    p = 0
    gameId = (ThreadCount - 1)//2
    if ThreadCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (conn, p, gameId))