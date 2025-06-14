# 30. Crie um programa que simule um sorteio:
# • Adicione os nomes dos participantes em uma lista.
# • Utilize a função random.choice() para escolher um ganhador aleatório.
# • Exiba o nome do vencedor.

import random
def exibir_participantes(participantes):
    if participantes:
        print("\nParticipantes do sorteio:")
        for participante in participantes:
            print(f"- {participante}")
    else:
        print("\nNenhum participante cadastrado.")
participantes = []
while True:
    nome = input("Digite o nome do participante (ou 'sair' para encerrar): ").strip()
    if nome.lower() == 'sair':
        break
    participantes.append(nome)
if participantes:
    exibir_participantes(participantes)
    ganhador = random.choice(participantes)
    print(f"\nO ganhador do sorteio é: {ganhador}")
else:
    print("Nenhum participante cadastrado para o sorteio.")
# Exibir a lista de participantes
exibir_participantes(participantes) 
