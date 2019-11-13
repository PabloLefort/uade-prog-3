# 1. Utilice el algoritmo de búsqueda binaria para diseñar un algoritmo que encuentre para un número entero positivo x el valor b = ⌊√x⌋ en O(log n).


def finder(x: int, numbers: list):
    half = int(len(numbers) / 2)
    squared = numbers[half]**2
    if squared == x:
      return numbers[half]
    elif len(numbers) == 2:
      return -1
    elif squared < x:
      return finder(x, numbers[half:])
    else:
      return finder(x, numbers[:half])


a = [1,2,3,4,5,6,7,8,9]

print(finder(4, a))
print(finder(25, a))
print(finder(49, a))
print(finder(48, a))
print(finder(1, a))


'''
a = 1
b = 2
k = 0

substraccion

o(n^k)              si a < 1
o(n^k+1)            si a = 1
o(n^k a^ndivb)      si a > 1


division
o(n^k)              si a < b^k
o(n^k logn)         si a = b^k
o(n^logba)          si a > b^k



=> division, 1 = 2^0 => segundo caso => o(n^k logn) => o(n^1 logn) = o(logn)

'''