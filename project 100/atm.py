class Atm:
    def __init__(self, atm_card_no, pin_no):
        self.atm_card_no = atm_card_no
        self.pin_no = pin_no
    def cashWithdraw(self, atm_card_no, pin_no):
        print("cash has been successfully withdrawn")
    def displayPinNumber(self, pin_no):
        print(self.pin_no, "is your pin number")
    def displayATMcardNumber(self, atm_card_no):
        print(self.atm_card_no)
    def sum(self, atm_card_no, pin_no):
        print(self.atm_card_no + self.pin_no)
Mohina = Atm(2223456, 9011090)
Himanshi = Atm(4945622, 9435654)



