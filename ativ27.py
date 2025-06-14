# 27. Peça ao usuário para inserir as notas de um aluno em uma lista. Após cadastrar todas as notas, calcule e exiba:
# a média das notas, a maior nota e a menor nota. Pergunte ao usuário se deseja adicionar mais notas ou encerrar o programa.
notas = []  
def calcular_media(notas):
    if notas:
        return sum(notas) / len(notas)
    return 0    

def maior_nota(notas):
    if notas:
        return max(notas)
    return 0
def menor_nota(notas):
    if notas:
        return min(notas)
    return 0
while True:
    try:
        nota = float(input("Digite a nota do aluno (ou -1 para encerrar): "))
        if nota == -1:
            break
        elif 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite uma nota entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
while True:
    try:
        nota = float(input("Digite a nota do aluno (ou -1 para encerrar): "))
        if nota == -1:
            break
        elif 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite uma nota entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
    # Pergunte ao usuário se deseja adicionar mais notas ou encerrar o programa
    continuar = input("Deseja adicionar mais notas? (s/n): ").strip().lower()
    if continuar != 's':
        print("Programa encerrado.")
        break

if notas:
    media = calcular_media(notas)
    maior = maior_nota(notas)
    menor = menor_nota(notas)
    
    print(f"\nMédia das notas: {media:.2f}")
    print(f"Maior nota: {maior:.2f}")
    print(f"Menor nota: {menor:.2f}")           
    print("Notas cadastradas:")
    for nota in notas:
        print(f"- {nota:.2f}")
else:
    print("Nenhuma nota foi cadastrada.")   
