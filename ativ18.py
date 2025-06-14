#18. Crie uma função que receba uma lista de numeros como entrada e retorne a mesma lista ordenada em ordem crescente
lista = []
for i in range(5):
  print("Digite 5 números:")
  num = int(input(f"Digite o {i+1}º número:"))
  lista.append(num)
print("A lista de números é: ", lista)
lista.sort()
print("A lista de números em ordem crescente é: ", lista)