class Animal:

    # Constructor / initializer of the parent class
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    # Method of the parent class
    def eat(self):
        print("I am eating")

    # Method of the parent class
    def sleep(self):
        print("I am sleeping")


class Dog(Animal):

    # Constructor / initializer of the child class
    def __init__(self, name: str, age: int, breed: str):

        # super() is used to access the parent class
        # Here, we are calling the constructor of Animal
        super().__init__(name, age)

        # Attribute specific to the Dog class
        self.breed = breed

    # Method of the child class
    def bark(self):
        print("I am barking")

    # Method of the child class
    def display(self):
        print(
            f"{self.name} is my dog and his age is {self.age} "
            f"and he is of {self.breed} cross-breed."
        )


# Creating an object of the Dog class
dog = Dog("Tommy", 5, "Pitbull")

# Calling the method of the Dog class
dog.bark()

# Calling the method inherited from the Animal class
dog.sleep()

# Calling the method inherited from the Animal class
dog.eat()

# Calling the method of the Dog class
dog.display()