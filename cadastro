import flet as ft 

def main(page: ft.Page):
    page.bgcolor = "#4682B4"
    page.window_center()
    page.window_width = '1000'
    page.window_height = '600'
    page.window_resizable = False
    page.window_maximizable = False
    page.horizontal_alignment = 'start'
    page


    r1 = ft.Row([
        ft.Container(
    bgcolor= '#FFFFFF',
    width= 500,
    height= 540,
    border_radius= 5,
    content= ft.Column([ 
        ft.Text("Faça Seu Login",size= 30),
        ft.TextField(label= 'Email', icon= ft.icons.ACCOUNT_BOX, width= 460),
        ft.TextField(label= 'Senha', icon= ft.icons.PASSWORD_SHARP, width= 460),
        ft.CupertinoFilledButton(text= 'Entrar',  width= 173, height= 50, padding= 5),
        ft.TextButton(text="Não possui Cadastro. Realizar Casdastro agora", on_click= True)




     ], alignment= ft.MainAxisAlignment.CENTER, horizontal_alignment= ft.CrossAxisAlignment.CENTER)
  ),
    
    ft.Image( src='lançar.png' )

 ])
    
    page.add(r1)
ft.app(target= main)

 
 
