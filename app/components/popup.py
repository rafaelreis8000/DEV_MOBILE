import flet as ft

from ..services.Api import Api
from .formulario import Formulario

class Popup: 

    def __init__(self, page, checar_estado):
        self.page=page
        self.checar_estado=checar_estado

    def show_popup_infos(self, dados):
        popup_infos=self.popup_infos(dados)
        self.page.dialog = popup_infos
        popup_infos.open = True
        self.page.update()
    
    def popup_infos(self, dados):

        infos=[]
        for chave, valor in dados[0].items():
            infos.append(
                ft.TextField(label=f"{chave}" , value=f"{valor}", width=self.page.width * 0.8, read_only=True)
            )

        def close_dialog(e):
            popup_amplia.open = False
            self.page.update()


        def snack_feedback(e,mensagem):
            self.page.snack_bar=ft.SnackBar(
                ft.Text(
                    mensagem,
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor="#DA4E49"
            )
            self.page.snack_bar.open=True
            self.page.update()


        popup_amplia = ft.AlertDialog(
        title=ft.Text("Dados"),
        content=ft.Column(infos,
        width=self.page.width * 0.95,
        scroll='auto',
        alignment=ft.alignment.center_right,
        ),
        actions=[
            ft.ElevatedButton("Cancelar", style=ft.ButtonStyle(bgcolor=ft.colors.RED, color=ft.colors.WHITE, text_style=ft.TextStyle(size=16)), height=40, on_click=close_dialog),
        ],
    )

        return popup_amplia