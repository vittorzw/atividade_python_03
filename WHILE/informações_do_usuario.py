def obter_nome():
    while True:
        nome = input("Digite o nome (maior que 3 caracteres): ")
        if len(nome) > 3:
            return nome
        print("Nome inválido. Deve ter mais de 3 caracteres.")

def obter_idade():
    while True:
        try:
            idade = int(input("Digite a idade (entre 0 e 100): "))
            if 0 <= idade <= 100:
                return idade
            print("Idade inválida. Deve estar entre 0 e 100.")
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

def obter_salario():
    while True:
        try:
            salario = float(input("Digite o salário (maior que zero): "))
            if salario > 0:
                return salario
            print("Salário inválido. Deve ser maior que zero.")
        except ValueError:
            print("Valor inválido. Digite um número válido.")

def obter_sexo():
    while True:
        sexo = input("Digite o sexo ('f' para feminino ou 'm' para masculino): ").strip().lower()
        if sexo in ['f', 'm']:
            return sexo
        print("Sexo inválido. Digite 'f' ou 'm'.")

def obter_estado_civil():
    while True:
        estado_civil = input("Digite o estado civil ('s' para solteiro, 'c' para casado, 'v' para viúvo, 'd' para divorciado): ").strip().lower()
        if estado_civil in ['s', 'c', 'v', 'd']:
            return estado_civil
        print("Estado civil inválido. Digite 's', 'c', 'v' ou 'd'.")

def main():
    nome = obter_nome()
    idade = obter_idade()
    salario = obter_salario()
    sexo = obter_sexo()
    estado_civil = obter_estado_civil()

    print("\nDados coletados:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: {salario:.2f}")
    print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
    print(f"Estado Civil: {'Solteiro' if estado_civil == 's' else 'Casado' if estado_civil == 'c' else 'Viúvo' if estado_civil == 'v' else 'Divorciado'}")

if __name__ == "__main__":
    main()