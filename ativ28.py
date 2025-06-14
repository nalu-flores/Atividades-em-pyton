# 28. Crie um programa que gerencie um estoque de produtos:
# • O usuário deve poder adicionar produtos (nome e quantidade).
# • Permita a busca por um produto específico e exiba sua quantidade.
# • Ofereça a opção de atualizar a quantidade de um produto.
# • Exiba o estoque completo ao final.

estoque = {}
def exibir_estoque():
    if estoque:
        print("\nEstoque atual:")
        for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade}")
    else:
        print("\nO estoque está vazio.")    

while True: 
    acao = input("\nEscolha uma ação: [1] Adicionar produto, [2] Buscar produto, [3] Atualizar quantidade, [4] Exibir estoque, [5] Sair: ").strip()
    
    if acao == '1':
        produto = input("Digite o nome do produto: ").strip()
        quantidade = int(input("Digite a quantidade do produto: "))
        estoque[produto] = estoque.get(produto, 0) + quantidade
        print(f"{quantidade} unidades de {produto} foram adicionadas ao estoque.")
    
    elif acao == '2':
        produto = input("Digite o nome do produto a ser buscado: ").strip()
        if produto in estoque:
            print(f"{produto}: {estoque[produto]} unidades")
        else:
            print(f"{produto} não está no estoque.")
    
    elif acao == '3':
        produto = input("Digite o nome do produto a ser atualizado: ").strip()
        if produto in estoque:
            nova_quantidade = int(input(f"Digite a nova quantidade para {produto}: "))
            estoque[produto] = nova_quantidade
            print(f"A quantidade de {produto} foi atualizada para {nova_quantidade}.")
        else:
            print(f"{produto} não está no estoque.")
    
    elif acao == '4':
        exibir_estoque()
    
    elif acao == '5':
        print("\nPrograma encerrado. Estoque final:")
        exibir_estoque()
        break
    
    else:
        print("Opção inválida. Tente novamente.")
# Exibir o estoque final
print("\nEstoque final:")
for produto, quantidade in estoque.items():
    print(f"{produto}: {quantidade}")
else:
    print("Nenhum produto no estoque.")
    