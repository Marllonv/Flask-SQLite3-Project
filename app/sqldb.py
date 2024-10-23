import sqlite3

# CONTROLE DO DB
conn = sqlite3.connect('table.db')
cur = conn.cursor()



conn.commit()

conn.close()