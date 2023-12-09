"""
Repeticoes
Iniciando os estudos com while
"""

while True:
    nome = (input('Qual seu nome?')).lower()
    print(f'Seu nome eh {nome}')
# Laco de repeticao infinito
    if nome == "sair":
        break
        # Break pra quebrar o laco de repeticao quando for digitado 'sair'