def calculadora():
    """
    Realiza operações matemáticas básicas com dois números reais,
    baseado em um caractere que representa a operação desejada.
    """

    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")
            break  # Sai do loop se as entradas forem válidas
        except ValueError:
            print("Entrada inválida. Digite números para os operandos.")

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
            return  # Encerra a função para evitar erros
        else:
            resultado = num1 / num2
    else:
        print("Operação inválida. Use apenas +, -, *, ou /.")
        return

    print(f"Resultado: {num1} {operacao} {num2} = {resultado}")


# Executa a função
if __name__ == "__main__":
    calculadora()
