class Book:
    # Classe que representa um livro na biblioteca.
    # Contém toda a informação sobre um livro específico.
    
    def __init__(self, title: str, author: str, isbn: str, genre: str, year: str, quantity: int = 1):
        self.title = title.strip()
        self.author = author.strip()
        self.isbn = isbn.strip().upper()      # ISBN em maiúsculas
        self.genre = genre.strip()
        self.year = year.strip()
        self.quantity = max(1, int(quantity))  # garante que nunca seja 0 ou negativo, DO NOT REMOVE YOU IDIOT
    
    def to_dict(self):
        # Converte o objeto Book num dicionário para guardar em JSON.
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "genre": self.genre,
            "year": self.year,
            "quantity": self.quantity
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        # Cria um objeto Book a partir de dados lidos do JSON.
        return cls(
            data.get("title", ""),
            data.get("author", ""),
            data.get("isbn", ""),
            data.get("genre", ""),
            data.get("year", ""),
            data.get("quantity", 1)
        )
    
    def __str__(self):
        # Mostra o livro de forma legível.
        return f"{self.title} - {self.author} (ISBN: {self.isbn}) | Stock: {self.quantity}"