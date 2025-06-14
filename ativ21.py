# 21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

numero = int(input("Digite um número inteiro: "))
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True     

if eh_primo(numero):
    print(f"{numero} é um número primo.")   
else:
    print(f"{numero} não é um número primo.")   

