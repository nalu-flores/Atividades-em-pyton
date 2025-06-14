# 25. Crie um programa que permita ao usuário cadastrar nomes de alunos em uma lista. Depois, exiba todos os alunos cadastrados. Pergunte ao usuário se deseja remover um aluno específico. Exiba a lista atualizada após a remoção.
alunos = []
while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ").strip()
    if nome.lower() == 'sair':
        break
    alunos.append(nome)


print("\nAlunos cadastrados:")
for aluno in alunos:
    print(aluno)    

if alunos:
    remover = input("\nDeseja remover um aluno? (Digite o nome ou 'não' para cancelar): ").strip()
    if remover.lower() != 'não':
        if remover in alunos:
            alunos.remove(remover)
            print(f"{remover} foi removido da lista.")
        else:
            print(f"{remover} não está na lista.")
print("\nLista atualizada de alunos:")
for aluno in alunos:
    print(aluno)
else:
    print("Nenhum aluno cadastrado.")
# Exibir a lista atualizada após a remoção
print("\nLista atualizada de alunos:")
for aluno in alunos:
    print(aluno)
else:
    print("Nenhum aluno cadastrado.")
