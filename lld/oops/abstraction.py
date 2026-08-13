from abc import ABC, abstractmethod
# To use abstract methods, we need to import ABC and abstractmethod.


class Shape(ABC):

    # @abstractmethod makes a method abstract.
    # An abstract method does not provide an implementation here.
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Concrete class
# A concrete class is a class that provides implementations
# for all the abstract methods of the parent class.
class Rectangle(Shape):

    def __init__(self, length: int, breadth: int):
        self.length = length
        self.breadth = breadth

    # Implementing the abstract area() method
    def area(self):
        print(self.length * self.breadth)

    # Implementing the abstract perimeter() method
    def perimeter(self):
        print(2 * (self.length + self.breadth))


# Till now, if we have not implemented the perimeter() method,
# it will give an error when we try to create the object.
#
# This is because an abstract method forces the child class
# to implement that method.


# Creating an object of Rectangle
r = Rectangle(5, 6)

# Calling the implemented area() method
r.area()

# Calling the implemented perimeter() method
r.perimeter()

# Now it is running without errors because
# Rectangle has implemented both abstract methods:
# area()
# perimeter() 