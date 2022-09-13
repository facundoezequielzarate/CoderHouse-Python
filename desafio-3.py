#####     CONSIGNA NUMERO 1     #####

#Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú

#Mostrar una suma de los dos números
#Mostrar una resta de los dos números (el primero menos el segundo)
#Mostrar una multiplicación de los dos números
#Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
#En caso de no introducir una opción válida, el programa informará de que no es correcta.

A = 64
B = 5

print (A + B)

print (A - B)

print (A * B)



#####     CONSIGNA NUMERO 2     #####

#Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar
#debe repetirse el proceso hasta que lo introduzca correctamente.

mi_numero = input ("ingresar número")

# print (f/h ("par")) if mi_numero %2 == 0 else print ("impar")

#####     CONSIGNA NÚMERO 3     #####
#Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:


for n in range (0, 15, 1):
 if n % 2 == 1:
    print (n)
