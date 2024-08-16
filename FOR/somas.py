# Solicita ao usuário dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Lista para armazenar os resultados das somas
resultados = []

# Realiza 3 somas e armazena os resultados na lista
for i in range(3):
    soma = numero1 + numero2
    resultados.append(soma)
    # Para variar os resultados das somas, vamos adicionar um valor incremental
    numero1 += 1
    numero2 += 1

# Exibe os resultados das 3 somas
print("\nResultados das 3 somas:")
for i, resultado in enumerate(resultados, start=1):
    print(f"Soma {i}: {resultado}")

# Calcula o totalizador (soma dos resultados das 3 somas)
totalizador = sum(resultados)
print(f"\nTotalizador das 3 somas: {totalizador}")
