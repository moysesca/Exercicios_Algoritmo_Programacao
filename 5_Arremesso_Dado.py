import random

def lancar_dado(num_faces: int) -> int:
    """
    Simula o lançamento de um dado com o número de faces especificado.

    Args:
        num_faces: O número de faces do dado (deve ser maior que 1).

    Returns:
        O resultado do lançamento do dado (um número inteiro entre 1 e num_faces).

    Raises:
        ValueError: Se o número de faces for menor ou igual a 1.
    """

    if num_faces <= 1:
        raise ValueError("O dado deve ter pelo menos duas faces.")

    resultado = random.randint(1, num_faces)
    return resultado

# Exemplos de uso
resultado_dado6 = lancar_dado(6)  # Simula um dado de 6 faces
print(f"Resultado do dado de 6 faces: {resultado_dado6}")

resultado_dado20 = lancar_dado(20)  # Simula um dado de 20 faces
print(f"Resultado do dado de 20 faces: {resultado_dado20}")
