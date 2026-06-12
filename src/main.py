from book import Book
from loan import Loan
from storage import Storage

def clear_screen():
    # Limpa o ecrã.
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def manage_books(storage: Storage):
    while True:
        clear_screen()
        print("=== Gerir Livros ===")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Pesquisar Livro")
        print("4. Editar Livro")
        print("5. Remover Livro")
        print("0. Voltar")
        
        opt = input("\nEscolha: ").strip()
        
        if opt == "1":
            add_book(storage)
        elif opt == "2":
            list_books(storage)
        elif opt == "3":
            search_books(storage)
        elif opt == "4":
            edit_book(storage)
        elif opt == "5":
            remove_book(storage)
        elif opt == "0":
            break
        else:
            print("Opção inválida!")
        input("\nPressione ENTER para continuar...")

def add_book(storage):
    print("\n--- Adicionar Novo Livro ---")
    title = input("Título: ")
    author = input("Autor: ")
    isbn = input("ISBN: ")
    genre = input("Género: ")
    year = input("Ano: ")
    qty = input("Quantidade (stock): ") or "1"
    
    book = Book(title, author, isbn, genre, year, qty) # type: ignore 
    storage.books.append(book)
    storage.save_data()
    print(f"\n Livro '{title}' adicionado com sucesso!")

def list_books(storage):
    print("\n--- Lista de Livros ---")
    if not storage.books:
        print("Nenhum livro registado.")
        return
    for i, book in enumerate(storage.books, 1):
        print(f"{i}. {book}")

def search_books(storage):
    term = input("\nPesquisar por título, autor ou ISBN: ").lower()
    results = [b for b in storage.books if term in b.title.lower() or 
                                           term in b.author.lower() or 
                                           term in b.isbn.lower()]
    if results:
        for book in results:
            print(book)
    else:
        print("Nenhum livro encontrado.")

def edit_book(storage):
    list_books(storage)
    try:
        idx = int(input("\nNúmero do livro a editar: ")) - 1
        if 0 <= idx < len(storage.books):
            book = storage.books[idx]
            print(f"Editando: {book}")
            book.title = input(f"Título [{book.title}]: ") or book.title
            # ... (podes adicionar mais campos se quiseres)
            storage.save_data()
            print("Livro atualizado!")
    except:
        print("Entrada inválida.")

def remove_book(storage):
    list_books(storage)
    try:
        idx = int(input("\nNúmero do livro a remover: ")) - 1
        if 0 <= idx < len(storage.books):
            removed = storage.books.pop(idx)
            storage.save_data()
            print(f"Livro '{removed.title}' removido!")
    except:
        print("Entrada inválida.")

# Funções para Empréstimos 
def manage_loans(storage):
    print("\nFuncionalidade de Empréstimos em desenvolvimento...")
    input("Pressione ENTER...")

def main():
    storage = Storage()
    while True:
        clear_screen()
        print("=== LibraryManager ===")
        print("1. Gerir Livros")
        print("2. Gerir Empréstimos")
        print("3. Relatórios")
        print("0. Sair")
        
        choice = input("\nEscolha uma opção: ").strip()
        
        if choice == "1":
            manage_books(storage)
        elif choice == "2":
            manage_loans(storage)
        elif choice == "3":
            print("\nRelatórios em desenvolvimento...")
            input("Pressione ENTER...")
        elif choice == "0":
            storage.save_data()
            print("Dados guardados.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()


# =================================================================|
# NOTE TO SELF:                                                    |
# =================================================================|
# ISBN = International Standard Book Number                        |
# É um identificador único para livros (geralmente 13 dígitos).    |
# Usamos o ISBN como chave principal para identificar cada livro.  |
# - ISBN-10 (older, 10 digits)                                     |
# - ISBN-13 (current standard)                                     |
# =================================================================|
# Futuro: Poder adicionar validação de ISBN para liverus não identificados. IDK how i will do that but we will see.