class Usurio:

    def __init__(self, name, password, correo, profesion, telefono, ubicacion, rol):
        self.name = name
        self.password = password
        self.correo = correo
        self.profesion = profesion
        self.telefono = telefono
        self.ubicacion = ubicacion
        self.rol =rol

class biologo(Usuario):
   def __init__(self, credencial)
   self.credencial =credencial 
  
class administrador(Usuario):
   def __init__(self, permisos)
   self.permisos = permisos

  
class individuo:

    def __init__(self, id, clase, genero, familia, especie, ubicación, imagen):
        self.id = id
        self.clase = clase
        self.genero = genero
        self.familia = familia
        self.especie = especie
        self.ubicacion = ubicacion
        self. imagen= imagen  
