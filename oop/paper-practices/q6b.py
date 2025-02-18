class Account:
    def __init__(self):
        self._AccountNumber = None
        self._Balance = 0.00
    def GetAccountNumber(self):
        return self._AccountNumber
    def GetBalance(self):
        return self._Balance
    def SetAccountNumber(self, number):
        self._AccountNumber = number
    def SetBalance(self, balance):
        self._Balance = balance
