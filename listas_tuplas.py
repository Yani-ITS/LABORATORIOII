 #Solicitar al usuario que ingrese números, los cuales se guardarán en una lista.
#Finalizar al ingresar el número 0, el cual no debe guardarse.

lista = []
 
valor = int(input("ingrese un valor "))
 
while valor!= 0:
   lista.append(valor)
   valor = int(input("ingrese un valor "))

print(lista)

#a. A continuación, solicitar al usuario que ingrese un número y, si el
#número está en la lista, eliminar su primera ocurrencia. Mostrar un
#mensaje si no es posible eliminar.  

numero= int(input(" ingrese un numero "))

if numero not in lista:
    print("no se borra")
else:
    lista.remove(numero)

print(lista)

#b. Recorrer la lista para imprimir la sumatoria de todos los elementos.

largo=len(lista)

suma=0
i=0

while i<largo:
    suma=suma+lista[i]
    i=i+1

print("la suma es: " ,suma)

#c. Solicitar al usuario otro número y crear una lista con los elementos de la
#lista original que sean menores que el número dado. Imprimir esta
#nueva lista, iterando por ella.

otroValor= int(input(" ingrese otro numero "))
nuevalista=[]
i=0

while i<largo:
    if otroValor>lista[i]:
        nuevalista.append(lista[i])
        
    i=i+1
        
print("la nueva lista es ", nuevalista)

#d. Generar e imprimir una nueva lista que contenga como elementos a
#tuplas de dos elementos, cada una compuesta por un número de la lista
#original y la cantidad de veces que aparece en ella. Por ejemplo, si la
#lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1),
#(2,2), (57,1)]

