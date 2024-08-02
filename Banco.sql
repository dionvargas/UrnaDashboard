DROP SCHEMA IF EXISTS urna;
CREATE SCHEMA urna;

USE urna;

CREATE TABLE Questoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Pergunta VARCHAR(255) NOT NULL,
    AlternativaA VARCHAR(255),
    AlternativaB VARCHAR(255),
    AlternativaC VARCHAR(255),
    AlternativaD VARCHAR(255)
);

CREATE TABLE Votos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_questao INT NOT NULL,
    voto VARCHAR(1) NOT NULL,
    usuario INT NOT NULL,
    dataHora DATETIME NOT NULL,
    FOREIGN KEY (id_questao) REFERENCES Questoes(id)
);

SHOW TABLES;

INSERT INTO Questoes (Pergunta, AlternativaA, AlternativaB, AlternativaC, AlternativaD) VALUES ('O que você vaz?', 'Estudo', 'Trabalho', 'Estudo e trabalho', 'Desempregado');
INSERT INTO Questoes (Pergunta, AlternativaA, AlternativaB, AlternativaC, AlternativaD) VALUES ('Qual é a sua faixa etária?', 'Menos de 18 anos', '18 a 24 anos', '25 a 34 anos', '35 anos ou mais');
INSERT INTO Questoes (Pergunta, AlternativaA, AlternativaB, AlternativaC, AlternativaD) VALUES ('Qual é o seu nível de escolaridade?', 'Ensino Fundamental Incompleto', 'Ensino Médio Completo', 'Ensino Superior Completo', 'Pós-Graduação ou mais');
INSERT INTO Questoes (Pergunta, AlternativaA, AlternativaB, AlternativaC, AlternativaD) VALUES ('Qual é a sua área de interesse principal?', 'Tecnologia e Inovação', 'Design e Artes', 'Indústria e Engenharia', 'Saúde e Segurança');
INSERT INTO Questoes (Pergunta, AlternativaA, AlternativaB, AlternativaC, AlternativaD) VALUES ('Qual seu nível de conhecimento em tecnologia?', 'Básico', 'Intermediário', 'Avançado', 'Super avançado');
INSERT INTO Questoes (Pergunta, AlternativaA, AlternativaB, AlternativaC, AlternativaD) VALUES ('Você tem contato com programação?', 'Trabalho e estudo', 'Só trabalho', 'Só estudo', 'Não tenho contato');
INSERT INTO Questoes (Pergunta, AlternativaA, AlternativaB, AlternativaC, AlternativaD) VALUES ('Qual é o seu objetivo ao visitar o Mundo SENAI?', 'Conhecer as oportunidades de cursos', 'Explorar as inovações tecnológicas', 'Participar de atividades interativas', 'Obter informações sobre parcerias e empresas');
INSERT INTO Questoes (Pergunta, AlternativaA, AlternativaB, AlternativaC, AlternativaD) VALUES ('Como você conheceu o Mundo SENAI?', 'Redes Sociais', 'Indicação de amigos/familiares', 'Publicidade (cartazes, flyers, etc.)', 'Pesquisa na internet');
INSERT INTO Questoes (Pergunta, AlternativaA, AlternativaB, AlternativaC, AlternativaD) VALUES ('Quais recursos ou atividades você mais valoriza em eventos como o Mundo SENAI?', 'Workshops e Palestras', 'Exposições e Demonstrações', 'Oportunidades de networking', 'Sessões interativas e práticas');
INSERT INTO Questoes (Pergunta, AlternativaA, AlternativaB, AlternativaC, AlternativaD) VALUES ('Você valoriza o reconhecimento de instituições em eventos como o Mundo SENAI?', 'Muito importante, fator decisivo.', 'Importante, mas não único.', 'Pouco importante, considerando outros aspectos.', 'Não é importante, o evento em si é relevante.');
SELECT * FROM Questoes;


INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('1', 'A', '1', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('2', 'A', '1', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('3', 'A', '1', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('4', 'A', '1', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('5', 'A', '1', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('6', 'A', '1', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('7', 'A', '1', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('8', 'A', '1', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('9', 'A', '1', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('10', 'A', '1', NOW());

INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('1', 'B', '2', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('2', 'B', '2', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('3', 'B', '2', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('4', 'B', '2', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('5', 'B', '2', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('6', 'B', '2', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('7', 'B', '2', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('8', 'B', '2', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('9', 'B', '2', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('10', 'B', '2', NOW());

INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('1', 'C', '3', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('2', 'C', '3', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('3', 'C', '3', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('4', 'C', '3', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('5', 'C', '3', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('6', 'C', '3', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('7', 'C', '3', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('8', 'C', '3', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('9', 'C', '3', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('10', 'C', '3', NOW());

INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('1', 'D', '4', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('2', 'D', '4', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('3', 'D', '4', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('4', 'D', '4', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('5', 'D', '4', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('6', 'D', '4', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('7', 'D', '4', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('8', 'D', '4', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('9', 'D', '4', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('10', 'D', '4', NOW());


SELECT * FROM Votos;

DELIMITER //

CREATE PROCEDURE recreate_user()
BEGIN
    DECLARE user_exists INT;

    -- Verifica se o usuário já existe
    SELECT COUNT(*) INTO user_exists FROM mysql.user WHERE user = 'eleitor' AND host = '%';

    -- Se o usuário existir, exclua-o
    IF user_exists > 0 THEN
        DROP USER 'eleitor'@'%';
    END IF;

    -- Crie o usuário novamente
    CREATE USER 'eleitor'@'%' IDENTIFIED BY '123456';
	GRANT ALL PRIVILEGES ON *.* TO 'eleitor'@'%' WITH GRANT OPTION;
	FLUSH PRIVILEGES;
END //

DELIMITER ;

CALL recreate_user();

SELECT User, Host FROM mysql.user;
