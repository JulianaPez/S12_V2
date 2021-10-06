from conexionDB import connetDB

def consultarContactos():
    conn = connetDB()
    conts = []
    with conn.cursor() as cursor:
        sql = "SELECT * FROM misiontic.contactos;"
        cursor.execute(sql)
        conts = cursor.fetchall()
    return conts


