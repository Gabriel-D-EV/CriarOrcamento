import sqlite3 as lite

cx = lite.connect('bd.db')

with cx:
    cur = cx.cursor()
    cur.execute("CREATE TABLE Orcamento (id INTEGER PRIMARY KEY AUTOINCREMENT, Nome TEXT, Projeto TEXT, Horas_Prevista FLOAT, Valor_Hora FLOAT, Prazo DECIMAL)")