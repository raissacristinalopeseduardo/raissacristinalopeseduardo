from flet import *
from sqlite3 import Error
from conexao import *

def main(page:Page):

    t= TextField(label= "Nome", autofocus= True)
    b= FilledButton(text="salvar",on_click= lambda e: salvar(e))
    c = FilledButton(text="Conect",on_click= lambda e: create(e))
    g= Text("",size=50)

    def salvar(e):

        if t.value == "Raissa":

            g.value= "CORRETO"
            g.color ="Green"

        else:
            g.value= "ERRADO"
            g.color="Red"

        t.value=""
      
        page.update()

    def create(e):
        nome = t.value

        t.value= ""

        if nome:
            conn, salvar = conectar_banco()
            if conn:
                result = inserir_nome(conn, nome)
                g.value = result
                conn.close()
            else:
                g.value = salvar
        else:
            g.value = "Por favor, insira seu nome!"
        
        page.update

    page.add(t, b, c, g)

app(target = main)
