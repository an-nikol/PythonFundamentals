class Catalogue:
    products = []

    def __init__(self, name: str):
        self.name = name

    def add_product(self, product_name: str):
        # adds the product to the products list
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        # returns a list containing only the products that start with the given letter
        list_of_given_letter = [word for word in Catalogue.products if word[0] == first_letter]
        return list_of_given_letter

    def __repr__(self):
        # returns the catalogue info
        returning_string = f"Items in the {self.name} catalogue:\n"
        # The items should be sorted alphabetically in ascending order
        returning_string += "\n".join(sorted(self.products))
        return returning_string


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
