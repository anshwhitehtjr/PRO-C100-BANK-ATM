class atm(object):
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pinpin_number = pin_number

    def cash_withdrawl(self, amout_of_money_withdrawn=0):
        print("He is withdrawing money " +
              str(amout_of_money_withdrawn) + " amout of money")

    def balance_enquiry(self):
        print("enquiring balance\n")


demo_person = atm(input("Please Enter Your Card Number:\n"),
                  input("Please Enter your pin number\n"))
demo_person.cash_withdrawl(
    int(input("Please Enter The Amount Of Money to withdraw:\n")))
demo_person.balance_enquiry()
