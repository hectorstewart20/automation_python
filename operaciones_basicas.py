from random import randint, uniform,random
def ingresar_num():
    nombre = int(input("ingrese SU NOMBRE, POR FAVOR: "))
    num = int(input("ingrese un numero: "))
    return num

opor = 1
gano = False
num_aleatorio = randint(0,100)
while gano == False:
    mi_numero = ingresar_num()
    if mi_numero == num_aleatorio:
        gano = True
        print("El numero era: ", mi_numero)
        print("Haz acertado en la oportunidad ", opor)
    if mi_numero > num_aleatorio:
        opor = opor + 1
        print("El numero QUE introdujiste es MAYOR: ")
    if mi_numero < num_aleatorio:
        opor = opor + 1
        print("El numero QUE introdujiste es MENOR: ")