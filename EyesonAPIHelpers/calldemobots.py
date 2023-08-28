import flet as ft 

"""Call demo bots for Eyeson API

"""

# When running on the local branch for testing
import sys
sys.path.append('/Users/stefansteinbauer/Github/EyesonAPI/eyeson/')
import eyeson
import requests

bottxt = "https://storage.googleapis.com/eyeson-demo/videos/callbots/names.txt"
response =requests.get(bottxt)
names = response.text.splitlines()
print(names)



def main(page: ft.Page):
    layout_select = 'six'
    def guest_add(e):
        if guest_link.value:
            ec = eyeson.EyesonClient()
            ec.register_guest(guest_link.value)
            ec.change_layout(layout_type='auto',layout_name=layout_select ,users=[])
        else:
            print("error accessing call")
        view.update()
    
    guest_link = ft.TextField(label="Guest Link",hint_text="Paste your guest link here", width=550)
    
    def dropdown_changed(e):
        layout_select = dd.value
        view.update()


    dd = ft.Dropdown(
        on_change=dropdown_changed,
        options=[
            ft.dropdown.Option("four"),
            ft.dropdown.Option("six"),
            ft.dropdown.Option("nine"),
        ],
        width=200,
    )
    
    view = ft.Column(
        width=800,
        controls=[
            ft.Row(
                width=800,
                controls=[
                    dd,
                    ft.FloatingActionButton(icon=ft.icons.AIRPLANE_TICKET_ROUNDED, on_click=guest_add),
                ],
            ),
            ft.Row(
                width=800,
                controls=[
                    guest_link,
                    ft.FloatingActionButton(icon=ft.icons.AIRPLANE_TICKET_ROUNDED, on_click=guest_add),
                ],
            ),
        ]
    )
        
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Eyeson Demo Bots"
    page.theme = ft.Theme(color_scheme_seed="teal")
    page.add(view)
    
ft.app(target=main)