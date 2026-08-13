# UML Association Example
#
# Association means that two classes are connected with each other,
# but neither class owns or controls the other.
#
# Here, Teacher and Student have an association because
# a Teacher can teach a Student.


class Teacher:

    def __init__(self, name: str) -> None:
        # Private attribute
        self.__name: str = name

    def get_name(self) -> str:
        # Getter method to access the private name
        return self.__name

    def teach(self, s: "Student") -> None:
        # The teach() method takes a Student object as a parameter.
        # This creates an association between Teacher and Student.
        print(f"{self.__name} is teaching {s.get_name()}")


class Student:

    def __init__(self, name: str) -> None:
        # Private attribute
        self.__name: str = name

    def get_name(self) -> str:
        # Getter method to access the private name
        return self.__name


# Creating a Teacher object
teacher1 = Teacher("MD Sir")

# Creating a Student object
student1 = Student("Aryan")

# Passing the Student object to the Teacher's teach() method.
# This shows the association between Teacher and Student.
teacher1.teach(student1)