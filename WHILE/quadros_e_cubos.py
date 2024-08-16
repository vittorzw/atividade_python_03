# Inicializa o número inicial
numero = 0

# Imprime o cabeçalho
print("nro\tquad\tcubo")

# Laço while para calcular e exibir os quadrados e cubos
while numero <= 50:
    quadrado = numero ** 2
    cubo = numero ** 3
    # Imprime o número, o quadrado e o cubo com separação por tabulação
    print(f"{numero}\t{quadrado}\t{cubo}")
    # Incrementa o número para a próxima iteração
    numero += 1
