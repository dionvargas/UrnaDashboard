from DatabaseManager import DatabaseManager
from model.Questao import Questao
from view.InterfaceUrna import InterfaceUrna

def main():
    print("Iniciando o programa...")

    # Configurações do banco de dados
    db_manager = DatabaseManager(
        host="localhost",
        user="root",
        password="123456",
        database="urna"
    )

    questoes = Questao.getAll(db_manager)
    InterfaceUrna(questoes, db_manager)

    print("Programa encerrado.")

if __name__ == "__main__":
    main()
