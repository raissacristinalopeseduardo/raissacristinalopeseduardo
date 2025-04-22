from flet import *

def main(page:Page):
     
    page.window_center()
    page.window.width= 1200
    page.window.height= 650
    page.bgcolor= "#FFFFFF"
    page.window.maximizable = False
    page.window.resizable = False


    t= TextField(label= "Nome", autofocus= True)
    b= FilledButton(text="salvar",on_click= lambda e: salvar(e))
    g= Text("",size=50)

    def salvar(e):

        if t.value == "Raissa":

            g.value= "CORRETO"
            g.color =colors.GREEN_100

        else:
            g.value= "ERRADO"
            g.color=colors.RED_100

        t.value=""
        page.update()


    page.add(t, b, g )

app(target = main)
