# client.py

import socket                   # Import socket module
from threading import Thread
import threading
import time
class Client(Thread):
    def __init__(self, rtt, chunksize):
        Thread.__init__(self)
        print(threading.currentThread().getName(), 'Starting_ client_1')
        self.rtt = rtt
        self.chunksize = chunksize

    def run(self):
        s = socket.socket()             # Create a socket object
        host = socket.gethostname()     # Get local machine name
        port = 60001                    # Reserve a port for your service.
        s.connect((host, port))
        s.send("Hello server!".encode())
        time.sleep(1)

        with open('received_file', 'wb') as f:
            print('file opened')
            while True:
                print('receiving data...')
                data = s.recv(1024)
                print('data=%b', (data))
                if not data:
                    break
                # write data to a file
                f.write(data)

        f.close()
        print('Successfully get the file')
        s.close()
        print('connection closed')

