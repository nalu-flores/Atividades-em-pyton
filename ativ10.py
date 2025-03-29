idade  = int(input ("Insira sua idade: "))

if idade <= 12 and idade >0:
    print("Sua faixa etária é criança.")
elif idade > 12 and idade < 18:
    print("Sua faixa etária é adolescente")
elif idade >=18 and idade < 60:
    print("Sua faixa etária é adulto.")
elif idade >= 60 and idade < 120:
    print("Sua faixa etária é idoso")
elif idade <= 0:
    print("Idade inválida.")
else:
    print("Você é um vampiro.")