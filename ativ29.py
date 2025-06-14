# 29. Simule um controle de presença para uma aula: Cadastre os nomes dos alunos presentes em uma lista. Exiba o número total de alunos presentes. Pergunte ao usuário se deseja buscar o nome de um aluno específico para verificar se ele estava presente.

alunos_presentes = []
def exibir_presenca():
    if alunos_presentes:
        print("\nAlunos presentes:")
        for aluno in alunos_presentes:
            print(f"- {aluno}")
    else:
        print("\nNenhum aluno presente.")

while True:
    nome = input("Digite o nome do aluno presente (ou 'sair' para encerrar): ").strip()
    if nome.lower() == 'sair':
        break
    alunos_presentes.append(nome)

print(f"\nTotal de alunos presentes: {len(alunos_presentes)}")
exibir_presenca()
# Pergunte ao usuário se deseja buscar o nome de um aluno específico
buscar = input("\nDeseja verificar a presença de um aluno específico? (s/n): ").strip().lower()
if buscar == 's':
    nome_buscar = input("Digite o nome do aluno a ser verificado: ").strip()
    if nome_buscar in alunos_presentes:
        print(f"{nome_buscar} estava presente na aula.")
    else:
        print(f"{nome_buscar} não estava presente na aula.")
else:
    print("Programa encerrado. Obrigado por usar o controle de presença.")
# Exibir a lista de alunos presentes
print("\nLista final de alunos presentes:")
for aluno in alunos_presentes:
    print(f"- {aluno}")
else:
    print("Nenhum aluno presente.")
    