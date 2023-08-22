import flet as ft 
import eyeson

import re
import requests

BASE_URL = 'https://api.eyeson.team'
def main(page: ft.Page):
    def get_access(s):
        match = re.search(r'guest=(.*)', s)
        if match:
            guest_token = match.group(1)
            url = "https://api.eyeson.team/guests/" + guest_token
            headers = {
                "Content-Type": "application/json"
            }
            data = {
                "id": "Assistant", 
                "name": "Assistant"
            }

            response = requests.post(url, headers=headers, json=data)
            # If the response status code is 201 OK (user created), print the response JSON and save response
            if response.status_code == 201:
                return response.json()['access_key']
            else:
                return None

    def guest_add(e):
        access_key = get_access(guest_link.value)
        if access_key:
            view.controls.append(ft.TextField(value=access_key))
            # how would I call the client ?
            ec = eyeson.__init__(access_key, base_url=BASE_URL)
            ec.broadcast_message('Hello World')
        else:
            print("Error getting access key") 
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