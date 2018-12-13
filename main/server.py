# server.py

import socket                   # Import socket module
from threading import Thread
import threading
import time

class Server(Thread):
    def __init__(self, rtt, chunksize):
        Thread.__init__(self)
        print(threading.currentThread().getName(), 'Starting_ client_2')
        self.chunksize = chunksize
        self.rtt = rtt

    def run(self):
        s = socket.socket()             # Create a socket object
        host = socket.gethostname()     # Get local machine name
        port = 60001                    # Reserve a port for your service.

        s.bind((host, port))            # Bind to the port
        s.listen(5)                     # Now wait for client connection.

        print('Server listening....')
        time.sleep(1)
        while True:
            conn, addr = s.accept()     # Establish connection with client.
            print ('Got connection from', addr)
            data = conn.recv(1024)
            print('Server received', repr(data))

            filename='mytext.txt'
            f = open(filename,'rb')
            l = f.read(1024)
            while (l):
                conn.send(l)
                print('Sent ',repr(l))
                l = f.read(1024)
            f.close()

            print('Done sending')
            conn.send('Thank you for connecting'.encode())
            conn.close()

