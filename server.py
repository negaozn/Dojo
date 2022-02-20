import socket
from datetime import datetime
from sys import exit

class Server:
    def __init__(self):
        self.host = ''
        self.port = 5000
        self.tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = (self.host,self.port)
    
    def Criar(self,msg,ip):
        data = datetime.now()
        try:
            file = open('C:\\Temp\\log-%s-%s %s.txt' % (data.day,data.hour,ip),'a')
            file.write('%s' % msg)
            file.close()
        except OSError as e:
            print(e)

    def Start(self):
        self.tcp.bind(self.server)
        self.tcp.listen(1)
        while True:
            con, cliente = self.tcp.accept()
            print('Concetado por %s' % cliente[0])
            while True:
                msg = con.recv(1024).decode('utf-8')
                if not msg: break
                if 'url' in msg:
                    self.Criar(msg,cliente[0])
                    print(msg)
                if msg == 'exit': break
            print('Finalizando conexao do %s ' % cliente[0])
            con.close()
            break
    


if __name__ == '__main__':
    s = Server()
    s.Start()
    #exit()