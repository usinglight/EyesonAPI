import flet as ft 
import re
import requests

# When running on the local branch for testing
import sys
sys.path.append('/Users/stefansteinbauer/Github/EyesonAPI/eyeson/')

import eyeson


def main(page: ft.Page):
    def guest_add(e):
        if guest_link.value:
            ec = eyeson.EyesonClient.register_guest(guest_link.value)
            print("Room Details")
            print(ec.room_details)
            print("Access Key")
            print(ec.access_key)
        else:
            print("error accessing call")
        view.update()

    guest_link = ft.TextField(hint_text="Paste your guest link here")
    
    view = ft.Column(
        width=1200,
        controls=[
            ft.Row(
                controls=[
                    guest_link,
                    ft.FloatingActionButton(icon=ft.icons.AIRPLANE_TICKET, on_click=guest_add),
                ],
            ),
        ]
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)
    
ft.app(target=main)