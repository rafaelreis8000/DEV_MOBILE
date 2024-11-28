import flet as ft

from .components.tabela import Tabela

class TelaCultura:

    def __init__(self,page,checar_estado):
        self.page=page
        self.checar_estado=checar_estado

    def cultura(self):

        tabela=Tabela(self.page, self.checar_estado).tabela(["ID", "Nome"], ["cultura_id", "nome"], "cultures", "culture")

        icone_retornar=ft.Container(
            on_click=lambda _:self.page.go("/g_agricola"),
            content=ft.Image(
                "app/assets\Ícone retornar.svg",
                width=20,
                height=20
            )
        )

        titulo_dashboard=ft.Container(
            alignment=ft.alignment.center,
            expand=True,
            content=ft.Text("CULTURA",size=25)
        )

        appbar=ft.Container(
            expand=True,
            height=50,
            bgcolor="#2A383E",
            padding=10,
            content=ft.Row(
                [
                    icone_retornar,
                    titulo_dashboard
                ],
            )
        )

        ###############################################################################
        ###############################################################################

        tela=ft.Container(
            expand=True,
            bgcolor="#1D3331",
            content=ft.ResponsiveRow(
                col={"xs":12,"sm":6,"md":4},
                controls=[
                    appbar,
                    ft.Column(
                        [
                            tabela
                        ]
                    )
                ]
            )
        )

        return tela