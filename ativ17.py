# 17. Desenvolva uma função que receba um palavra como entrada e retorne a quantidade de vogais presentes na palavra

from types import prepare_class
def contar_vogais(palavra):
    vogais = "aeiou"
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador
palavra = input("Digite uma palavra: ".lower())
quantidade = contar_vogais(palavra)
print("A quantidade de vogais na palavra é: ", quantidade)