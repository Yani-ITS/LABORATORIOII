print("El siguiente programa realiza la suma de los numeros que se encuentran entre dos valores dados")
suma = 0 #Declaro la variable suma en 0 donde se almacena el resultado.

#Solicito al usuario los valores
numero1 = int(input("Ingrese un valor: "))
numero2 = int(input("Ingrese un valor: "))

""""de los valores ingresados verifico cuál es el mayor
    ya que de eso depende el orden para poder sumar
    Aclaracion: Es una solución no quiere decir que sea la unica!!
"""
if(numero1>numero2):
    desde = numero2
    hasta = numero1
else:
    desde = numero1
    hasta = numero2

#Realizo la suma para ello utilizo la variable suma que es el acumulador.

while(desde<hasta):
    suma = suma+desde
    desde = desde+1

print("La suma de los valores es: {}".format(suma))