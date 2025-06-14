# 31. Solicite ao usuário que insira 10 números em uma lista.
# • Exiba os números em ordem crescente.
# • Exiba os números em ordem decrescente.
# • Exiba apenas os valores pares.

numeros = []
for i in range(10):
    while True:
        try:
            numero = int(input(f"Digite o {i + 1}º número: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")     

# Exibir os números em ordem crescente
numeros_crescentes = sorted(numeros)
print("\nNúmeros em ordem crescente:")
for numero in numeros_crescentes:
    print(numero, end=' ')  

# Exibir os números em ordem decrescente
numeros_decrescentes = sorted(numeros, reverse=True)    
print("\nNúmeros em ordem decrescente:")
for numero in numeros_decrescentes:
    print(numero, end=' ')  
# Exibir apenas os valores pares
numeros_pares = [numero for numero in numeros if numero % 2 == 0]
print("\nNúmeros pares:")
for numero in numeros_pares:
    print(numero, end=' ')
print("\n")  # Linha em branco para melhor formatação
# Exibir a lista completa de números
print("\nLista completa de números:")
for numero in numeros:
    print(numero, end=' ')
print("\n")  # Linha em branco para melhor formatação
# Exibir a lista completa de números
print("\nLista completa de números:")
for numero in numeros:
    print(numero, end=' ')
print("\n")  # Linha em branco para melhor formatação