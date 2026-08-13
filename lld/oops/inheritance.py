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

    # Polymorphism example
    def move(self):
        print("I am moving")

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
    # This method has the same name as the method in the parent class
    # but it behaves differently.
    # This is an example of method overriding / polymorphism.
    def move(self):
        print("I am running on 4 legs")



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

# Polymorphism calls

# Creating an object of the Animal class
a1 = Animal("Banno", 5)

# Calling move() from the Animal class
a1.move()

# Calling move() from the Dog class
# Dog has its own version of move(),
# so the Dog version is executed instead of the Animal version.
dog.move()