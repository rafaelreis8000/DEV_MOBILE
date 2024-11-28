import flet as ft

from app.home import home
from app.gestao_agricola import g_agricola
from app.gestao_insumos import g_insumos
from app.relatorios import TelaRelatorios
from app.login import TelaLogin
from app.cultura import TelaCultura
from app.plantio import TelaPlantio
from app.colheita import TelaColheita
from app.insumos import TelaInsumo
from app.fornecedores import TelaFornecedor
from app.pedidos import TelaPedidos



class ChecarEstado: # essa classe checa o estado do sistema para utilização do token de navegação
    def __init__(self):
        self.token=None
        self.dados_api=None
        self.role=None

#função que realiza o caminho das telas do sistema
def registro_rotas(page:ft.Page):
    checar_estado=ChecarEstado()

    def mudar_rota(route):
        #limpa a tela para começar a checar as rotas
        page.views.clear()

        #leva para a tela de login
        if page.route=="/":
            obj_login=TelaLogin(page,checar_estado)
            page.views.append(ft.View(route="/",controls=[obj_login.login()]))
            #page.views.append(ft.View(route="/",controls=[login(page)]))

        elif page.route=="/home":
            page.views.append(ft.View(route="/home",controls=[home(page)]))

        elif page.route=="/g_agricola":
            page.views.append(ft.View(route="/g_agricola",controls=[g_agricola(page)]))

        elif page.route=="/g_insumos":
            page.views.append(ft.View(route="/g_insumos",controls=[g_insumos(page)]))

        elif page.route=="/pedidos":
            obj_pedido=TelaPedidos(page,checar_estado)
            page.views.append(ft.View(route="/pedidos",controls=[obj_pedido.pedido()]))

        elif page.route=="/relatorios":
            obj_relatorio=TelaRelatorios(page,checar_estado)
            page.views.append(ft.View(route="/relatorios",controls=[obj_relatorio.relatorios()]))

        elif page.route=="/colheita":
            obj_colheita=TelaColheita(page,checar_estado)
            page.views.append(ft.View(route="/colheita",controls=[obj_colheita.colheita()]))

        elif page.route=="/plantio":
            obj_plantio=TelaPlantio(page,checar_estado)
            page.views.append(ft.View(route="/plantio",controls=[obj_plantio.plantio()]))

        elif page.route=="/cultura":
            obj_cultura=TelaCultura(page,checar_estado)
            page.views.append(ft.View(route="/cultura",controls=[obj_cultura.cultura()]))

        elif page.route=="/fornecedores":
            obj_fornecedor=TelaFornecedor(page,checar_estado)
            page.views.append(ft.View(route="/fornecedores",controls=[obj_fornecedor.fornecedor()]))

        elif page.route=="/insumos":
            obj_insumo=TelaInsumo(page,checar_estado)
            page.views.append(ft.View(route="/insumos",controls=[obj_insumo.insumo()]))

        page.update()

    page.on_route_change=mudar_rota