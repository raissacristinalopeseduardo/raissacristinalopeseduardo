import flet as ft
import sqlite3 as db
from sqlite3 import* 




def conectardb():
    try:
        con = db.connect("Bancoteste.db")
        return con, "conectado com sucesso"
    
    except Error as e:
        return None, f"Erro ao conctar: {e}"
    
def concreate(con, nome):
    try:
        cursor = con.cursor()
        query = "INSERT INTO pessoa (nome) VALUES(?)"
        cursor.execute(query,(nome))
        con.commit()
        return "Nome inserido com sucesso!"
    
    except Error as e:
        return f"Acesso negado{e}"


def main(page:ft.Page):
    tx = ft.TextField(label= "Nome")
    b2 = ft.ElevatedButton("Salvar", bgcolor= "#000000", on_click= lambda e: create(e))
    t1 = ft.Text(value= "Banco: Não Conctado", color= "Red")
    b1 = ft.ElevatedButton("Testar", bgcolor= "#000000", on_click= lambda e: status(e))
    imprimir = ft.Text(value="")


    def status(e):
        con, status = conectardb()

        if con:
            t1.value = "Banco: Conectado"
            t1.color = "Green"
            con.close()
        
        else: 
            t1.value = status
            t1.color = "red"

        
        page.update()
    def create(e):
        nome = tx.value

        if nome:
            conn,status = conectardb()
            if conn:
                result = concreate(conn, nome)
                imprimir.value = result
                conn.close() #Fechar a coneção apos inserção
            else:
              imprimir.value = status
        else:
             imprimir.value = "Por favor, insira um nome."

        page.update()
    

    page.add(tx,t1,b1,b2, imprimir)
ft.app(target=main)
