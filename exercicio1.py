'''
    Faca um programa que peca ao usuario um numero inteiro, informe se este numero eh par ou impar e caso o usuario nao digite um numero inteiro,
    informe que nao eh um inteiro.
'''

try:
    numero = int(input("Digite um numero inteiro: "))
    if (numero % 2 == 0):
        print("Numero par")
    else:
        print("Numero impar")
except ValueError:
    print("Nao eh um numero inteiro")