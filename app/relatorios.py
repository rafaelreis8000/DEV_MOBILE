import flet as ft

from .services.Api import Api

class TelaRelatorios:

    def __init__(self,page,checar_estado):
        self.page=page
        self.checar_estado=checar_estado

    def relatorios(self):

        icone_retornar=ft.Container(
            on_click=lambda _:self.page.go("/home"),
            content=ft.Image(
                "app/assets\Ícone retornar.svg",
                width=20,
                height=20
            )
        )

        titulo_relatorios=ft.Container(
            alignment=ft.alignment.center,
            expand=True,
            content=ft.Text("RELATÓRIOS",size=25)
        )

        appbar=ft.Container(
            expand=True,
            height=50,
            bgcolor="#2A383E",
            padding=10,
            content=ft.Row(
                [
                    icone_retornar,
                    titulo_relatorios
                ],
            )
        )

        consultaAPI=Api(self.checar_estado)
        
        ###############################################################################
        ###############################################################################
        vendaPeriodo=consultaAPI.vendaPeriodo()
        vendaCultura=consultaAPI.vendaCultura()
        vendaReceita=consultaAPI.vendaReceita()
        plantioPeriodo=consultaAPI.plantioPeriodo()
        plantioCulturas=consultaAPI.plantioCulturas()
        plantioStatus=consultaAPI.plantioStatus()
        colheitaPeriodo=consultaAPI.colheitaPeriodo()
        insumoFornecedor=consultaAPI.insumoFornecedor()

        print(vendaReceita)

        relatorio_1=ft.Container(
            width=300,
            border=ft.border.only(
                top=ft.border.BorderSide(2,"black")),
            padding=15,
            content=ft.Column(
                [
                    ft.Text(f"Venda último mês: ", color='#000000'),
                    ft.Text(f"Quantidade: {vendaPeriodo}", color='#000000'),
                    ft.Text(f"Receita Total: {vendaReceita["receita_total"]["receita_total"]}", color='#000000'),
                ]
            )
        )

        relatorio_2=ft.Container(
            width=300,
            border=ft.border.only(
                top=ft.border.BorderSide(2,"black")),
            padding=15,
            content=ft.Column(
                [
                    ft.Text(f"Culturas mais vendidas: ", color='#000000'),
                ]
            )
        )

        for venda in vendaCultura:
            venda_info = ft.Column([
                ft.Text(f"Cultura: {venda['cultura_nome']}", color='#000000'),
                ft.Text(f"Quantidade: {venda['frequencia']}", color='#000000'),
            ])

            relatorio_2.content.controls.append(venda_info)

        relatorio_3=ft.Container(
            width=300,
            border=ft.border.only(
                top=ft.border.BorderSide(2,"black")),
            padding=15,
            content=ft.Column(
                [
                    ft.Text(f"Plantios último mês: ", color='#000000'),
                    ft.Text(f"Quantidade: {plantioPeriodo}", color='#000000'),
                    ft.Text(f"Culturas plantadas: ", color='#000000'),
                ]
            )
        )

        for plantios in plantioCulturas:
            plantio_info = ft.Column([
                ft.Text(f"Cultura: {plantios['cultura_nome']}", color='#000000'),
                ft.Text(f"Quantidade Plantada: {plantios['frequencia']}", color='#000000'),
            ])

            relatorio_3.content.controls.append(plantio_info)

        relatorio_3.content.controls.append(ft.Text("Status dos plantios: ", color='#000000'))

        for status in plantioStatus:
            status_info = ft.Column([
                ft.Text(f"Status: {status['status']}", color='#000000'),
                ft.Text(f"Quantidade: {status['frequencia']}", color='#000000'),
            ])

            relatorio_3.content.controls.append(status_info)

        relatorio_4=ft.Container(
            width=300,
            border=ft.border.only(
                top=ft.border.BorderSide(2,"black")),
            padding=15,
            content=ft.Column(
                [
                    ft.Text(f"Colheitas último mês: ", color='#000000'),
                    ft.Text(f"Quantidade: {colheitaPeriodo}", color='#000000'),
                ]
            )
        )

        relatorio_5=ft.Container(
            width=300,
            border=ft.border.only(
                top=ft.border.BorderSide(2,"black")),
            padding=15,
            content=ft.Column(
                [
                    ft.Text(f"Colheitas último mês: ", color='#000000'),
                    ft.Text(f"Quantidade: {colheitaPeriodo}", color='#000000'),
                ]
            )
        ) 

        for insumo in insumoFornecedor:
            insumo_info = ft.Column([
                ft.Text(f"Fornecedor: {insumo['fornecedor_nome']}", color='#000000'),
                ft.Text(f"Quantidade de insumos: {insumo['frequencia']}", color='#000000'),
            ])

            relatorio_5.content.controls.append(insumo_info)

        relatorios_container=ft.Container(
            width=300,
            bgcolor="#D9D9D9",
            margin=15,
            border=ft.border.all(5,ft.colors.BLACK),
            content=ft.Column(
                [
                    relatorio_1,
                    relatorio_2,
                    relatorio_3,
                    relatorio_4,
                    relatorio_5
                ],
                scroll="auto",
                expand=True,
            )
        )

        ###############################################################################
        ###############################################################################

        tela=ft.Container(
            expand=True,
            bgcolor="#1D3331",
            alignment=ft.alignment.center,
            content=ft.ResponsiveRow(
                col={"xs":12,"sm":6,"md":4},
                controls=[
                    appbar,
                    ft.Container(
                        content=ft.Column(
                            [
                                relatorios_container
                            ]
                        ),
                        alignment=ft.alignment.center
                    ),
                ]
            )
        )
        
        return tela