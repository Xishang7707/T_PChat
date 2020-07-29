import socket
import _thread
import time

class socketclient:

    __host = ''
    __port = 0
    __socket = 0
    def __init__(self, host, port):
        self.__host = host
        self.__port = port

    def __init_connect(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.__socket.connect((self.__host, self.__port))
        self.__thread_ping()
        pass

    def __thread_ping(self):
        _thread.start_new_thread(self.__ping, ())

    def __ping(self):
        while True:
            time.sleep(5)
            self.__socket.send('ping'.encode('utf-8'))

    def start(self):
        self.__init_connect()

        msg = self.__socket.recv(1024)
        print(msg.decode('utf-8'))
        # while True:
        #     clientsocket, clientaddr = self.__socket.accept()
        #     print("连接地址: %s" % str(clientaddr))
        #
        #     msg = '欢迎访问菜鸟教程！' + "\r\n"
        #     clientsocket.send(msg.encode('utf-8'))
        #     clientsocket.close()
        #     pass
        # pass
    pass