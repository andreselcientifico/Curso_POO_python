import random


def busqueda_lineal(lista, objetivo):
    match =False

    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break

    return match

if __name__ == '__main__':
    tamaño_de_lista = int(input('De que tamaño sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0,1000000) for i in range(tamaño_de_lista)]

    
    encontrado = busqueda_lineal(lista, objetivo)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    