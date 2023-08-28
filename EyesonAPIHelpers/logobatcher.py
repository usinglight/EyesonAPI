"""App to show company logo on the screen as an overlay
tobedone
- retrieve layout and position
- calculate corner and position image
- scale accodring to layout and slider

"""

import flet as ft 
import sys
sys.path.append('/Users/stefansteinbauer/Github/EyesonAPI/eyeson/')

import eyeson

def main(page: ft.Page):
    def guest_add(e):
        if guest_link.value:
            ec = eyeson.EyesonClient()
            ec.register_guest(guest_link.value)
            print(type(ec.get_users))
        else:
            print("error accessing call")
        view.update()
    guest_link = ft.TextField(label="Guest Link",hint_text="Paste your guest link here", width=550)
    logo_slider = ft.Slider(min=0, max=100, divisions=10, label="{value}%",value=20)
    view = ft.Column(
        controls=[
            ft.Row(
                width=750,
                controls=[
                    guest_link,
                    ft.FloatingActionButton(icon=ft.icons.AIRPLANE_TICKET_ROUNDED, on_click=guest_add),  
                ], 
            ),
            ft.Row(
                width=750,
                controls=[
                    ft.Text("Logo size"),
                    logo_slider,
                ],      
            ),
        ],
    )
    page.add(view)
ft.app(target=main)