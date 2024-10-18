import flet as ft

def login(page: ft.Page):

    btn_1=ft.Container(
        content=ft.Text("BOTAO 1"),
        width=100,
        height=100,
        bgcolor="#2A383E",
        padding=10
    )

    btn_2=ft.Container(
        content=ft.Text("BOTAO 2"),
        width=100,
        height=100,
        bgcolor="#2A383E",
        padding=10
    )

    btn_3=ft.Container(
        content=ft.Text("BOTAO 3"),
        width=100,
        height=100,
        bgcolor="#2A383E",
        padding=10
    )

    conjunto=ft.Container(
        content=ft.Row(
            controls=[btn_1,btn_2]
        )
    )

    tela=ft.Container(
        content=ft.Column(
            controls=[conjunto, btn_3]
        )
    )

    #manda exibir tudo que estiver no container
    return tela