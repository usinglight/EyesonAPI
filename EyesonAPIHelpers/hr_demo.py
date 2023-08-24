import flet as ft 

"""HR DEMO app
tobedone:
- fill dropdowns with user list
- assign spots
- create image overlays
"""

# When running on the local branch for testing
import sys
sys.path.append('/Users/stefansteinbauer/Github/EyesonAPI/eyeson/')

import eyeson

def main(page: ft.Page):
    def guest_add(e):
        if guest_link.value:
            ec = eyeson.EyesonClient()
            ec.register_guest(guest_link.value)
            ec.join_call()
            
            print(ec.room_details)
        else:
            print("error accessing call")
        view.update()
        

    
    
    guest_link = ft.TextField(label="Guest Link",hint_text="Paste your guest link here", width=550)
    
    name_hr = ft.TextField(label="Name of HR Rep",hint_text="Firstname Lastname", width=300)
    role_hr = ft.TextField(label="Role of HR Rep",value="HR Executive",hint_text="HR Exec", width=300)
    name_applicant = ft.TextField(label="Name of Applicant",hint_text="Firstname Lastname", width=300)
    role_candidate = ft.TextField(label="Role of Candidate",value ="Candidate",hint_text="Candidate", width=300)
    
    drop_hr = ft.Dropdown(
        width=300,
        label="HR Representative Video",
        options=[
            ft.dropdown.Option("auto"),
            ft.dropdown.Option("Green"),
        ],
        value="Auto",
    )
    
    drop_cand = ft.Dropdown(
        width=300,
        label="Candidate Video",
        options=[
            ft.dropdown.Option("auto"),
            ft.dropdown.Option("Green"),
        ],
        value="Auto",
    )
    
    view = ft.Column(
        width=1000,
        controls=[
            ft.Row(
                width=750,
                controls=[
                    name_hr,
                    role_hr,
                ],
            ),
            ft.Row(
                width=750,
                controls=[
                    name_applicant,
                    role_candidate,
                ],
            ),
            ft.Row(
                width=750,
                controls=[
                    drop_hr,
                    drop_cand,
                ],
            ),
            ft.Row(
                width=750,
                controls=[
                    guest_link,
                    ft.FloatingActionButton(icon=ft.icons.AIRPLANE_TICKET_ROUNDED, on_click=guest_add),
                ],
            ),
        ]
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Eyeson HR Solution"
    page.theme = ft.Theme(color_scheme_seed="teal")
    page.add(view)
    
ft.app(target=main)