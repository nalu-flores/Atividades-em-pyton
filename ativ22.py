# 22. Crie um programa que simule o acesso a um sistema onde o usuário tem três tentativas para informar a senha correta.

senha_correta = "batatadoce"
tentativas = 3 
while tentativas > 0:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso permitido.")
        break
    else:
        tentativas -= 1
        print(f"Senha incorreta. Você ainda tem {tentativas} tentativas.")
if tentativas == 0:
    print("Acesso negado. Você excedeu o número de tentativas.")    
