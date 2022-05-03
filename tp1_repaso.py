num1= int(input("ingrese un numero: "))
num2= int(input("ingrese otro numero: "))

suma= 0

while (num1!=num2):
    if (num1<num2):
        suma = suma+num1
        num1=num1+1
    else:
        suma = suma+num2
        num2=num2+1

print("La suma de los valores es: {}".format(suma))