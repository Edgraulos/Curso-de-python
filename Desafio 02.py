#Já o desafio 02 era:
#Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

#O codigo usado foi:

import sys

def numero_para_mes(numero):
    meses = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    return meses[numero - 1]

# Lê a entrada como um valor inteiro
numero_mes = int(sys.stdin.readline())

# Obtém o nome do mês correspondente
nome_mes = numero_para_mes(numero_mes)

# Imprime o resultado com a primeira letra maiúscula
print(nome_mes.capitalize())
