import sqlite3 as lite

cx = lite.connect('dados.db')


def inserir_(i):
    with cx:
        cur = cx.cursor()
        query = "INSERT INTO Orcamento(Nome, Projeto, Horas_Prevista, Valor_Hora, Prazo) VALUES(?,?,?,?,?)"
        cur.execute(query,i)
        
        
def del_(i):
    with cx:
        cur = cx.cursor()
        query = "DELETE FROM Inventario WHERE id=?"
        cur.execute(query,i)
