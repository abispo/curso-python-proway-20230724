/*
A normalização de dados é um processo importante na
criação de banco de dados. É um processo que ajuda a
evitar problemas comuns que ocorrem quando os dados
são armazenados de maneira desorganizada. A normalização
ajuda a melhorar a eficiência, reduzir a redundância de
dados, melhorar a integridade dos dados e evitar problemas
de inconsistência.

Para alcançar esse objetivo, dentro da normalização
utilizamos passos que chamamos de formas normais. Existem
3 principais formas normais, que são a Primeira Forma
Normal (1FN), Segunda Forma Normal (2FN) e a Terceira
Forma Normal (3FN)

A 1FN define que cada coluna em uma tabela deve conter
apenas valores atômicos e indivisíveis, ou seja, valores
únicos e não compostos. Essa forma normal ajuda a evitar
a repetição de informações em uma mesma coluna (coluna
multivalorada), o que pode levar a problemas de redundância
de dados, inconsistência e performance
*/

USE modulo02_python;

-- Exemplo: Tabela de clientes

CREATE TABLE IF NOT EXISTS tb_clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(200) NOT NULL,
    telefone VARCHAR(100) NOT NULL
);

INSERT INTO tb_clientes(nome, endereco, telefone) VALUES
	(
    "João da Silva",
    "Rua XV de Novembro, 1000, Centro, Blumenau, SC",
    "47957323907"
    );

INSERT INTO tb_clientes(nome, endereco, telefone) VALUES
(
	"Neide Carvalho",
    "Praça da Liberdade, 12, Liberdade, São Paulo, SP",
    "11956283098,11972633312"
);

INSERT INTO tb_clientes(nome, endereco, telefone) VALUES
(
	"Maria Souza",
    "Rua dos Bandeirantes, 240, Centro, Pomerode, SC",
    "47989878531"
);

/*
No caso da tabela tb_clientes, as regras da 1FN estão sendo
violadas, pois a coluna endereço possui um tipo de dado composto,
e a coluna telefone possui alguns registros multivalorados. Vamos
aplicar a 1FN.
*/
SELECT * FROM tb_clientes;

-- Alterar o nome da tabela para tb_clientes_pre_1fn
RENAME TABLE tb_clientes TO tb_clientes_pre_1fn;

/*
Criamos a nova tabela, "quebrando" o endereço em várias colunas,
dessa maneira em cada coluna temos um valor indivisível, ou seja,
não composto, como diz a 1FN
*/
CREATE TABLE IF NOT EXISTS tb_clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(200) NOT NULL,
    tipo_logradouro VARCHAR(20) NOT NULL,
    logradouro VARCHAR(200) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(50) NOT NULL
);

INSERT INTO tb_clientes(
	nome, tipo_logradouro, logradouro, numero, bairro, cidade, estado
) VALUES
	("João da Silva", "Rua", "XV de Novembro", "1000", "Centro", "Blumenau", "SC"),
	("Neide Carvalho", "Praça", "da Liberdade", "12", "Liberdade", "São Paulo", "SP"),
	("Maria Souza", "Rua", "dos Bandeirantes", "240", "Centro", "Pomerode", "SC");
/*
Após isso, criamos uma outra tabela para armazenar os dados
de telefone dos clientes, criando assim um relacionamento
onde vamos poder associar telefones a um cliente
*/

CREATE TABLE IF NOT EXISTS tb_telefones(
	id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    
    FOREIGN KEY (cliente_id) REFERENCES tb_clientes(id)
);

/* Inserindo os dados de telefone dos clientes */

INSERT INTO tb_telefones(cliente_id, telefone) VALUES
	(1, "47957323907"),
    (2, "11956283098"),
    (2, "11972633312"),
    (3, "47989878531");
    
/*
Utilizamos os JOINs para consultar dados de tabelas diferentes
ao mesmo tempo
*/

INSERT INTO tb_clientes(
	nome, tipo_logradouro, logradouro, numero, bairro, cidade, estado
) VALUES
	("Paulo Souza", "Rua", "XV de Novembro", "1000", "Centro", "Blumenau", "SC");

SELECT a.id, a.nome, a.cidade, a.estado, b.telefone FROM tb_clientes a
INNER JOIN tb_telefones b
ON a.id = b.cliente_id;
