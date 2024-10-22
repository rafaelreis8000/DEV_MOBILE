import flet as ft

from app.login import login
from app.home import home
from app.dashboard import dashboard
from app.gestao_agricola import g_agricola

#função que realiza o caminho das telas do sistema
def registro_rotas(page: ft.Page):
    def mudar_rota(route):
        #limpa a tela para começar a checar as rotas
        page.views.clear()

        #leva para a tela de login
        if page.route == "/":
            page.views.append(ft.View(route="/", controls=[login(page)]))

        elif page.route == "/home":
            page.views.append(ft.View(route="/home", controls=[home(page)]))
        
        elif page.route == "/dashboard":
            page.views.append(ft.View(route="/dashboard", controls=[dashboard(page)]))

        elif page.route == "/g_agricola":
            page.views.append(ft.View(route="/g_agricola", controls=[g_agricola(page)]))

        page.update()

    page.on_route_change = mudar_rota