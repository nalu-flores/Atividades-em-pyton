# 13. Faça um programa que leia a nota de um aluno e indique se ele foi aprovado, reprovado ou está em recuperação. Exemplo: Nota maior ou igual a 7: Aprovado Nota entre 5 e 6.9: Recuperação Nota abaixo de 5: Reprovado

nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("O aluno foi aprovado")
elif nota >= 5 and nota <= 6.9:
    print("O aluno está de recuperação")
else:
    print("O aluno foi reprovado")