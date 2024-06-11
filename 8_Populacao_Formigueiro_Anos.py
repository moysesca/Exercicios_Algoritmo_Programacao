def anos_para_ultrapassar():
    """
    Calcula o número de anos para que a população de um formigueiro ultrapasse outro.
    """

    populacao_a = 90000
    populacao_b = 200000
    taxa_crescimento_a = 0.03  # 3%
    taxa_crescimento_b = 0.017  # 1.7%
    anos = 0

    while populacao_a < populacao_b:
        populacao_a += populacao_a * taxa_crescimento_a
        populacao_b += populacao_b * taxa_crescimento_b
        anos += 1

    print(f"Serão necessários {anos} anos para a população do formigueiro A ultrapassar ou igualar a do formigueiro B.")


# Executa a função
if __name__ == "__main__":
    anos_para_ultrapassar()
