# declaramos la clase alumno
class alumno:
    # declaramos el metodo __init__
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.nota=int(input("Ingrese la nota: "))
 
    # declaramos el metodo calificaciones
    def calificaciones(self):
        if self.nota >= 3:
          print("El alumno ",self.nombre," con su nota ",self.nota,"APROBO")
        else:
          print("El alumno ",self.nombre," con su nota ",self.nota,"REPROBO")
 
# bloque principal
alumno1=alumno()
alumno1.calificaciones()
