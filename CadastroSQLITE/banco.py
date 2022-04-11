import sqlite3


dbase = sqlite3.connect('cliente.db')
c = dbase.cursor()
dbase.execute(''' CREATE TABLE IF NOT EXISTS clientes(
                  CPF INT PRIMARY KEY NOT NULL,
                  NOME TEXT NOT NULL,
                  TELEFONE INT NOT NULL)''')


dbase.commit()

def gravar_dados(CPF,NOME,TELEFONE):
    c.execute(''' INSERT into clientes(CPF,NOME,TELEFONE) VALUES(?,?,?)''', (CPF,NOME,TELEFONE))
    dbase.commit()


def lendo_dados():
    c = dbase.cursor()
    c.execute(''' SELECT CPF from clientes''')
    data = c.fetchall()
    dbase.commit()
    return data

def selecionar_tudo():
    c = dbase.cursor()
    c.execute('''SELECT * from clientes''')
    data = c.fetchall()  # busca tudo
    dbase.commit()
    return data


def delete(CPF):
    c.execute(''' DELETE from clientes WHERE CPF=?''',CPF )
    dbase.commit()