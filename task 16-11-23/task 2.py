from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass


class CreditCard(PaymentMethod):
    def __init__(self, card_number, expiry_date, cvv):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def make_payment(self, amount):
        print(f"Оплата {amount} грн за допомогою кредитної карти {self.card_number}")


class BankTransfer(PaymentMethod):
    def __init__(self, account_number):
        self.account_number = account_number

    def make_payment(self, amount):
        print(f"Банківський переказ {amount} грн на рахунок {self.account_number}")


class EWallet(PaymentMethod):
    def __init__(self, email):
        self.email = email

    def make_payment(self, amount):
        print(f"Електронний гаманець: оплата {amount} грн на {self.email}")


class PaymentProcessor:
    def __init__(self):
        self.payment_methods = []

    def add_payment_method(self, payment_method):
        self.payment_methods.append(payment_method)

    def process_payment(self, amount, payment_method):
        if payment_method in self.payment_methods:
            payment_method.make_payment(amount)
        else:
            print("Обраний платіжний засіб не доступний.")


credit_card = CreditCard("1234-5678-9101-1121", "12/25", "123")
bank_transfer = BankTransfer("123456789")
e_wallet = EWallet("example@email.com")


payment_processor = PaymentProcessor()


payment_processor.add_payment_method(credit_card)
payment_processor.add_payment_method(bank_transfer)
payment_processor.add_payment_method(e_wallet)


payment_processor.process_payment(100, credit_card)
payment_processor.process_payment(200, bank_transfer)
payment_processor.process_payment(50, e_wallet)
