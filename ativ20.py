#20. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

lista = []
print("Digite 10 números inteiros:")
for i in range (10):
  num = int(input(f"Digite o {i+1}º número:"))
  lista.append(num)

def pares_impares(lista):
  pares = 0
  impares = 0
  for num in lista:
    if num % 2 == 0:
      pares += 156
    else:
      impares += 1
  return pares, impares
  print("A quantidade de números pares é: ", pares)
  print("A quantidade de números impares é: ", impares)
quantidade_pares, quantidade_impares = pares_impares(lista)
print("A quantidade de números pares é: ", quantidade_pares)
print("A quantidade de números impares é: ", quantidade_impares)