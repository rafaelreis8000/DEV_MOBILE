import flet as ft

def home(page:ft.Page):

    #botão de Dashboard. Leva o usuário para a tela de dashboard
    btn_dashboard=ft.GestureDetector(
        on_tap=lambda _:page.go("/dashboard"),
        content=ft.Stack(
            [
                #define tamanho, largura e cor do botão
                ft.Container(
                    width=300,
                    height=100,
                    bgcolor="#2A383E",
                    border=ft.border.all(10,"#222D32"),
                    border_radius=10,
                    padding=20
                ),

                #organiza a imagem e o texto para que fiquem um em cima do outro
                ft.Column(
                    [
                        ft.Image("app/assets\Ícone Dashboard.svg"),
                        ft.Text("DASHBOARD"),
                    ],
                    #centraliza imagem e texto
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            ],
            #alinha os elementos de imagem e texto no centro do botão
            alignment=ft.alignment.center
        )
    ),

    btn_dash=ft.Container(
        width=300,
        height=100,
        bgcolor="#2A383E",
        border=ft.border.all(10,"#222D32"),
        border_radius=10,
        padding=20,
        on_click=lambda _:page.go("/dashboard"),
        content=ft.Row(
            [
                ft.Image("app/assets\Ícone Dashboard.svg"),
                ft.Text("DASHBOARD"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            #wrap=True
        ),
        alignment=ft.alignment.center
    )

    tela=ft.Container(
        expand=True,
        bgcolor="#1D3331",
        content=ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=ft.Text("DASHBOARD",size=40),
                alignment=ft.alignment.center
            ),
            btn_dash],
        )
    )

    return tela