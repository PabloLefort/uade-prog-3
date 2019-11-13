import copy

CITIES = ['BS AS', 'La Plata', 'Corrientes', 'Cordoba']
DISTANCES = [
    [90, 100, 140],
    [0, 70, 80],
    [70, 0, 90],
    [80, 90, 0]
]


CITIES = ['BS AS', 'La Plata']


'''
complejidad minima!!! 2^(n-1) - 1
- cantidad de ciudades / 2 -> recorrido para cada vector: 5 ciudades = 2.5 => int(2.5+1) = 3. MEDIO
- recorrer la matriz armando las combinaciones. Siendo para el primero c[i->MEDIO+j] = A, c[MEDIO->n-1] = B. j=-1
- i+1. En B agregar en orden. j si se pasa de n => j=n
- 


- recorrer ciudades hasta completar los dos caminos
- obtener siguiente ciudad
- agregar a ambos caminos siendo 3 o 4 combinaciones posibles
- calcular costo de las combinaciones
- actualizar caminos con la mejor combinacion
'''

def distance(paths):
    paths_length = len(paths)
    if paths_length == 0 or paths_length == 1:
        return 0
    else:
        aux = 0
        size = len(paths)
        for i in range(size):
            if (i+1) < size:
                aux += DISTANCES[paths[i]][paths[i+1]-1]
        return aux


def alg():

    A, B = [], []
    aux_A, aux_B = [], []
    for i in range(len(CITIES)):
        #print(i)
        #next_city = CITIES.pop(0)
        CITIES.pop(0)

        # add to A
        aux_A = copy.deepcopy(A)
        aux_A.append(i)

        # add to B
        aux_B = copy.deepcopy(B)
        aux_B.append(i)

        if len(aux_A) == 1:
            A = aux_A
            continue
        elif distance(aux_A) + distance(B) < distance(A) + distance(aux_B):
            A = aux_A
        else:
            B = aux_B

        # take last from A, send to B, add to A
    
    print(A)
    print(B)


#alg()




def combineta():
    A = []
    B = []

    a = 1
    b = len(CITIES)

    for i in range(b):
        if i >= 1:
            B = CITIES[:i]

        B += CITIES[i+1:]
        print(f'A = [{CITIES[i]}], B = [{B}]')
        B = []