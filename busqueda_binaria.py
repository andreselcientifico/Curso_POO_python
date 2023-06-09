import random
import time

def busqueda_binaria(lista,comienzo,final,objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final-1]}')
    if comienzo > final:
        return False
    medio = (comienzo + final)// 2
    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista,medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo,medio -1, objetivo)
    
    



if __name__ == '__main__':
    tamaño_de_lista = int(input('De que tamaño sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0,1000000) for i in range(tamaño_de_lista)])

    comienzo = time.time()
    encontrado, final = busqueda_binaria(lista, 0, len(lista), objetivo) ,time.time()
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(final-comienzo)