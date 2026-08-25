from abc import ABC,abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self,amount,currency):
        pass
class StripeGateway(PaymentGateway):
    def process_payment(self, amount, currency):
        return True
gateway=StripeGateway()
print(gateway.process_payment(100,"USD"))
