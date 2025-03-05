from InquirerPy import prompt

def get_user_action():
    options = [
        {
            "type": "list",
            "message": "Selecione a ação que você deseja que o bot realize:",
            "choices": [
                "Cadastro de produtos sem dados para comanda",
                "Cadastro de Grupo Delivery, Grupo de Itens e Insumos"
            ],
            "name": "action"
        }
    ]
    
    user_response = prompt(options)
    return user_response["action"]
