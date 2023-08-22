"""_summary_
An app which takes a guest link shows the JSON and opens the call
pip3 install flet
to run the app, type flet run guestlink_gui.py

TOBEDONE
- use eyeson.py to join the call and route to a new window for the call
- create simple controls for simple changes
- create a drag and drop interface depending on the layout and existing elements

"""
import flet as ft
import re
import requests

def get_token(s):
    match = re.search(r'guest=(.*)', s)
    if match:
        return match.group(1)
    return None

def main(page: ft.Page):
    def add_clicked(e):
        result_view.controls.append(ft.Text(value=guest_link.value))
        guest_token = get_token(guest_link.value)
        if guest_token:
            
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
                guest_response =response.json()
                result_view.controls.append(ft.Text(value=guest_response))
            else:
                print("Error joining guest user with call. Status code:", response.status_code)
            
            access_key = guest_response['access_key']
            result_view.controls.append(ft.Text(value=access_key))
        view.update()

    guest_link = ft.TextField(hint_text="Paste your guest link here")
    result_view = ft.Column()
    
    
    
    view=ft.Column(
        width=800,
        controls=[
            ft.Row(
                controls=[
                    guest_link,
                    ft.FloatingActionButton(icon=ft.icons.AIRPLANE_TICKET_OUTLINED, on_click=add_clicked),
                ],
            ),
            result_view,
        ],
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)

ft.app(target=main)