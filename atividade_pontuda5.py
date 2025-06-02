import os
os.system('clear || cls')


estoque = [] # Lista para armazenar os itens do estoque

def adicionar_item(nome, quantidade, preco):
    """Adiciona um novo item ao estoque."""
    item = {"nome": nome, "quantidade": quantidade, "preco": preco}
    estoque.append(item)
    print(f"Item '{nome}' adicionado ao estoque.")

def remover_item(nome, quantidade):
    """Remove uma certa quantidade de um item existente no estoque."""
    for item in estoque:
        if item["nome"] == nome:
            if item["quantidade"] >= quantidade:
                item["quantidade"] -= quantidade
                print(f"{quantidade} unidades de '{nome}' removidas do estoque.")
                return
            else:
                print(f"Quantidade insuficiente de '{nome}' no estoque.")
                return
    print(f"Item '{nome}' não encontrado no estoque.")

def listar_estoque():
    """Lista todos os itens presentes no estoque com suas quantidades e preços."""
    if not estoque:
        print("O estoque está vazio.")
        return
    print("\n--- Estoque Atual ---")
    for item in estoque:
        print(f"Nome: {item['nome']}, Quantidade: {item['quantidade']}, Preço: R${item['preco']:.2f}")
    print("---------------------\n")

def consultar_item(nome):
    """Consulta um item específico no estoque pelo nome."""
    for item in estoque:
        if item["nome"] == nome:
            print(f"Informações de '{nome}': Quantidade: {item['quantidade']}, Preço: R${item['preco']:.2f}")
            return
    print(f"Item '{nome}' não encontrado no estoque.")

if __name__ == "__main__":
    while True:
        print("\n--- Sistema de Gestão de Estoque ---")
        print("1. Adicionar Item")
        print("2. Remover Item")
        print("3. Listar Estoque")
        print("4. Consultar Item")
        print("0. Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            nome = input("Digite o nome do item: ")
            try:
                quantidade = int(input("Digite a quantidade: "))
                preco = float(input("Digite o preço: "))
                adicionar_item(nome, quantidade, preco)
            except ValueError:
          
                print("Entrada inválida. Certifique-se de digitar números para quantidade e preço.")
        
        
        elif opcao == '2':
            nome = input("Digite o nome do item a remover: ")
            try:
                quantidade = int(input("Digite a quantidade a remover: "))
                remover_item(nome, quantidade)
            except ValueError:
                print("Entrada inválida. Certifique-se de digitar um número para a quantidade.")
        elif opcao == '3':
            listar_estoque()
        elif opcao == '4':
            nome = input("Digite o nome do item a consultar: ")
            consultar_item(nome)
        elif opcao == '0':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")