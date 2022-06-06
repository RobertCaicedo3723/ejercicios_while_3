print("---------------------------------------")
print("--------Calcular 1/5 de H--------------")
print("---------------------------------------")

#Input

h = int(input("Ingrese el numero de robotes: "))

#Procesing

q = h/5
n = 0

while h>q:
    h = h-0.1*h
    n = n+1
    print("La altura que disminuye es: " + str(h))
    print("La altura que aumenta es: " + str(n))





#Output

input("El numero de robotes antes de alcanzar 1/5 partes de h es: " + str(n))

