from management import product_handler
from management import tab_handler
from tests.data import original_products

products_to_add = {
    "description": "lau",
    "price": 2.50,
    "rating": 1,
    "title": "blimblom",
    "type": "CLEYTIN",
}

if __name__ == "__main__":



    # product_handler.get_product_by_id(12.5)
    # product_handler.get_products_by_type("bakery")
    product_handler.get_products_by_type(4)
    # product_handler.menu_report()
    # product_handler.add_product(original_products,
    #                             description="lau",
    #                             price=2.50,
    #                             rating=1,
    #                             title="blimblom",
    #                             type="CLEYTIN",
    # )


    #TAB METHODS
    # tab_handler.calculate_tab(dict_list=[{"amount": 2.50}, {"amount": 4.50}, {"amount": 3.50}])
