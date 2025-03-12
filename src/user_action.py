from InquirerPy import prompt

def get_user_action():
    options = [
        {
            "type": "list",
            "message": "Selecione a ação que você deseja que o bot realize:",
            "choices": [
                "Cadastro de bairros",
                "Cadastro de produtos sem dados para comanda",
                "Cadastro de produtos com dados para comanda",
                "Cadastro de produtos com dados para comanda, mas Grupo Delivery, Grupo de Itens e Insumos já estão cadastrados"
            ],
            "name": "action"
        }
    ]
    
    user_response = prompt(options)
    return user_response["action"]
