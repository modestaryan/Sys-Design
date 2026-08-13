#encapsulation example

class Bank:
    def __init__(self, name: str ,balance:int)->None:
        self.name:str=name
        # self.balance:int=balance  #now letsmake it private 
        self.__balance:int=balance # we need to add __before the property now it is private no one can update 


    #getter
    def get_balance(self)->None:
        print(f"Current balance : {self.__balance}")

    #setter
    # def set_balance(self,new_amount)->None:
    #     self.__balance=new_amount #I know doesn't make sense here but still learn

    def __is_Serverlive(self)->bool: # we can make fucntion also private 
        return True
    

    def deposit(self, amount:int)-> None :
        if self.__is_Serverlive==True:
            self.__balance+=amount
            print(f"Amount Deposited ,current balance={self.__balance}")
        else:
            print("Server is Down")

    def withdraw(self,amount:int)-> None:
        if amount>self.__balance:
            print("Not enough balance to withdraw ")
        else:
            self.__balance-=amount
            print(f"Amount withdrawn, current balance : {self.__balance}")

acc=Bank("Aryan",10000)
acc.deposit(1000)
#now it will not even access 
acc.balance=12345678 #here we can see anyone can access and update because it is not private so we need to make it private 
acc.get_balance()
acc.withdraw(5000)

# cannot be accessed 
# acc.__is_Serverlive(False)# Encapsulation example

class Bank:

    # Constructor / initializer
    def __init__(self, name: str, balance: int) -> None:
        self.name: str = name

        # self.balance: int = balance

        # Now let's make balance private.
        # We need to add __ before the property name.
        # Now it is private and cannot be directly accessed in the usual way.
        self.__balance: int = balance

    # Getter
    def get_balance(self) -> None:
        print(f"Current balance : {self.__balance}")

    # Setter
    # def set_balance(self, new_amount) -> None:
    #     self.__balance = new_amount
    #
    # I know this doesn't make much sense here,
    # but we are learning how a setter works.

    # We can make a function private as well
    def __is_server_live(self) -> bool:
        return True

    def deposit(self, amount: int) -> None:

        # Calling the private method
        if self.__is_server_live() == True:
            self.__balance += amount
            print(f"Amount Deposited, current balance = {self.__balance}")
        else:
            print("Server is Down")

    def withdraw(self, amount: int) -> None:
        if amount > self.__balance:
            print("Not enough balance to withdraw")
        else:
            self.__balance -= amount
            print(f"Amount withdrawn, current balance : {self.__balance}")


# Creating a Bank object
acc = Bank("Aryan", 10000)

# Depositing money
acc.deposit(1000)

# Now let's see what happens if we try to access balance directly.
# acc.balance = 12345678

# Here, if balance were not private, anyone could access and update it.
# That is why we use __balance to make it private.

# Getting the balance using the getter
acc.get_balance()

# Withdrawing money
acc.withdraw(5000)


# Cannot be directly accessed from outside the class
# acc.__is_server_live(False)