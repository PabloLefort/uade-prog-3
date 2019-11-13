# 2. Suponga que v es un vector de n numeros binarios ordenados. Encuentre un algoritmo eficiente que determine la cantidad de unos en v.
# Ejemplo. Si v = [0,0,0,1,1,1,1,1] (aqui n = 8). El programa deberia retorna 5, que es la cantidad de unos en v.


def counter(numbers: list):
    length = len(numbers)
    half = int(length / 2)
    if length == 2:
        if numbers[half] == 1:
            return 1
        else:
            return 0
    if numbers[half] == 1:
        return half + counter(numbers[:half])
    else:
        return counter(numbers[half:])


'''
[0,0,0,1,1,1,1,1] = 4 + recursive
[0,0,0,1,1,1,1] = 3

half 


'''
a = [0,0,0,1,1,1,1,1]
print(counter(a))