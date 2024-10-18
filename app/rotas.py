import flet as ft

from app.login import login

#função que realiza o caminho das telas do sistema
def registro_rotas(page: ft.Page):
    def mudar_rota(route):
        #limpa a tela para começar a checar as rotas
        page.views.clear()

        #leva para a tela de login
        if page.route == "/":
            page.views.append(ft.View(route="/", controls=[login(page)]))

        page.update()

    page.on_route_change = mudar_rota