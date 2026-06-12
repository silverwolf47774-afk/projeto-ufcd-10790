import json
import os
from book import Book
from loan import Loan

class Storage:
    # Responsável por guardar e carregar todos os dados da biblioteca.
    
    def __init__(self, filename="library_data.json"):
        self.filename = filename
        self.books = []      # lista de Book
        self.loans = []      # lista de Loan
        self.load_data()
        
    def load_data(self):
        # Carrega os dados do ficheiro JSON.
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.books = [Book.from_dict(b) for b in data.get("books", [])]
                    self.loans = [Loan.from_dict(l) for l in data.get("loans", [])]
            except Exception as e:
                print(f"Erro ao carregar dados: {e}")
    
    def save_data(self):
        # Guarda todos os dados no ficheiro JSON.
        try:
            data = {
                "books": [b.to_dict() for b in self.books],
                "loans": [l.to_dict() for l in self.loans]
            }
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Erro ao guardar dados: {e}")