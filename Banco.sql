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

INSERT INTO Questoes (Pergunta, AlternativaA, AlternativaB, AlternativaC, AlternativaD) VALUES ('Qual personagem do chaves você mais gosta?', 'Chaves', 'Chiquinha', 'Kiko', 'Seu Madruga');
INSERT INTO Questoes (Pergunta, AlternativaA, AlternativaB, AlternativaC, AlternativaD) VALUES ('Pergunta 2', 'A2', 'B2', 'C2', 'D2');
INSERT INTO Questoes (Pergunta, AlternativaA, AlternativaB, AlternativaC, AlternativaD) VALUES ('Pergunta 3', 'A3', 'B3', 'C3', 'D3');
INSERT INTO Questoes (Pergunta, AlternativaA, AlternativaB, AlternativaC, AlternativaD) VALUES ('Pergunta 4', 'A4', 'B4', 'C4', 'D4');
INSERT INTO Questoes (Pergunta, AlternativaA, AlternativaB, AlternativaC, AlternativaD) VALUES ('Pergunta 5', 'A5', 'B5', 'C5', 'D5');
SELECT * FROM Questoes;


INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('1', 'A', '1', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('2', 'A', '1', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('3', 'A', '1', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('4', 'A', '1', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('5', 'A', '1', NOW());

INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('1', 'B', '2', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('2', 'B', '2', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('3', 'B', '2', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('4', 'B', '2', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('5', 'B', '2', NOW());

INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('1', 'C', '3', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('2', 'C', '3', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('3', 'C', '3', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('4', 'C', '3', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('5', 'C', '3', NOW());

INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('1', 'D', '4', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('2', 'D', '4', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('3', 'D', '4', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('4', 'D', '4', NOW());
INSERT INTO Votos (id_questao, voto, usuario, dataHora) VALUES ('5', 'D', '4', NOW());

SELECT * FROM Votos;

GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
