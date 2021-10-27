import socket,os
from datetime import datetime


class Handler:

    def __init__(self,host,port):
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.data_payload = 2048
        self.server_address = (host,port)

    def Servidor(self):
        #server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #data_payload = 2048
        self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        print("Servidor iniciado em %s na porta %s" % self.server_address)
        self.server.bind(self.server_address)
        self.server.listen(10)
        i = 0
        while True:
            client,address = self.server.accept()
            data = client.recv(self.data_payload)
            if data:
                print("Data: %s" % data.decode('utf-8'))
                client.send(data)
                #print("enviando %s bytes de volta para %s " % (data,address))
                if 'url:' in str(data):
                    agora = datetime.now()
                    nome = 'log-%s-%s %s-%s.txt' % (agora.day,agora.hour,agora.minute,address[0])
                    arquivo = open('C:\\temp\\handler\\%s' % nome,'a')
                    arquivo.write(data.decode('utf-8'))
                    arquivo.close()

if __name__ == "__main__":
    handler = Handler('localhost',8080)
    handler.Servidor()