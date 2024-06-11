def multiplicar_doubles(num1: float, num2: float) -> float:
    """
    Multiplica dois números de ponto flutuante (doubles) e retorna o resultado.

    Args:
        num1: O primeiro número double.
        num2: O segundo número double.

    Returns:
        O resultado da multiplicação dos dois números.
    """

    resultado = num1 * num2
    return resultado

# Exemplo de uso
num1 = 3.14
num2 = 2.71
produto = multiplicar_doubles(num1, num2)
print(f"O produto de {num1} e {num2} é: {produto}")
