spar = 0
simpar = 0
contimpar = 0
promimpar = 0
print("Cuantos numeros desea ingresar?")
num = int(input())
if num >= 0:
    for i in range(1, num+1):
        print("Ingrese un numero")
        x = int(input())
        if x == 0:
            print("Valor neutral, no cuenta")
        elif x % 2 == 0:
            spar = spar + x
        else:
            simpar = simpar + x 
            contimpar = contimpar + 1
else:
    print("Ingrese un numero positivo")
promimpar = simpar/contimpar
print("La suma de los numeros pares es: ", spar)
print("El promedio de los numeros impares es: ", promimpar)

