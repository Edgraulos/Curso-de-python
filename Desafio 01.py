#O  primeiro deasfio era o seguinte:
#O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua tarefa.

#O codigo usado no desafio:

import sys

def verifica_tuite(texto):
    if len(texto) <= 140:
        return "TWEET"
    else:
        return "MUTE"

# Lê a linha de entrada
linha_de_texto = sys.stdin.readline().rstrip()

# Obtém o resultado
resultado = verifica_tuite(linha_de_texto)

# Imprime o resultado
print(resultado)
