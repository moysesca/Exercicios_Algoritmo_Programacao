def desenhar_losango(tamanho: int):
    """
    Desenha um losango com asteriscos, dado um número inteiro ímpar representando o tamanho da linha central.

    Args:
        tamanho: O tamanho da linha central do losango (deve ser um número ímpar e positivo).

    Raises:
        ValueError: Se o tamanho não for um número ímpar ou for menor ou igual a zero.
    """

    if tamanho <= 0 or tamanho % 2 == 0:
        raise ValueError("O tamanho deve ser um número ímpar e positivo.")

    meio = tamanho // 2
    for i in range(-meio, meio + 1):
        espacos = abs(i)
        asteriscos = tamanho - 2 * espacos
        print(" " * espacos + "*" * asteriscos)


# Exemplo de uso
desenhar_losango(7)
