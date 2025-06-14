# 26. Implemente um programa onde o usuário pode: Adicionar itens a uma lista de compras. Exibir todos os itens na lista. Remover um item específico, caso o usuário deseje. Finalizar o programa exibindo a lista final.

lista_compras = []
def exibir_lista():
    if lista_compras:
        print("\nLista de compras:")
        for item in lista_compras:
            print(f"- {item}")
    else:
        print("\nA lista de compras está vazia.")   

while True:
    acao = input("\nEscolha uma ação: [1] Adicionar item, [2] Exibir lista, [3] Remover item, [4] Sair: ").strip()
    
    if acao == '1':
        item = input("Digite o item a ser adicionado: ").strip()
        lista_compras.append(item)
        print(f"{item} foi adicionado à lista.")
    
    elif acao == '2':
        exibir_lista()
    
    elif acao == '3':
        if not lista_compras:
            print("A lista de compras está vazia. Não há itens para remover.")
            continue
        item_remover = input("Digite o item a ser removido: ").strip()
        if item_remover in lista_compras:
            lista_compras.remove(item_remover)
            print(f"{item_remover} foi removido da lista.")
        else:
            print(f"{item_remover} não está na lista.")
    
    elif acao == '4':
        print("\nPrograma encerrado. Lista final de compras:")
        exibir_lista()
        break
    
    else:
        print("Opção inválida. Tente novamente.")
# Exibir a lista final de compras
print("\nLista final de compras:")
for item in lista_compras:
    print(f"- {item}")
else:
    print("Nenhum item na lista de compras.")
