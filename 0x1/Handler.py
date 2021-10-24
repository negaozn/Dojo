import socket
from datetime import datetime
def Servidor(host = 'localhost' , port = 8080):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    data_payload = 2048
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_address = (host,port)
    print("Servidor iniciado em %s na porta %s" % server_address)
    server.bind(server_address)
    server.listen(10)
    i = 0
    while True:
        client,address = server.accept()
        data = client.recv(data_payload)
        if data:
            print("Data: %s" % data.decode('utf-8'))
            client.send(data)
            #print("enviando %s bytes de volta para %s " % (data,address))
            if 'Dojo' in str(data):
                agora = datetime.now()
                nome = 'log-%s-%s %s-%s.txt' % (agora.day,agora.hour,agora.minute,address[0])
                arquivo = open('C:\\temp\\%s' % nome,'w')
                arquivo.write(data.decode('utf-8'))
                arquivo.close()



Servidor()