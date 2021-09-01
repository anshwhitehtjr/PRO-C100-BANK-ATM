class atm(object):
    def __init__(self, card_number, pin_number, available_balance=5000):
        self.card_number = card_number
        self.pin_number = pin_number
        self.available_balance = available_balance

    def cash_withdrawl(self, amout_of_money_withdrawn=0):
        self.available_balance = self.available_balance - amout_of_money_withdrawn
        print(f"withdrawl amount = {amout_of_money_withdrawn} \n")
        print(f"remaining balance - {self.available_balance}")

    def balance_enquiry(self):
        print(f"available balance = {self.available_balance}")


demo_person = atm(input("Please Enter Your Card Number:\n"),
                  input("Please Enter your pin number\n"))
demo_person.cash_withdrawl(
    int(input("Please Enter The Amount Of Money to withdraw:\n")))
demo_person.balance_enquiry()
