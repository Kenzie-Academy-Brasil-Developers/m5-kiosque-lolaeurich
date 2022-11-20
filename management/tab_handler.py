from menu import products
from management import product_handler


def calculate_tab(dict_list):
    subtotal = 0
    for item in dict_list:
        product = product_handler.get_product_by_id(item["_id"])

        subtotal += item["amount"] * product["price"]

    return {"subtotal":  f'${subtotal.__format__("2.2f")}'}
