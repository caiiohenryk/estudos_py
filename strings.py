# Tratamento de Strings

"""
    Strings sao imutaveis, ou seja, voce nao pode entrar no indice X
    de uma string e modifica-la manualmente, pra isso, voce deve criar
    OUTRA variavel pra que receba o valor novo.
"""

# Exemplo:

try:
    string = "Caio"
    string[2] = "F"
except TypeError:
    print("Try/except foi para o except\nErro de string")
    """
        string[2] = "F"
        ~~~~~~^^^
    TypeError: 'str' object does not support item assignment
    """

"""
 Porem, voce ainda pode mudar as letras de uma string ou muda-la usando funcoes ou formatacao,
 veja o exemplo:
"""

print(f'{string[:3]}ABC')

"""
 Nesse caso, a string nao foi modificada de fato, apenas printada de forma diferente
"""

