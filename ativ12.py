usuariocrt = 'floresa.com'
senhacrt = 'campim123'
user = str(input("Insira o usuário: "))
senha = str(input("Insira a senha: "))

if user == usuariocrt and senha == senhacrt:
    print("Acesso autorizado.")
else:
    print("Acesso incorreto, tente outro vez.")

