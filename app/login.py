import flet as ft

def login(page: ft.Page):

    logo=ft.Container(
        alignment=ft.alignment.top_center,
        content=ft.Image(src="app/assets\logo.png")
    )

    inputs=ft.Container(

    )

    tela=ft.Container(
        expand=True,
        bgcolor="#1D3331",
        alignment=ft.alignment.top_center,
        content=ft.Column(
            controls=[
                logo,
                ft.Text("TEST")
            ]
        ) 
    )

    #manda exibir tudo que estiver no container
    return tela