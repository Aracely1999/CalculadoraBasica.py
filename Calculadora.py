def agregar(a, b):
    return a + b 
def sustraer(a, b):
    return a - b 
def multiplicacion(a, b):
    return a * b 
def division(a, b):
    return a / b 

print("por favor, seleccione su operacion:")
print("1- Agregar")
print("2- Sustraer")
print("3- Multiplicacion")
print("4- Division")

while True:
    eleccion= input("Por favor, Ingrese su eleccion ( 1| 2| 3| 4)")
    if eleccion in ('1' ,'2', '3' ,'4'):
        num1= float(input("Por favor, Introduzca su primer numero:"))
        num2= float(input("Por favor, Introduzca su segundo numero:"))
        if eleccion == '1':
            print(f"{num1} + {num2} = " , agregar(num1, num2))
        elif eleccion == '2':
            print(f"{num1} - {num2} = " , sustraer(num1, num2))
        elif eleccion == '3':
            print(f"{num1} * {num2} = " , multiplicacion(num1, num2))
        elif eleccion == '4':
            print(f"{num1} / {num2} = " , division(num1, num2))
            

    else:
        print("Tu eleccion no es valida.")

    keep_running= input("Te gustaria continuar? si o no?")
    if keep_running in ('si', 'Si', 'SI'):
        continue
    else:
        break
     