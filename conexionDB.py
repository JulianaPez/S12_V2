###CONEXION BASE DE DATOS###
import pymysql

HOST = "localhost"
PORT = 3306
USER = "root"
PSS = "admin"
DB = "colecciones"

def connetDB():

    try:
        conn = pymysql.connect(host=HOST,port=PORT,user=USER,passwd=PSS,db=DB)
        print("Conectado")
        return conn
    except:
        print("No se pudo conectar")
        return conn
    
###INSERTAR FILAS###
cursor = db.cursor()
sql = "INSERT INTO individuo(id, clase, genero, familia, especie, ubicación, imagen ) \
   VALUES (NULL,'{0}','{1}','{2}','{3}','{4}','{5}')".format("clase", "genero", "familia", "especie", "ubicación", "imagen")  #valores cambiaran en cada fila#
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()

###LEER BASE DE DATOS###
cursor = db.cursor()

sql = "SELECT * FROM individuo \
WHERE id > {0}".format(0)
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
   id = row[0]
   clase= row[1]
   genero= row[2]
   familia= row[3]
   especie= row[4]
   ubicacion= row[5]
   imagen= row[6]
   print ("id = {0}, clase= {1}, genero= {2}, familia= {3}, especie= {4}, ubicación= {5}, imagen= {6}".format(id, clase, genero, familia, especie, ubicación, imagen))
db.close()
