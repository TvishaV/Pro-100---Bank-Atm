class Atm():
    def __init__(self,colour,weight,width,height,bank,atmCardNumber,pinNumber):
        self.colour = colour
        self.weight = weight
        self.width = width
        self.height = height
        self.bank = bank
        self.atmCardNumber = atmCardNumber
        self.pinNumber = pinNumber

    def CashWithdrawl(self,atmCardNumber,pinNumber,orignalBalance,amountWithdrawn,balanceLeft):
        self.atmCardNumber = atmCardNumber
        self.pinNumber = pinNumber   
        self.orignalBalance = input("Enter the amount i your bank acoount")
        self.amountWithdrawn = input("Enter the amount of money you are withdrawing")
        self.balanceLeft = originalBalance - amountWithdrawn
        self.balanceLeft = orignalBalance

    def BalanceEnquiry(self,atmCardNumber,pinNumber,balanceLeft):
        self.atmCardNumber = atmCardNumber
        self.pinNumber = pinNumber
        self.balanceLeft = orignalBalance - amountWithdrawn
        self.balanceLeft = orignalBalance

axisBankCard = Atm(orange,20g,3,2.5,axis,1999478,23903839)

axisBankCard.CashWithdrawl()
axisBankCard.BalanceEnquiry()