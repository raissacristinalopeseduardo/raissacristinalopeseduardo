import flet as ft

def main(page:ft.Page):
   page.window_center()
   page.title='calculadora'
   page.window_width='360'
   page.window_height='450'  

   result=ft.Text( value="0", color=ft.colors.BLACK, size=40),
  

   a = ft.Row([
      ft.ElevatedButton(text="%",  on_click= True ),
      ft.ElevatedButton(text="CE",  on_click= True ),
      ft.ElevatedButton(text="C",  on_click= True ),
      ft.ElevatedButton(on_click= True, content=ft.Icon(ft.icons.BACKSPACE)),

   ])


   b = ft.Row([
      ft.ElevatedButton(text="7",  on_click= True ),
      ft.ElevatedButton(text="8",  on_click= True ),
      ft.ElevatedButton(text="9",  on_click= True ),
      ft.ElevatedButton(text="/", on_click= True)

   ])

   c = ft.Row([
      ft.ElevatedButton(text="4",  on_click= True ),
      ft.ElevatedButton(text="5",  on_click= True ),
      ft.ElevatedButton(text="6",  on_click= True ),
      ft.ElevatedButton(text="*", on_click= True)

   ])

   d = ft.Row([
      ft.ElevatedButton(text="1",  on_click= True ),
      ft.ElevatedButton(text="2",  on_click= True ),
      ft.ElevatedButton(text="3",  on_click= True ),
      ft.ElevatedButton(text="+", on_click= True)

   ])

   e = ft.Row([
      ft.ElevatedButton(text="0",  on_click= True ),
      ft.ElevatedButton(text=",",  on_click= True ),
      ft.ElevatedButton(text="-", on_click= True),
      ft.ElevatedButton(text="=", on_click= True)

   ])


   
   
   page.add(result, a, b, c, d, e) 
ft.app(main)
