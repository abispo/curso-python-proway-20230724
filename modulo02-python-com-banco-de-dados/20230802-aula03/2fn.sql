/*
A segunda forma normal (2FN) exige que cada tabela possua uma chave primária única e que todas as outras colunas dependam
diretamente dessa chave primária. Isso ajuda a evitar problemas de redundância e inconsistência de dados em relação a registros
duplicados ou incompletos. Além disso, essa forma normal ajuda a melhorar a eficiência de consultas ao banco de dados, já que as
informações estão organizadas de forma mais estruturada.
*/

-- Comando para renomear uma coluna
-- ALTER TABLE table_name RENAME COLUMN current_name TO new_name;

USE modulo02_python;

-- tb_controle

CREATE TABLE IF NOT EXISTS tb_controle(
	id			INTEGER         AUTO_INCREMENT,
	servico_id	INTEGER         NOT NULL,
	servico		VARCHAR(100)	NOT NULL,
	total_horas	INTEGER	        NOT NULL,
	valor_hora	FLOAT	        NOT NULL,
	
	PRIMARY KEY(id, servico_id)
);

/*
Na tabela acima, temos uma chave primária composta, ou seja, uma chave
primária criada a partir de 2 ou mais colunas
*/

INSERT INTO tb_controle (servico_id, servico, total_horas, valor_hora) VALUES
	(1, "Manutenção de PC", 6, 80),
	(1, "Manutenção de PC", 10, 80),
	(2, "Desenvolvimento de Site", 150, 100),
	(3, "Configuração de Servidor", 30, 250),
	(4, "Aulas de Programação", 80, 50);

SELECT * FROM tb_controle ;

RENAME TABLE tb_controle TO tb_controle_pre_2fn;

CREATE TABLE IF NOT EXISTS tb_servicos(
	id	INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(200) NOT NULL,
    valor_hora	FLOAT NOT NULL
);

INSERT INTO tb_servicos(nome, valor_hora) VALUES
	("Manutenção de PC", 80),
    ("Desenvolvimento de Site", 100),
    ("Configuração de Servidor", 150),
    ("Aulas de Programação", 80);

CREATE TABLE IF NOT EXISTS tb_controle(
	id			INTEGER         AUTO_INCREMENT,
	servico_id	INTEGER         NOT NULL,
	total_horas	INTEGER	        NOT NULL,
	
	PRIMARY KEY(id, servico_id),
    FOREIGN KEY (servico_id) REFERENCES tb_servicos(id)
);

INSERT INTO tb_controle(servico_id, total_horas) VALUES
	(1, 6),
    (1, 10),
    (2, 150),
    (3, 30),
    (4, 80);
