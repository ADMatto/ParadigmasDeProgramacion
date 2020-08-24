#Ejercicio 1
#
# Crear un programa que imprima por pantalla el mensaje “Hello World!”.
#
def ejercicio1():
	print("Hello World")
# Nota: se puede imprimir el dato puro o el dato almacenado en una variable, siempre es una buena práctica usar variables.

# Ejercicio 2
#
# Crear un programa que imprima por pantalla todos los números pares del 0 al 100.
def ejercicio2():
	numero = 0
	for i in range(0,101,2):
		if i % 2 == 0:
			print(i)
			numero += 1
		
# Ejercicio 3
#
# Crear un programa que imprima por pantalla todos los números del 0 al 100 que sean divisibles por 3.
def ejercicio3():
	numero = 0
	for i in range(0,101):
		if i % 3 == 0:
			print(i)
			numero += 1
		

# Ejercicio 4
# Crear un programa que pida al usuario que ingrese dos números y luego el programa imprima por pantalla: en un renglón la suma de ellos, en otro la resta y en otro el producto.
def ejercicio4():
	numero1 = int(input("Ingrese el primer numero: "))
	numero2 = int(input("Ingrese el segundo numero: "))
	print(f"{numero1} + {numero2} = {numero1 + numero2}")
	print(f"{numero1} - {numero2} = {numero1 - numero2}")
	print(f"{numero1} x {numero2} = {numero1 * numero2}")

# Ejercicio 5
#
# Crear un programa que pida al usuario 10 números enteros, los almacene en una lista, ordene los números dentro de la lista y luego imprima por pantalla la lista completa y ordenada.

def ejercicio5():
	numero = 0
	lista_numero = []
	for i in range(10):
		numero = int(input(f"Ingrese numero {i+1}: "))
		lista_numero.append(numero)
	lista_numero.sort()
	print(lista_numero)
		
# Ejercicio 6
#
# Crear un programa que le pida al usuario dos números enteros y luego: si el primero es mayor que el segundo, retorne 1, si el primero es menor que el segundo retorne -1 y si ambos números son iguales retorne 0.

def ejercicio6():
	numero1 = int(input("Ingrese el numero 1: "))
	numero2 = int(input("Ingrese el numero 2: "))
	if numero1 > numero2:
		print(1)
	elif numero1 == numero2:
		print(0)
	else: print(-1)
	
# Ejercicio 7
#
# Crear un programa que le pida al usuario ingresar dos números enteros y devuelva el punto medio entre ellos.
#

def ejercicio7():
	numero1 = int(input("Ingrese el numero 1: "))
	numero2 = int(input("Ingrese el numero 2: "))
	media = (numero1 + numero2) / 2
	print(media)

# Ejercicio 8
#
# Crear un programa que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.
#

def ejercicio8():
	lista_numero = [1,2,3,4,5,6,7,8,9,10]
	lista_pares = []
	lista_impares = []
	for numero in lista_numero:
		if numero % 2 == 0:
			lista_pares.append(numero)
		else: lista_impares.append(numero)
	print("Pares: ", lista_pares)
	print("Impares: ", lista_impares)

# Ejercicio 9
#
# Crear un programa que solicite al usuario que ingrese su dirección mail. Imprimir un mensaje indicando si la dirección es válida o no. Una dirección se considerará válida si contiene el símbolo "@".

def ejercicio9():
	email = input("Ingrese su Email: ")
	if "@" in email:
		print("Email Valido!")
	else: print("Email Invalido!")

# Ejercicio 10
#
# Crear un programa que dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

def ejercicio10():
	dni = input("Ingrese su DNI: ")
	digitos = len(dni)
	int(dni)
	if digitos == 7 or digitos == 8:
		print("DNI Valido!")
	else: print("DNI Invalido!")

# Ejercicio 11
#
# Crear un programa que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.

def ejercicio11():
	frase = input("Ingrese un texto: ")
	lista_palabra = frase.split()
	print(len(lista_palabra[-1]))

# Ejercicio 12
#
# En McDonald’s se pueden comprar patitas de pollo en 6, 9 o 20 unidades. Crear un programa que, a partir de un número, decida si es posible comprar esa cantidad de patitas.
#

def ejercicio12():
	numero = int(input("Numero de patitas de pollo a comprar: "))
	if (numero % 6 == 0 or numero % 9 == 0 or numero % 20 == 0) and numero != 0:
		print(f"Es posible comprar {numero} patitas")
	else: print(f"No es posible comprar {numero} patitas")

#
