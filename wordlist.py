import itertools

#EX.: ABCDE
string = input('string para ser permutada: ')

#EX.: 3
tamanho = int(input('tamanho da permutação: '))

resultado = itertools.permutations(string, tamanho)

for letra in resultado:
    print(''.join(letra))