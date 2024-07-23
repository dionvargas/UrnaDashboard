class Voto:
  def __init__(self, questao, voto, usuario, dataHora):
    self.questao = questao
    self.voto = voto
    self.usuario = usuario
    self.dataHora = dataHora

  def vote(self, db_manager):
    # Conecte-se ao banco de dados
    db_manager.connect()

    # Inserindo um voto no banco de dados
    query = "INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES (%s, %s, %s, %s)"
    cursor = db_manager.connection.cursor()
    cursor.execute(query, (self.questao, self.voto, self.usuario, self.dataHora))
    db_manager.connection.commit()

    # Fecha a conexão com o banco de dados
    db_manager.close()

  @classmethod
  def getLastVoteUser(self, db_manager):
    # Conecte-se ao banco de dados
    db_manager.connect()

    # Consulta SQL para buscar todas as questões
    query = "SELECT usuario FROM Votos ORDER BY id DESC LIMIT 1;"
    cursor = db_manager.connection.cursor()
    cursor.execute(query)

    # Obtém o resultado da consulta
    result = cursor.fetchone()

    # Fecha a conexão com o banco de dados
    db_manager.close()

    # Retorna o último ID (ou None se não houver registros)
    return result[0] if result else 0

  @classmethod
  def getQtdVotes(self, db_manager):

    # Conecte-se ao banco de dados
    db_manager.connect()

    # Consulta SQL para buscar a quantidade de votos das questões
    query = "SELECT id_questao, SUM(CASE WHEN voto = 'A' THEN 1 ELSE 0 END) AS VotosA, SUM(CASE WHEN voto = 'B' THEN 1 ELSE 0 END) AS VotosB, SUM(CASE WHEN voto = 'C' THEN 1 ELSE 0 END) AS VotosC, SUM(CASE WHEN voto = 'D' THEN 1 ELSE 0 END) AS VotosD FROM Votos GROUP BY id_questao;"
    cursor = db_manager.connection.cursor()
    cursor.execute(query)

    # Recupere todas as linhas do resultado
    qtdVotes = []
    for row in cursor.fetchall():
        id, qtdA, qtdB, qtdC, qtdD = row
        qtdVotes.append([qtdA, qtdB, qtdC, qtdD])

    # Fecha a conexão com o banco de dados
    db_manager.close()

    # Retorna o último ID (ou None se não houver registros)
    return qtdVotes
