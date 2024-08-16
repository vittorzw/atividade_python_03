# Função para exibir o menu
def exibir_menu():
    print("Escolha uma das opções abaixo:")
    print("1 - Eu programo em Python")
    print("2 - Eu programo em PHP")
    print("3 - Eu programo em Java")

# Exibe o menu e solicita uma opção ao usuário
while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada: ")
    
    # Verifica a opção escolhida e exibe a mensagem correspondente
    if opcao == '1':
        print("Eu estou estudando Python!")
        break
    elif opcao == '2':
        print("Eu estou estudando PHP!")
        break
    elif opcao == '3':
        print("Eu estou estudando Java!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
