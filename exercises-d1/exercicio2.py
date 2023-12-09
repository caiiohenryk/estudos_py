"""
    Faca um programa que pergunte ao usuario o horario e retorne a saudacao apropriada. ex: boa tarde, boa noite.
"""
try:
    horario = int(input("Digite que horas sao: "))
except ValueError:
    print("Voce digitou algo que nao representa um horario")



def saudacao(horario):
    if horario >= 0 and horario <= 11:
        return f"Bom dia, sao {horario} horas"
    elif horario >= 12 and horario <= 17:
        return f"Boa tarde, sao {horario} horas"
    elif horario >= 18 and horario <= 23:
        return f"Boa noite, sao {horario} horas"

print(saudacao(horario))