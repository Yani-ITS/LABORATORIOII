#Crea una tupla con los meses del año, pide números al usuario, si el numero
#esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa
#posición sino muestra un mensaje de error

tupla_meses=("","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
             "Agosto","Septiembre","Octubre","Noviembre","Diciembre")

numero= int(input("ingrese un numero: "))

if numero<13:
    print("mes: ", tupla_meses[numero])
else:
    print("solo hay 12 meses.")