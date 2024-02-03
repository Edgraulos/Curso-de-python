# E o desafio 03 era:
# Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

# O codigo usado foi:

import sys

# Função para verificar se B corresponde aos últimos dígitos de A
def verifica_encaixe(A, B):
    if A[-len(B):] == B:
        return "encaixa"
    else:
        return "nao encaixa"

# Lê o número de casos de teste
N = int(sys.stdin.readline())

# Itera sobre os casos de teste
for _ in range(N):
    # Lê os valores A e B
    A, B = sys.stdin.readline().split()

    # Obtém o resultado e imprime
    resultado = verifica_encaixe(A, B)
    print(resultado)