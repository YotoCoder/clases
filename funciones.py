
def funcion_suma(a: int, b: int) -> int:

    return (a + b)

# a = int(input('Ingrese el primer valor a sumar: '))
# b = int(input('Ingrese el segundo valor a sumar: '))

def saludo(nombre: str) -> str:

    if(nombre == 'admin'):
        return 'Acceso valido'
    elif(nombre == 'henry'):
        return 'Acceso restringido'

    return f'el usuario no existe'

print( saludo('otro usuario') ) 