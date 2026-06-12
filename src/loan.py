from datetime import datetime

class Loan:
    # Classe que representa um empréstimo de um livro.
    
    def __init__(self, book_isbn: str, user_name: str):
        self.book_isbn = book_isbn.strip().upper()
        self.user_name = user_name.strip()
        self.loan_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.return_date = None
        self.status = "Ativo"          
    
    def return_book(self):
        # Regista a devolução do livro. 
        self.return_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.status = "Devolvido"
    
    def to_dict(self):
        # Converte o empréstimo para dicionário (para JSON).
        return {
            "book_isbn": self.book_isbn,
            "user_name": self.user_name,
            "loan_date": self.loan_date,
            "return_date": self.return_date,
            "status": self.status
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        # Cria um objeto Loan a partir de dados do JSON.
        loan = cls(data.get("book_isbn", ""), data.get("user_name", ""))
        loan.loan_date = data.get("loan_date", "")
        loan.return_date = data.get("return_date")
        loan.status = data.get("status", "Ativo")
        return loan
    
    def __str__(self):
        # Representação legível do empréstimo.
        status = self.status
        if self.return_date:
            status += f" (Devolvido em {self.return_date})"
        return f"Empréstimo: {self.book_isbn} | Utilizador: {self.user_name} | Data: {self.loan_date} | Estado: {status}"