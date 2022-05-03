num1= int(input("ingrese un numero: "))
num2= int(input("ingrese otro numero: "))

suma= 0

if (num1<num2):
    suma = num1+num2
    num1=num1+1
else:
    suma = num2+num1
    num2=num2+1

print("la suma es " +suma)