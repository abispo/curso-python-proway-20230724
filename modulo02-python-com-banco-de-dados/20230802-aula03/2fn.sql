/*
A segunda forma normal (2FN) exige que cada tabela possua uma chave primária única e que todas as outras colunas dependam
diretamente dessa chave primária. Isso ajuda a evitar problemas de redundância e inconsistência de dados em relação a registros
duplicados ou incompletos. Além disso, essa forma normal ajuda a melhorar a eficiência de consultas ao banco de dados, já que as
informações estão organizadas de forma mais estruturada.
*/

-- Comando para renomear uma coluna
-- ALTER TABLE table_name RENAME COLUMN current_name TO new_name;


-- tb_controle

CREATE TABLE IF NOT EXISTS tb_controle(
	id			INTEGER         PRIMARY KEY AUTO_INCREMENT,
	servico_id	INTEGER         NOT NULL,
	servico		VARCHAR(100)	NOT NULL,
	total_horas	INTEGER	        NOT NULL,
	valor_hora	FLOAT	        NOT NULL,
	
	PRIMARY KEY(id, servico_id)
);

INSERT INTO tb_controle (id, servico_id, servico, total_horas, valor_hora) VALUES
	(1, "Manutenção de PC", 6, 80),
	(1, "Manutenção de PC", 10, 80),
	(2, "Desenvolvimento de Site", 150, 100),
	(3, "Configuração de Servidor", 30, 250),
	(4, "Aulas de Programação", 80, 50);

SELECT * FROM tb_controle ;