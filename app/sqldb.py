import sqlite3

# Conectar ao banco de dados (substitua 'meu_banco.db' pelo caminho correto)
conn = sqlite3.connect('table.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS personalidade (
        nome TEXT,
        age INTEGER,
        genero_filme TEXT,
        gosta_estudar TEXT,
        linguagens_programa TEXT,
        praia TEXT,
        resultado TEXT
    )
''')

conn.commit()

conn.close()