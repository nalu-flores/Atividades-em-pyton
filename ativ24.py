# 24. Escreva um programa que simula a chamada de senhas em um sistema de atendimento. O usuário pode escolher "chamar próximo" ou "encerrar atendimento".
import random
senha_atual = 1
while True:
    acao = input("Digite 'próximo' para chamar a próxima senha ou 'finalizar' para encerrar o atendimento: ").strip().lower()
    
    if acao == "próximo":
        print(f"Senha {senha_atual} chamada.")
        senha_atual += 1
    elif acao == "finalizar":
        print("Atendimento encerrado.")
        break
    else:
        print("Ação inválida. Por favor, digite 'chamar próximo' ou 'encerrar atendimento'.")