from flask import Flask, render_template
import matplotlib
matplotlib.use('Agg')  # Use o backend 'Agg' para evitar problemas de thread
import matplotlib.pyplot as plt
from DatabaseManager import DatabaseManager
from model.Questao import Questao
from model.Voto import Voto
import numpy as np

app = Flask(__name__)

print("Iniciando o programa...")

# Configurações do banco de dados
db_manager = DatabaseManager(
    host="192.168.1.2",
    #host="localhost",
    user="eleitor",
    password="123456",
    database="urna"
)

def gerar_grafico(questao, voto):
    plt.clf()

    # Define os dados que serão representados no gráfico de pizza
    labels = questao.getAlternatives()
    sizes = voto  # Tamanhos das fatias do gráfico de pizza
    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(labels)))  # Cores das fatias
    explode = (0.1, 0, 0, 0)  # Destaca a primeira fatia (Produto A)

    # Cria o gráfico de pizza
    plt.pie(sizes,
            ##explode=explode,
            labels=labels,
            colors=colors,
            autopct='%1.1f%%',
            shadow=True,
            startangle=140)

    # Define que o gráfico deve ser desenhado de forma circular
    plt.axis('equal')

    urlImage = 'static/images/charts/grafico' + str(questao.id) + '.png'
    plt.savefig(urlImage)



@app.route('/')
def home():
    questoes = Questao.getAll(db_manager)
    votos = Voto.getQtdVotes(db_manager)

    for questao in questoes:
        questao.alternativas = questao.getAlternatives()
        questao.getResultados(votos)

    for i in range(len(questoes)):
        gerar_grafico(questoes[i], votos[i])

    return render_template('index.html', questoes=questoes)

if __name__ == '__main__':
    app.run(debug=True)
