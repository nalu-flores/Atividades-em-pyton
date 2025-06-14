# 16. Crie uma função que calcule o fatorial de um numero dado como entrada

num = int(input("Digite um número: "))
fatorial = 1
for i in range(1, num + 1):
    fatorial *= i
print("O fatorial de ", num, " é: ", fatorial)