'''
 Testando a funcao id() do Python
'''

variavel = 13

print(variavel)
print(id(variavel))
    ## Saida: 140703824364712
"""
    Eh interessante salientar que independente de quantas vezes voce rode o programa o pID (process id)
    sempre sera o mesmo ja que a variavel esta guardada no mesmo espaco da memoria e nao se modifica
"""