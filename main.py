import sqlite3
from modelo import Pessoa, Marca, Veiculo

banco = sqlite3.connect("database.db")
banco.execute("PRAGMA foreign_keys=on")
cursor = banco.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS Pessoa(
               cpf INTEGER PRIMARY KEY,
               nome TEXT NOT NULL,
               nascimento DATE NOT NULL,
               oculos BOOLEAN NOT NULL
                 ); 
''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS Marca(
               id INTEGER PRIMARY KEY,
               nome TEXT NOT NULL,
               sigla CHARACTER(2) NOT NULL
               );
''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS Veiculo(
               placa CHARACTER(7) NOT NULL,
               ano INTEGER NOT NULL,
               cor TEXT NOT NULL,
               proprietario INTEGER NOT NULL,
               marca INTEGER NOT NULL,
               PRIMARY KEY(placa),
               FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
               FOREIGN KEY(marca) REFERENCES Marca(id)
               );
''')

#cursor.execute(''' ALTER TABLE Veiculo ADD motor REAL;''')
#inserção de dados - query dinâmicas
"""comando = '''INSERT INTO Pessoa(cpf,nome, nascimento, oculos)
VALUES(?,?,?,?)'''"""
'''pessoa = Pessoa(12345678989,"Pedro", "2000-01-31", True)
#delimitador "?"

#print(pessoa.usa_oculos)
cursor.execute(comando, (pessoa.cpf, pessoa.nascimento, pessoa.nome, pessoa.usa_oculos))'''

"""pessoas = [Pessoa(12345678998, "Cynthia", "1995-03-10", False)]
cursor.executemany(comando, [(i.cpf, i.nome, i.nascimento,i.usa_oculos) for i in pessoas])"""


#outra forma

#pessoa = Pessoa(98776554312, "Carlos", "2000-01-31", True)
comando = '''INSERT INTO Pessoa(cpf,nome,nascimento,oculos) VALUES(:cpf, :nome, :nascimento, :usa_oculos)'''
"""cursor.execute(comando, {"cpf": pessoa.cpf, "nome": pessoa.nome, "nascimento": pessoa.nascimento, "usa_oculos": pessoa.usa_oculos})"""

"""pessoa = Pessoa(67543289710, "Joao", "2000-01-31", False)
cursor.execute(comando, vars(pessoa))"""

#Adicionando marcas
"""comando1 = '''INSERT INTO Marca(nome, sigla) VALUES(:nome, :sigla)'''
marcaA = Marca("Marca A", "MA")
cursor.execute(comando1, vars(marcaA))
marcaA.id = cursor.lastrowid #Armazena o id da linha do ulitmo comando."""

"""marcaB = Marca("Marca B", "MB")
cursor.execute(comando1, vars(marcaB))
marcaB.id = cursor.lastrowid"""

"""veiculos = [Veiculo("AABB003", "2001", "Prata", 1.0 , 12345678998, 1),
            Veiculo("BABB004", "2002", "Preto", 1.6,67543289710, 2)]

comando2 = '''INSERT INTO Veiculo(placa,ano,cor,motor,proprietario,marca) VALUES(:placa, :ano,:cor,:motor,:proprietario,:marca)'''

dados = [vars(i) for i in veiculos]
cursor.executemany(comando2, dados)"""

comando3 = '''
SELECT Pessoa.nome, Marca.nome
FROM Pessoa
JOIN Veiculo ON Pessoa.cpf = Veiculo.proprietario 
JOIN Marca ON Marca.id = Veiculo.marca 
WHERE Marca.nome = :nome;'''

cursor.execute(comando3, {"nome": "Marca B"})
registros = cursor.fetchall()
print(registros)
banco.commit()

#fechamento das conexões e do cursor.
cursor.close()
banco.close()
