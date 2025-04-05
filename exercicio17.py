def boasVindas():
    nomeSobrenome = "Fernando Filho"
    print(f"Boas-vindas ao Sistema de Gerenciamento de Livros! Desenvolvido por {nomeSobrenome}\n")

# Lista para armazenar os livros cadastrados
lista_livro = []
id_global = 0  # ID global para cadastrar livros

# Cadastrar um livro
def cadastrarLivro(id):
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")

    livro = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }

    lista_livro.append(livro)  # Adicionando o livro à lista

# Consultar livros
def consultarLivro():
    while True:
        print("\n1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu")

        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            # Consultar todos os livros
            print("\nLivros cadastrados:")
            for livro in lista_livro:
                print(f"ID: {livro['id']} | Nome: {livro['nome']} | Autor: {livro['autor']} | Editora: {livro['editora']}")
            break

        elif opcao == "2":
            # Consultar livro por ID
            id_consulta = int(input("\nDigite o ID do livro a ser consultado: "))
            encontrado = False
            for livro in lista_livro:
                if livro['id'] == id_consulta:
                    print(f"ID: {livro['id']} | Nome: {livro['nome']} | Autor: {livro['autor']} | Editora: {livro['editora']}")
                    encontrado = True
                    break
            if not encontrado:
                print("ID inválido. Tente novamente.")
            break

        elif opcao == "3":
            # Consultar livros por autor
            autor_consulta = input("\nDigite o nome do autor: ")
            encontrados = False
            for livro in lista_livro:
                if livro['autor'].lower() == autor_consulta.lower():
                    print(f"ID: {livro['id']} | Nome: {livro['nome']} | Autor: {livro['autor']} | Editora: {livro['editora']}")
                    encontrados = True
            if not encontrados:
                print("Nenhum livro encontrado para este autor.")
            break

        elif opcao == "4":
            # Retornar ao menu
            break
        else:
            print("Opção inválida. Tente novamente.")

# Remover um livro
def removerLivro():
    while True:
        id_remover = int(input("\nDigite o ID do livro a ser removido: "))
        encontrado = False
        for livro in lista_livro:
            if livro['id'] == id_remover:
                lista_livro.remove(livro)
                print(f"Livro com ID {id_remover} removido com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("ID inválido. Tente novamente.")
        else:
            break

# Main
def main():
    global id_global

    boasVindas()

    while True:
        # Menu principal
        print("\n1. Cadastrar Livro")
        print("2. Consultar Livro")
        print("3. Remover Livro")
        print("4. Encerrar Programa")

        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            # Cadastrar livro
            id_global += 1  # Incrementa o ID global
            cadastrarLivro(id_global)
        elif opcao == "2":
            # Consultar livro
            consultarLivro()
        elif opcao == "3":
            # Remover livro
            removerLivro()
        elif opcao == "4":
            # Encerrar o programa
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Rodar a função principal
if __name__ == "__main__":
    main()
