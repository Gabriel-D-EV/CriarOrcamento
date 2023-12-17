import sqlite3 as lite

cx = lite.connect('dados.db')

with cx:
    cur = cx.cursor()
    cur.execute("CREATE TABLE Orcamento (id INTEGER DEFAULT 1, Nome TEXT, Projeto TEXT, Horas_Prevista FLOAT, Valor_Hora FLOAT, Prazo DECIMAL)")
    