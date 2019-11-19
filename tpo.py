CITIES = ['BS AS', 'La Plata', 'Corrientes', 'Cordoba', 'Salta', 'Puerto Madryn', 'Neuquen', 'Cachari', 'La Rioja']
DISTANCES = [
    [90, 100, 140, 500, 1, 100, 250, 100],
    [0, 70, 80, 90, 3, 20, 270, 90],
    [70, 0, 90, 100, 7, 10, 600, 70],
    [80, 90, 0, 3, 100, 80, 900, 50],
    [90, 100, 3, 0, 70, 80, 1000, 1],
    [3, 7, 100, 70, 0, 500, 1500, 3],
    [20, 10, 80, 80, 500, 0, 3, 200],
    [270, 600, 900, 1000, 1500, 3, 0, 100],
    [90, 70, 50, 1, 3, 200, 100, 0]
]


def alg(CITIES, DISTANCES):
    min_cost = 0
    result = ''
    partials = {}

    for i in range(len(CITIES)):
        combinations = 2**(i+1) - 2
        for j in range(combinations):  # range goes from zero to last number less one
            aux = bin(j+1)[2:].zfill(i+1)

            # stop iteration when found an already calculated result
            if partials.get(aux, False):
                break

            new_city = len(aux) - 2
            try:
                partial = partials[aux[1:]]
                a_or_b = aux[0]
                cost = 0
                if a_or_b == aux[1]:
                    cost = DISTANCES[len(aux)-2][new_city]
                else:
                    found = False
                    k = 2
                    while not found:
                        if a_or_b == aux[k]:
                            found = True
                        else:
                            k += 1

                    cost = DISTANCES[len(aux)-(k+1)][new_city]

                partials[aux] = partial + cost
            except KeyError:
                if i > 1:
                    # remove first and last
                    partial = partials[aux[1:-1]+aux[0]]
                    # only add the first city to the second one
                    partials[aux] = partial + DISTANCES[0][1]
                else:
                    partials[aux] = 0

            # Avoid recalculation for same paths
            partials[bin(combinations-j)[2:].zfill(i+1)] = partials[aux]

            if partials[aux] < min_cost or j == 0:
                result = aux
                min_cost = partials[aux]


    A, B = [], []
    index = 0
    for i in result[::-1]:
        if i == '0':
            B.append(CITIES[index])
        else:
            A.append(CITIES[index])
        index += 1
    
    print('A', A)
    print('B', B)
    print(min_cost)

alg(CITIES, DISTANCES)