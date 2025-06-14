# 23. Escreva um programa que pergunte o valor total da conta e permita ao usuário escolher a porcentagem de gorjeta que deseja adicionar (10%, 15%, ou 20%).

valor_conta = float(input("Digite o valor total da conta: R$ "))
porcentagem_gorjeta = input("Escolha a porcentagem de gorjeta (10%, 15%, ou 20%): ")        
if porcentagem_gorjeta == "10%":
    gorjeta = valor_conta * 0.10
elif porcentagem_gorjeta == "15%":
    gorjeta = valor_conta * 0.15
elif porcentagem_gorjeta == "20%":
    gorjeta = valor_conta * 0.20
else:
    print("Porcentagem de gorjeta inválida. Por favor, escolha 10%, 15%, ou 20%.")
    gorjeta = 0
valor_total = valor_conta + gorjeta
print(f"Valor da conta: R$ {valor_conta:.2f}")
print(f"Gorjeta ({porcentagem_gorjeta}): R$ {gorjeta:.2f}")
print(f"Valor total a pagar: R$ {valor_total:.2f}")