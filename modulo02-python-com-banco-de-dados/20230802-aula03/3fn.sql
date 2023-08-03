/*
A terceira forma normal (3FN) exige que cada coluna em uma tabela seja dependente apenas da chave primária da tabela, e
não de outras colunas. Isso ajuda a evitar problemas de redundância e inconsistência de dados em relação a informações
desnecessárias ou irrelevantes, e também ajuda a melhorar a eficiência de consultas ao banco de dados.
*/

USE modulo02_python;

-- tb_pedidos_itens

CREATE TABLE IF NOT EXISTS tb_pedidos_itens(
	pedido_id		INTEGER		NOT NULL,
	item_id			INTEGER		NOT NULL,
	valor_unitario	FLOAT		NOT NULL,
	quantidade		INTEGER		NOT NULL,
	subtotal		FLOAT		NOT NULL,
	PRIMARY KEY(pedido_id, item_id)
);

INSERT INTO tb_pedidos_itens (pedido_id, item_id, valor_unitario, quantidade, subtotal) VALUES
	(1, 1, 10, 2, 10 * 2),
	(1, 2, 3.50, 5, 3.50 * 5),
	(2, 3, 69.90, 2, 69.90 * 2);


SELECT * FROM tb_pedidos_itens ;

SELECT pedido_id, item_id, quantidade, subtotal FROM tb_pedidos_itens;

RENAME TABLE tb_pedidos_itens TO tb_pedidos_itens_pre_3fn;

CREATE TABLE IF NOT EXISTS tb_itens(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(200) NOT NULL,
    valor_unitario FLOAT NOT NULL
);

INSERT INTO tb_itens(nome, valor_unitario) VALUES
	("Garrafa Térmica", 50),
    ("Caixa de som", 99),
    ("Smartwatch", 199.90),
    ("Máquina de cortar cabelo", 50);
    
SELECT * FROM tb_itens;

CREATE TABLE IF NOT EXISTS tb_pedidos_itens(
	pedido_id INT NOT NULL,
    item_id INT NOT NULL,
    quantidade INT NOT NULL,
    
    PRIMARY KEY(pedido_id, item_id),
    FOREIGN KEY(item_id) REFERENCES tb_itens(id)
);

INSERT INTO tb_pedidos_itens(pedido_id, item_id, quantidade) VALUES
	(1, 1, 2),
    (1, 2, 3),
    (1, 4, 2),
    (2, 2, 1),
    (2, 4, 3);
    
CREATE VIEW vw_total_pedidos AS
SELECT
	tpi.pedido_id,
    ti.nome,
    ti.valor_unitario,
    tpi.quantidade,
    FORMAT(ti.valor_unitario * tpi.quantidade, 2) AS Subtotal
FROM tb_itens ti
INNER JOIN tb_pedidos_itens tpi
ON ti.id = tpi.item_id
ORDER BY Subtotal DESC;

SELECT * FROM vw_total_pedidos;