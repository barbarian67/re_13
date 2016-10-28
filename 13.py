#!/usr/bin/env python 
#-*- coding: utf-8 -*-
# Programa que lea números desde el teclado hasta que se 
# introduzca un número negativo. Cuando eso ocurra mostrará
# la cantidad de números introducidos y el la suma de los mismos
suma = 0
cuenta = 0
numero = int(raw_input('Haz el favor de meter un número: '))
while numero >= 0:
	suma = suma + numero
	cuenta = cuenta + 1
	numero = int(raw_input('Haz el favor de meter un número: '))
print 'La cuenta es', cuenta
print 'La suma es',suma



li = ['urrrrllll', 'Jaime', 123, 165, True]
for elemento in li:
	print elemento
	
	
	
nus = [1,2,3,4,45,456,543,78]	
suma = 0
for ele in nus:
	# suma = suma + ele
	suma += ele
print suma

ca = 'pakito'
for letra in ca:
	print letra
tu = ('urrrrllll', 'Diego', 123, 165, False)
for ele in tu:
	print ele



