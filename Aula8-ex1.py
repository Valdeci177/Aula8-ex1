def adicionar_produto(lista_produtos):
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    valor_unitario = float(input("Digite o valor unitário do produto: "))
    total_produto = quantidade * valor_unitario
    produto = {"produto": nome, "quantidade": quantidade, "valor": valor_unitario, "total": total_produto}
    lista_produtos.append(produto)
    print("Produto adicionado com sucesso!")


def ver_lista(lista_produtos):
    if not lista_produtos:
        print("Lista de produtos vazia.")
        return

    print("Lista de Produtos:")
    for produto in lista_produtos:
        print("Produto:", produto["produto"])
        print("Quantidade:", produto["quantidade"])
        print("Valor Unitário:", produto["valor"])
        print("Total:", produto["total"])
        print("------------------------")
    total_geral = sum(produto["total"] for produto in lista_produtos)
    print("Valor Total de Todos os Produtos:", total_geral)


def atualizar_produto(lista_produtos):
    nome = input("Digite o nome do produto que deseja atualizar: ")
    for produto in lista_produtos:
        if produto["produto"] == nome:
            quantidade = int(input("Digite a nova quantidade do produto: "))
            valor_unitario = float(input("Digite o novo valor unitário do produto: "))
            produto["quantidade"] = quantidade
            produto["valor"] = valor_unitario
            produto["total"] = quantidade * valor_unitario
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado na lista.")


def remover_produto(lista_produtos):
    nome = input("Digite o nome do produto que deseja remover: ")
    for produto in lista_produtos:
        if produto["produto"] == nome:
            lista_produtos.remove(produto)
            print("Produto removido com sucesso!")
            return
    print("Produto não encontrado na lista.")


def main():
    lista_produtos = []
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar Produto")
        print("2. Ver Lista de Produtos")
        print("3. Atualizar Produto")
        print("4. Remover Produto")
        print("5. Encerrar Programa")
        opcao = input("Opção: ")

        if opcao == "1":
            adicionar_produto(lista_produtos)
        elif opcao == "2":
            ver_lista(lista_produtos)
        elif opcao == "3":
            atualizar_produto(lista_produtos)
        elif opcao == "4":
            remover_produto(lista_produtos)
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()