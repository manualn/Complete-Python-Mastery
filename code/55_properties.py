class Product:
    def __init__(self, price):
        self.price = price

    #def get_price(self):
        #return self.__price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative")
        self._price = value
    
    #def set_price(self, value):
        #if value < 0:
            #raise ValueError("Price cannot be negative")
        #self.__price = value

#price = property(get_price, set_price)
product = Product(10)
print(product.price)