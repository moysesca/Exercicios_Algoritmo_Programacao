def calcular_media():
    """
    Calcula a média aritmética ou ponderada de duas notas, dependendo da escolha do usuário.
    """

    while True:
        try:
            nota1 = float(input("Digite a primeira nota (entre 0 e 10): "))
            nota2 = float(input("Digite a segunda nota (entre 0 e 10): "))
            if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
                break  # Sai do loop se as notas forem válidas
            else:
                print("Notas inválidas. Digite notas entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite números.")

    while True:
        tipo_media = input("Digite 'a' para média aritmética ou 'p' para média ponderada: ").lower()
        if tipo_media in ('a', 'p'):
            break
        else:
            print("Opção inválida. Digite 'a' ou 'p'.")

    if tipo_media == 'a':
        media = (nota1 + nota2) / 2
        print(f"A média aritmética é: {media:.2f}")  # Formata para 2 casas decimais
    else:  # tipo_media == 'p'
        media = (nota1 * 3 + nota2 * 7) / 10
        print(f"A média ponderada é: {media:.2f}")  # Formata para 2 casas decimais


# Executa a função
if __name__ == "__main__":
    calcular_media()
