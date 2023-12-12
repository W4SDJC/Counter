import flet as ft
import keyboard 
def main(page: ft.Page):
    page.title = "Counter"
    page.window_width = 465
    page.window_height = 115
    page.window_resizable = False

    num_area = ft.TextField(label="Counter",value="0")
    
    def less(x):
       num_area.value = str(int(num_area.value)-x)      #type: ignore
       page.update()   
    
    def more(x):
        num_area.value = str(int(num_area.value)+x)     #type: ignore
        page.update()  

    minus = ft.ElevatedButton("-",bgcolor="#8D8F8A",color="white", on_click= lambda _:less(1)) 
    keyboard.add_hotkey('-', lambda:less(1))
    keyboard.add_hotkey('ctrl+-', lambda:less(5))
    plus = ft.ElevatedButton("+",bgcolor="#329F74",color="white", on_click= lambda _:more(1))
    keyboard.add_hotkey('+', lambda:more(1))
    keyboard.add_hotkey('ctrl+plus', lambda:more(5))
    
    page.add(
        ft.Row([minus,num_area,plus])
        )



ft.app(target=main)