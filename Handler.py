import socket
def Servidor(host = 'localhost' , port = 443):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_address = (host,port)
    print("Servidor iniciado em %s na porta %s" % server_address)
    server.bind(server_address)
    server.listen(10)
    i = 0
    
