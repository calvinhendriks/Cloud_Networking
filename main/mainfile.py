from main.server import Server
from main.client import Client
from threading import Thread


if __name__ =='__main__':
    s = Server(100,4)
    c = Client(100,4)
    ss = Thread(name = 'test' , target = s.start())
    cc = Thread(name = 'client', target = c.start())