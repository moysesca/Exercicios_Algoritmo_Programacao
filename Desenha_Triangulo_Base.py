def desenhar_triangulo(base: int):
    """
    Desenha um triângulo retângulo com a base formada pelo número de asteriscos especificado.

    Args:
        base: O número de asteriscos na base do triângulo (deve ser maior que 0).

    Raises:
        ValueError: Se a base for menor ou igual a 0.
    """

    if base <= 0:
        raise ValueError("A base do triângulo deve ser maior que zero.")

    for i in range(1, base + 1):
        print("*" * i)  # Imprime uma linha com i asteriscos


# Exemplos de uso
desenhar_triangulo(8)  # Triângulo com base de 8 asteriscos
print("\n")  # Adiciona uma linha em branco para separar os exemplos
desenhar_triangulo(5)  # Triângulo com base de 5 asteriscos
