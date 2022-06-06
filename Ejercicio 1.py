# declaramos la clase persona
class Persona:
    # declaramos el metodo __init__
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))
 
 
    # declaramos el metodo mostrar
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
 
 
# declaramos la clase empleado
# la clase empleado hereda los atributos y metodos de la clase Persona
class Empleado(Persona):
    # declaramos el metodo __init__
    def __init__(self):
        # llamamos al metodo init de la clase padre
        # utilizamos la funcion super() para hacer referencia al padre
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo: "))
 
 
    # declaramos el metodo mostrar
    def mostrar(self):
        super().mostrar()
        print("Sueldo: ",self.sueldo)
 
 
    # declaramos el metodo descuento
    def descuento(self):
        if self.sueldo > 3600000:
          descuento = self.sueldo * 0.035
          total = self.sueldo - descuento
          print("El empleado cuenta con un descuento del 3.5%.")
          print("Su descuento es de: ",descuento)
          print("El total de su sueldo es de: ",total)
        else:
            print("El empleado no cuenta con descuento")
 
# bloque principal
persona1=Persona()
persona1.mostrar()
empleado1=Empleado()
empleado1.mostrar()
empleado1.descuento()
