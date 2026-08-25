class Order:
    def __init__(self,total:int):
        self.__total=total
    def add_Item(self,price:int)->None:
        if (price<=0):
            raise ValueError("Price must be positive")
        self.__total+=price
    def get_Total(self)->None:
        return self.__total
orders=Order(20)
orders.add_Item(20)
print(orders.get_Total())