import flet as ft
import requests
import jwt

def login(page: ft.Page):

    #importa a API contendo a lógica de autenticação de usuário
    API="https://api-pim.onrender.com"
    #chave que decodifica os tokens gerados pela API
    KEY="0d8689404a2c83325a0353496caafcdfa01abd76f4511037bad2a66ed3dd6050"

    def autenticar_usuario(e):
        #obtém o email e senha do usuário
        email=email.value
        senha=senha.value 

        #parâmetro de requisição da API
        payload={
            "email":email,
            "senha":senha
        }

        # Fazer a requisição à API
        try:
            response=requests.post(f"{API}/auth/login", json=payload)
            response_data=response.json()

            # Verifica se o status da resposta é 200 e se o token foi recebido
            if response.status_code==200 and"token" in response_data:
                token=response_data["token"]
                
                # Decodificar o token JWT
                try:
                    decoded_data=jwt.decode(token,KEY,algorithms=["HS256"])
                    output_text.value=f"Token decodificado:{decoded_data}"
                except jwt.ExpiredSignatureError:
                    output_text.value="Erro: o token expirou."
                except jwt.InvalidTokenError:
                    output_text.value="Erro: token inválido."

                page.go("/home")
            else:
                output_text.value=f"Erro de autenticação: verifique suas credenciais.{response_data}"
        
        except requests.exceptions.RequestException as ex:
            output_text.value=f"Erro ao conectar com a API: {ex}"

    ###############################################################################
    ###############################################################################

    #logo do projeto
    logo=ft.Container(
        alignment=ft.alignment.top_center,
        content=ft.Image(src="app/assets\logo.png")
    )

    #informações que o usuário escreve no teclado
    email=ft.TextField(label="Insira seu E-mail: ")
    senha=ft.TextField(label="Insira sua Senha: ",password=True)

    #ao clicar no botão, ele tenta a autenticação na API
    btn_login=ft.Container(
        alignment=ft.alignment.center_right,
        padding=ft.Padding(left=20,right=20,bottom=20,top=0),
        content=ft.TextButton("LOGIN",on_click=autenticar_usuario),
    )

    #retorna informações de login
    output_text=ft.Text()

    ###############################################################################
    ###############################################################################

    tela=ft.Container(
        expand=True,
        bgcolor="#1D3331",
        content=ft.ResponsiveRow(
            col={"xs":12,"sm":6,"md":4},
            controls=[
                logo,
                email,
                senha,
                btn_login,
                output_text
            ]
        ) 
    )

    #manda exibir tudo que estiver no container
    return tela