def resto_divisao(dividendo: int, divisor: int) -> int:
    """
    Calcula o resto da divisão entre dois números inteiros sem usar o operador de módulo.

    Args:
        dividendo: O número a ser dividido.
        divisor: O número pelo qual dividir.

    Returns:
        O resto da divisão entre dividendo e divisor.

    Raises:
        ZeroDivisionError: Se o divisor for zero.
    """

    if divisor == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")

    while dividendo >= divisor:
        dividendo -= divisor

    return dividendo

# Exemplos de uso
resultado1 = resto_divisao(10, 3)  # Resto de 10 / 3 = 1
print(f"Resto de 10 / 3: {resultado1}")

resultado2 = resto_divisao(17, 5)  # Resto de 17 / 5 = 2
print(f"Resto de 17 / 5: {resultado2}")
