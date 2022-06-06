# declaramos la clase calculadora
class Calculadora:
    # declaramos el metodo __init__
    def __init__(val):
      val.num1 = int(input("Ingrese un primer valor: "))
      val.num2 = int(input("Ingrese un segundo valor: "))
 
    # declaramos el metodo mostrar
    def mostrar(val):
      print("Valor 1: ",val.num1)
      print("Valor 2: ",val.num2)
 
    # operaciones
    def operaciones(val):
      suma = val.num1 + val.num2
      resta = val.num1 - val.num2 
      multip = val.num1 * val.num2 
      division = val.num1 / val.num2 
      print("Suma: ",val.num1," + ",val.num2," = ",suma)
      print("Resta: ",val.num1," - ",val.num2," = ",resta)
      print("Multiplicación: ",val.num1," x ",val.num2," = ",multip)
      print("División: ",val.num1," / ",val.num2," = ",division)
# bloque principal
calculadora = Calculadora()
calculadora.mostrar()
calculadora.operaciones()
