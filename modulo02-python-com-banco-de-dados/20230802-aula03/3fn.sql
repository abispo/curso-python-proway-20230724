/*
A terceira forma normal (3FN) exige que cada coluna em uma tabela seja dependente apenas da chave primária da tabela, e
não de outras colunas. Isso ajuda a evitar problemas de redundância e inconsistência de dados em relação a informações
desnecessárias ou irrelevantes, e também ajuda a melhorar a eficiência de consultas ao banco de dados.
*/

-- tb_pedidos_itens

CREATE TABLE IF NOT EXISTS tb_pedidos_itens(
	pedido_id		INTEGER		NOT NULL,
	item_id			INTEGER		NOT NULL,
	valor_unitario	FLOAT		NOT NULL,
	quantidade		INTEGER		NOT NULL,
	subtotal		REAL		NOT NULL,
	PRIMARY KEY(pedido_id, item_id)
);

INSERT INTO tb_pedidos_itens (pedido_id, item_id, valor_unitario, quantidade, subtotal) VALUES
	(1, 1, 10, 2, 10 * 2),
	(1, 2, 3.50, 5, 3.50 * 5),
	(2, 3, 69.90, 2, 69.90 * 2);


SELECT * FROM tb_pedidos_itens ;