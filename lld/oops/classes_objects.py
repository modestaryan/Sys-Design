class Student:

    # Attributes - these are variables defined under a class
    # name = ""
    # age = 0
    # gender = ""

    # If I define these attributes inside a method,
    # I don't need to define them separately here.

    # Methods - these are functions defined under a class
    def __init__(self, name: str, age: int, gender: str):  # Constructor
        print("This is a constructor/initializer")

        # Attributes
        self.name = name
        self.age = age
        self.gender = gender

        # As I have put the set_info functionality here,
        # I don't need to create a separate function.
        # I can directly pass the values while creating the object.

    def set_info(self, name: str, age: int, gender: str):
        # self.name is an attribute of the object,
        # whereas name is a parameter of this parameterised method.

        # name: str
        # Here, str is an annotation that tells us
        # what type of input is expected.

        # self.name = input("Enter your name : ")
        # self.age = int(input("Enter your age : "))
        # self.gender = input("Enter your gender : ")

        # Now let's access the attributes using the parameters.
        self.name = name
        self.age = age
        self.gender = gender

    def display(self) -> None:
        # Writing self is compulsory when defining an instance method.

        # print("This is a display method")

        # We use -> None when the method does not return anything.

        print(
            f"My name is {self.name}, age is {self.age} and gender is {self.gender}"
        )

        # Here, self helps us access the attributes of the current object.
        print(f"self = {self}")

        # Example output:
        # <__main__.Student object at 0x104ad6900>
        # My name is Aryan, age is 23 and gender is Male
        # self = <__main__.Student object at 0x104ad6900>

        # As we can see, the address is the same.

    def get_age(self) -> int:
        return self.age

    # Here, I am showing how a return method works.


# --------------------------------------------------
# Creating an object and accessing attributes directly
# --------------------------------------------------

# s1 = Student()

# s1.name = "Aryan"
# s1.age = 23
# s1.gender = "Male"

# print(s1)
# print(s1.name)
# print(s1.age)
# print(s1.gender)


# s2 = Student()

# print(s2)

# s1.display()
# s2.display()


# --------------------------------------------------
# Using the set_info() method
# --------------------------------------------------

# s1 = Student()

# s1.set_info()

# s1.set_info("Aryan", 23, "Male")  # Parameter-based
# s1.display()


# s2 = Student()

# s2.set_info()

# s2.set_info("Aditi", 23, "Female")  # Parameter-based
# s2.display()


# --------------------------------------------------
# Using the initializer / constructor
# --------------------------------------------------

s1 = Student("Aryan", 23, "Male")  # See, here I can pass the values directly.

s1.display()

print(s1.get_age())

# When I hover over get_age(), my editor shows the return type as int,
# like this:
# (method) def get_age() -> int