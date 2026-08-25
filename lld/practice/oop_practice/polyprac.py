# class Calculator:
#     def add(self,a:int,b:int):
#         return a+b
#     def add(self,a:float,b:float):
#         return a+b
# calc=Calculator()
# print(calc.add(3.6,3.0))

from abc import ABC,abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self,msg:str):
        pass
class EmailNotification(Notification):
    def send(self,msg:str):
        print("sending email",msg)
class smsNotification(Notification):
    def send(self,msg:str):
        print("sending sms",msg)
notif=EmailNotification()
notif.send("order confirmed")