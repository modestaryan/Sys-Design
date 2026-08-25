class Vechile:
    def __init__(self,brand:str,speed:int):
        self._brand:str=brand
        self._speed:int=speed
    def accelerate(self,amount:int):
        self._speed+=amount
class Car(Vechile):
    def __init__(self,brand:str,speed:int,number_of_doors):
        super().__init__(brand,speed)
        self.__number_of_doors=number_of_doors
car=Car("Toyota",100,4)
car.accelerate(20)
print(car._speed)