import flet as ft

def home(page:ft.Page):

    #botão de dashboard. Leva para a página de mesmo nome
    btn_dash=ft.Container(
        #define os parâmetros visuais do botão como altura, largura, cor e borda
        width=300,
        height=100,
        bgcolor="#2A383E",
        border=ft.border.all(10,"#222D32"),
        border_radius=10,
        padding=20,
        on_click=lambda _:page.go("/dashboard"),
        #adiciona uma imagem e um texto dentro do botão
        content=ft.Row(
            [
                ft.Image("app/assets\Ícone Dashboard.svg"),
                ft.Text("DASHBOARD"),
            ],
            #centraliza imagem e texto
            alignment=ft.MainAxisAlignment.CENTER,
            wrap=True
        ),
        #alinha os elementos de imagem e texto no centro do botão
        alignment=ft.alignment.center
    )

    tela=ft.Container(
        expand=True,
        bgcolor="#1D3331",
        content=ft.ResponsiveRow(
            #delimita a quantidade de colunas que os elementos da tela podem ocupar
            col={"xs": 12, "sm": 6, "md": 4},
            controls=[
                ft.Container(
                    content=ft.Text("DASHBOARD",size=40),
                    alignment=ft.alignment.center
                ),

                ft.Container(
                    content=btn_dash,
                    alignment=ft.alignment.center
                )
            ]
        )
    )

    return tela