#19. Uma pessoa deseja otimizar a sua lista de compras para isso criar um algoritmo que permita a inclusão dos itens faltantes em uma lista

def adicionar_item(lista, item):
    if item not in lista:
        lista.append(item)
        print(f"{item} adicionado à lista.")
    else:
        print(f"{item} já está na lista.")


def exibir_lista(lista):
    if lista:
        print("Lista de compras:")
        for item in lista:
            print(f"- {item}")
    else:
        print("A lista de compras está vazia.")     


def main():
    lista_compras = []
    while True:
        print("\nMenu:")
        print("1. Adicionar item")
        print("2. Exibir lista de compras")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            item = input("Digite o item a ser adicionado: ").strip()
            adicionar_item(lista_compras, item)
        elif escolha == '2':
            exibir_lista(lista_compras)
        elif escolha == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")   
if __name__ == "__main__":
    main()