"""
numero_sorteado = 10 

numero_escolhido = int(input('Informe seis números entre 1 e 60: '))

while numero_escolhido != numero_sorteado:
    print('Você errou o número, tente outro ano!')  

    numero_escolhido = int(input('Informe um número entre 1 e 60: '))   

print('Você ganhou um premio ')
"""

import random

# Gerar um número sorteado aleatório entre 1 e 60
numero_sorteado = 10
numero_sorteado = 15
numero_sorteado = 20
numero_sorteado = 30
numero_sorteado = 49
numero_sorteado = 55
print(f"Número sorteado (para referência): {numero_sorteado}")

# Solicitar ao usuário que informe 6 números entre 1 e 60
numeros_escolhidos = []
for i in range(6):
    numero_escolhido = int(input(f'Informe o número entre 1 e 60'))
    numeros_escolhidos.append(numero_escolhido)

# Verificar se algum dos números escolhidos corresponde ao número sorteado
if numero_sorteado in numeros_escolhidos:
    print('Parabéns! Você ganhou um premio')
else:
    print('Você não acertou o número sorteado. Tente novamente outro ano!')

# Foi usado um for para fazer um tipo de programa para o usuário poder colocar o valor escolhido    
