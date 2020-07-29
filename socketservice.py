import socket
import time
import _thread

class socketservice:

    class __client_connect_info:
        socket = 0
        ping_tick = 0
        def __init__(self, sock):
            self.socket = sock
            self.ping_tick = time.time()

    __port = 0
    __socket = 0
    __client_list = []

    __recv_event = None
    __connect_event = None
    def __init__(self, port):
        self.__port = port

    def __init_connect(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        host = socket.gethostname()
        self.__socket.bind((host, self.__port))
        self.__socket.listen(10)
        self.__ping_check()
        print(host, self.__port)
        pass

    def __thread_ping(self):
        while True:
            time.sleep(5)
            for client in self.__client_list:
                print(time.time()-client.ping_tick)
                if time.time()-client.ping_tick > 15:
                    self.__client_list.remove(client)
                    client.socket.close()
        pass

    def __ping_check(self):
        # try:
        _thread.start_new_thread(self.__thread_ping, ())
        # except:
        #     print("Error: 无法启动线程 __ping_check")
        pass

    def connect_event(self, call):
        self.__connect_event = call
        pass

    def recv_event(self, call):
        self.__recv_event = call
        pass

    def send(self, sock, data):

        pass

    def __recv(self, sock, addr):

        while True:
            data = sock.recv(1024)
            if data.decode('utf-8') == 'ping':
                for item_client in self.__client_list:
                    if item_client.socket == sock:
                        item_client.ping_tick = time.time()
                        break
            print(data.decode('utf-8'))
            if self.__recv_event != None:
                self.__recv_event(sock, data.decode('utf-8'))
        pass

    def __accept(self, sock, addr):
        self.__client_list.append(self.__client_connect_info(sock))

        if self.__connect_event != None:
            self.__connect_event(sock, addr)

        _thread.start_new_thread(self.__recv, (sock, addr))
        pass

    def start(self):
        self.__init_connect()

        while True:
            clientsocket, clientaddr = self.__socket.accept()

            self.__accept(clientsocket, clientaddr)
            pass
        pass
    pass