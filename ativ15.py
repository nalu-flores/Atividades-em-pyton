# 15. Crie um programa que receba uma quantidade de numeros definidos pelo usuario e retorne a media dos valores presentes na lista

quant = int(input("Digite a quantidade de números desejada: "))
soma = 0
for i in range(quant):
    num = float(input("Digite um número: "))
    soma += num
media = soma / quant
print("A média dos números é: ", media)
