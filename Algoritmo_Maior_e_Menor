def encontrar_maior_e_menor_nota():

    notas = [] 

    for i in range(4):
        while True:
            try:
                nota = float(input(f"Digite a nota do aluno {i + 1}: "))
                if 0 <= nota <= 100:  
                    notas.append(nota)
                    break 
                else:
                    print("Nota inválida. Digite uma nota entre 0 e 100.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    maior_nota = max(notas)  # Encontra a maior nota
    menor_nota = min(notas)  # Encontra a menor nota

    print(f"\nA maior nota é: {maior_nota}")
    print(f"A menor nota é: {menor_nota}")

if __name__ == "__main__":
    encontrar_maior_e_menor_nota()
