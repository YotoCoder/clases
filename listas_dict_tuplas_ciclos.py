lista = [1,2,3,]

diccionario = {
    'uno': 1,
    'dos': 2,
    'tres': 3,
    'cuatro': 4,
}

tupla = (
    'lunes',
    'martes',
    'miercoles',
)

''' for i in tupla:
     print(i)
'''

estado = True
intentos = 1

while estado:

    nombre = input('Ingrese el nombre: ')

    if(nombre == 'admin'):
         print('Acceso valido')
         estado = False

    elif nombre == 'henry':
         print('Acceso restringido')
         estado = False

    elif(intentos >= 3):
        estado = False

    intentos += 1

    print( f'el usuario no existe, te quedan {4 - intentos} intentos')
