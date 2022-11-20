#Esse módulo ficará responsável por concentrar suas funções de interação 
#com os produtos do arquivo menu.py que já se encontra na raíz do projeto.
from menu import products
from collections import Counter


def get_product_by_id(product_id):
    if type(product_id) is not int:
        raise TypeError("product id must be an int")

    for product in products:
        if product["_id"] == product_id:
            return product
    return {}


def get_products_by_type(product_type):
    if type(product_type) is not str:
        raise TypeError("product type must be a str")

    results = []

    for product in products:
        if product["type"] == product_type:
            results.append(product)
    return results


def menu_report():
    count = len(products)
    type_counter = Counter()
    types = {}

    total_price = 0

    for product in products:
        total_price += product["price"]
        current_type = {product["type"]: 1}
        type_counter.update(current_type)

    for product in products:
        if product["type"] not in types.keys():
            types[product["type"]] = 1
        else:
            val = types[product["type"]]
            types[product["type"]] = val + 1

    types_list = list(types.items())

    types_list.sort(key=lambda item: item[1], reverse=True)

    most_common_type2 = types_list[0][0]

    most_common_type = tuple(type_counter.most_common()[0])[0]
    #
    return f'Products Count: {count} - Average Price: ${round((total_price / count), 2)} - Most Common Type: {most_common_type}'
    # print(f'Product count: {count} - Average Price: {new_price} - Most Common Type: {most_common_type2}')


def add_product(menu, **products_to_add):
    # print(products_to_add)

    last_id = 0
    if len(menu) != 0:
        for item in menu:
            if item["_id"] > last_id:
                last_id = item["_id"]

    product = {"_id": last_id + 1}
    for key, value in products_to_add.items():
        product[key] = value

    menu.append(product)
    return product







