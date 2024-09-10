--- SELECT * from Veiculo; ---

SELECT Pessoa.nome, Marca.nome
FROM Pessoa
JOIN Veiculo ON Pessoa.cpf = Veiculo.proprietario 
JOIN Marca ON Marca.id = Veiculo.marca 
WHERE Marca.nome = 'Marca B';