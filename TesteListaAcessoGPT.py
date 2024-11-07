import flet as ft

def main(page: ft.Page):
    # Configuração inicial da lista e do pop-up
    items = []
    dialog = ft.AlertDialog()
    
    # Nível de acesso do usuário (1 para adicionar, 2 para adicionar e remover)
    user_level = 2  # Altere para 1 para permitir apenas adicionar itens

    # Coluna para armazenar a lista de itens
    item_column = ft.Column(scroll="auto")  # Permite a rolagem

    # Campo de texto para o nome do item no pop-up
    item_name_input = ft.TextField(label="Nome do Novo Item", width=200)
    
    # Função para alternar cores
    def get_color(index):
        return ft.colors.BLUE_200 if index % 2 == 0 else ft.colors.GREEN_200

    # Função para atualizar a lista dinamicamente
    def update_list():
        item_column.controls.clear()  # Limpa a lista
        for i, item_name in enumerate(items, start=1):
            item_container = ft.Container(
                content=ft.Text(f"{item_name}", size=18, color=ft.colors.BLACK),
                width=200,
                height=50,
                bgcolor=get_color(i),
                border_radius=5,
                border=ft.border.all(2, ft.colors.BLACK),
                padding=10,
                alignment=ft.alignment.center,
                on_click=lambda e, name=item_name: show_dialog(name)
            )
            item_column.controls.append(item_container)
        page.update()

    # Função para exibir o pop-up com as informações do item clicado
    def show_dialog(name):
        dialog.content = ft.Text(f"Você clicou no item: {name}")
        page.dialog = dialog
        dialog.open = True
        page.update()

    # Função para exibir o pop-up de adição de item
    def show_add_item_dialog(e):
        # Configura o diálogo para inserção do nome do item
        dialog.content = ft.Column([
            item_name_input,
            ft.ElevatedButton("Confirmar", on_click=add_item)
        ])
        page.dialog = dialog
        dialog.open = True
        page.update()

    # Função para adicionar um novo item com o nome inserido no pop-up
    def add_item(e):
        item_name = item_name_input.value.strip()
        if item_name:
            items.append(item_name)  # Adiciona o nome do item
            item_name_input.value = ""  # Limpa o campo de texto
            dialog.open = False       # Fecha o pop-up de adição de item
            update_list()
        else:
            # Mostra uma mensagem de erro se o nome estiver vazio
            dialog.content = ft.Text("Por favor, insira um nome válido para o item.")
            dialog.open = True
        page.update()

    # Função para remover o último item
    def remove_item(e):
        if items:
            items.pop()
            update_list()

    # Botões de controle para adicionar ou remover itens, dependendo do nível de acesso
    add_button = ft.TextButton("Adicionar Item", on_click=show_add_item_dialog)
    remove_button = ft.TextButton("Remover Item", on_click=remove_item)

    # Verifica o nível do usuário e exibe os botões apropriados
    if user_level == 1:
        # Usuário com nível 1 pode apenas adicionar itens
        page.add(
            ft.Row([add_button]),
            item_column
        )
    elif user_level == 2:
        # Usuário com nível 2 pode adicionar e remover itens
        page.add(
            ft.Row([add_button, remove_button]),
            item_column
        )

# Executa o app
ft.app(target=main)



