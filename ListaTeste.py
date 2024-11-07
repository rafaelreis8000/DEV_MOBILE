import flet as ft
import requests

def main(page: ft.Page):

    API="https://api-pim.onrender.com"
    
    dialog = ft.AlertDialog()

    def update_list():
        page.controls[0].controls.clear()  # Limpa a lista

        try:
            response=requests.get(f"{API}/users")
            response_data=response.json()

            print(response_data)
        
        except requests.exceptions.RequestException as e:
            print("erro")
        
        for i in response_data:
            item_container = ft.Container(
                content=ft.Text(f"Usuário {i["nome"]}", size=18, color=ft.colors.BLACK),
                width=200,
                height=50,
                bgcolor="#d9d9d9",
                border_radius=5,
                border=ft.border.all(2, ft.colors.BLACK),
                padding=10,
                alignment=ft.alignment.center,
                on_click=lambda e, index=i: show_dialog(index)
            )
            page.controls[0].controls.append(item_container)
        page.update()

    # Função para exibir o pop-up com as informações do item clicado
    def show_dialog(index):
        dialog.content = ft.Text(f"ID: {index["usuario_id"]} \nNome: {index["nome"]} \nEmail: {index["email"]} \nSenha: {index["senha"]} \nTipo de usuário: {index["tipo_usuario"]} \nData: {index["data_criacao"]} \n")
        page.dialog = dialog
        dialog.open = True
        page.update()

    page.add(
        ft.Column(scroll="auto"),  # Permite a rolagem na lista
    )

    update_list()

# Executa o app
ft.app(target=main)

