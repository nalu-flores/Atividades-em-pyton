# 14. Peça ao usuário para inserir três números. Determine e exiba qual é o maior número.

for i in range(3):
    num = float(input(f"Digite o {i+1}º número:"))
    if i == 0:
        maior = num
    elif num > maior:
        maior = num
print("O maior número é: ", maior)