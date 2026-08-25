class Bank_Account:
    def __init__(self,accountID:str,balance:int):
        self.__accountID:str=accountID
        self.__balance:int=balance

    def get_balance(self):
        return self.__balance
account=Bank_Account("A",100000)
account.get_balance()
    