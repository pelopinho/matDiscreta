    # Este programa faz com que o usuário possa estudar um pouco sobre os conceitos de indução matemática e como realizá-la matematicamente



    # A função "mostrar_conceito" é responsável por fazer com que o usuário visualize o conceito de acordo com o número digitado por ele.
    def mostrar_conceito(numero):
    conceitos = {
        1: "A indução matemática é um método de prova matemática que é frequentemente usado para provar afirmações para todos os números naturais.",
        2: "O primeiro passo da indução matemática é provar a afirmação para o caso base, geralmente para n=1.",
        3: "O segundo passo é a hipótese de indução, onde assumimos que a afirmação é verdadeira para um valor arbitrário k.",
        4: "O terceiro passo é provar que, se a afirmação é verdadeira para k, então também é verdadeira para k+1.",
        
    }
    # Se o número digitado estiver entre os números determinados nos conceitos, ele irá imprimir o conceito de acordo com o número digitado.
    if numero in conceitos:
        print(f"\nConceito {numero}:\n\n{conceitos[numero]}")
        print(f"---------------------------------------------------------------------------------------------------------------------------------------------------")
    else:
        print("Opção inválida. Tente novamente.")


    # Essa é a função "menu", que mostra as opções que o usuário dispõe no código.
    def menu():
    while True:
        print("\n----- MENU DE INDUÇÃO MATEMÁTICA -----")
        print("\nO que você gostaria de aprender hoje?")
        print("\n1. O que é indução matemática?")
        print("2. Passo base da indução matemática")
        print("3. Hipótese de indução")
        print("4. Passo de indução")
        print("0. Sair")

        escolha = input("Escolha uma opção (0-4): ")

        if escolha == '0':
            print("Saindo do programa. Até mais!")
            break
        elif escolha.isdigit() and 0 < int(escolha) <= 4:
            mostrar_conceito(int(escolha))
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()