import os.path

class Questao:
  def __init__(self, id, pergunta, alternativaA, alternativaB, alternativaC,alternativaD):
    self.id = id
    self.pergunta = pergunta
    self.alternativaA = alternativaA
    self.alternativaB = alternativaB
    self.alternativaC = alternativaC
    self.alternativaD = alternativaD
    self.resultados = None

  def getAlternatives(self):
    return self.alternativaA, self.alternativaB, self.alternativaC, self.alternativaD

  def getResultados(self, votos):
    self.resultados = []
    alternativas = self.getAlternatives()
    for i in range(len(alternativas)):
      url = "./static/images/" + str(self.id) + "/" + chr(97+i) + ".png"
      if(not os.path.isfile(url)):
        url = "./static/images/semImagem.jpeg"
      resultado = {
        "nome": alternativas[i],
        "votos": votos[self.id - 1][i],
        "percentual": 100*votos[self.id - 1][i]/sum(votos[self.id - 1]),
        "url": url
      }
      self.resultados.append(resultado)



  @classmethod
  def getAll(self, db_manager):
    # Conecte-se ao banco de dados
    db_manager.connect()

    # Consulta SQL para buscar todas as questões
    query = "SELECT id, pergunta, alternativaA, alternativaB, alternativaC, alternativaD FROM Questoes"
    cursor = db_manager.connection.cursor()
    cursor.execute(query)

    # Recupere todas as linhas (questões) do resultado
    questoes = []
    for row in cursor.fetchall():
        id, pergunta, alternativaA, alternativaB, alternativaC, alternativaD = row
        questao = Questao(id, pergunta, alternativaA, alternativaB, alternativaC, alternativaD)
        questoes.append(questao)

    # Fecha a conexão com o banco de dados
    db_manager.close()

    return questoes
