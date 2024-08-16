# Inicializa uma lista para armazenar as notas
notas = []

# Solicita 4 notas ao usuário
for i in range(4):
    while True:
        try:
            # Solicita a nota ao usuário
            nota = float(input(f"Digite a nota {i + 1} (entre 0 e 10): "))
            
            # Verifica se a nota está no intervalo válido
            if 0 <= nota <= 10:
                notas.append(nota)
                break  # Sai do loop se a nota for válida
            else:
                print("Nota inválida. A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# Calcula e exibe a média se todas as notas forem válidas
if len(notas) == 4:
    media = sum(notas) / len(notas)
    print(f"A média final das notas é: {media:.2f}")
else:
    print("Não foi possível calcular a média devido a notas inválidas.")
