import pymysql

HOST = "localhost"
PORT = 3306
USER = "root"
PSS = "admin"
DB = "misiontic"

def connetDB():

    try:
        conn = pymysql.connect(host=HOST,port=PORT,user=USER,passwd=PSS,db=DB)
        print("Conectado")
        return conn
    except:
        print("No se pudo conectar")
        return conn

    