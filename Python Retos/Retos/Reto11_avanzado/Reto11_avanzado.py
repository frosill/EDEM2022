'''
Reto 11: Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:
NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean).
El programa debe mostrar las siguientes opciones para que escoja el usuario:
(1) Añadir un cliente
(2) Eliminar cliente por NIF
(3) Mostrar Cliente por NIF
(4) Listar TODOS os clientes
(5) Mostrar ÚNICAMENTE los clientes preferentes
(6) Finalizar Programa
'''

seleccion = int(input('¡Bienvenido a la gestión de cartera de clientes! Seleccione una de las siguientes opciones para continuar:\n\n\t(1) Añadir un cliente\n\t(2) Eliminar cliente por NIF\n\t(3) Mostrar cliente por NIF\n\t(4) Listar todos los clientes\n\t(5) Mostrar todos los clientes preferentes\n\t(6) Finalizar programa\n\n Inroduzca su selección: '))

if seleccion == 6:
    print(f"\nHas seleccionado ({seleccion}): Programa finalizado")

