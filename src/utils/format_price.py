import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def format_price(price):
    if isinstance(price, str):
        try:
            price = float(price)
        except ValueError:
            raise ValueError("A string fornecida não é um número válido.")
    
    return locale.currency(price, grouping=True)
