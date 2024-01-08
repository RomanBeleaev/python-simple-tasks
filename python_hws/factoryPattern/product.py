class _Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product <{self.name:15} {self.price:.2f}>"
    
def createProduct(type, name, price):
    if type == "product":
        return _Product(name, price)
    else:
        raise TypeError("You can only create \"product\" type with this factory")