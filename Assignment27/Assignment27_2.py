class BankAccount():

    ROI = 10.5

    def __init__(self,A,B):
        self.Name = A
        self.Amount = B

    def Display(self):
        print("Account Holder Name : ",self.Name)
        print("Account Balance : ",self.Amount)

    def Deposit(self):
        deposit = int(input("Enter the Amount to Deposit : "))

        self.Amount = self.Amount + deposit

    def Withdraw(self):
        withdraw = int(input("Enter Amount to withdraw : "))

        print("Minium Balance should be more than 500rs")

        if (self.Amount - withdraw) >= 500:
            print("Withdraw Successfull")
            self.Amount = self.Amount - withdraw
        else:
            print("Withdraw unsuccessful!")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest

def main():
    obj1 = BankAccount("Aditya",1000)
    obj2 = BankAccount("Om",5000)

    print("-----Account 1-----")

    obj1.Display()
    obj1.Deposit()
    obj1.Withdraw()

    ret = obj1.CalculateInterest()

    print("Interest is : ",ret)
    print("-----Final Account Details-----")
    obj1.Display()


    print("-----Account 2-----")

    obj2.Display()
    obj2.Deposit()
    obj2.Withdraw()

    ret = obj2.CalculateInterest()

    print("Interest is : ",ret)
    print("-----Final Account Details-----")
    obj2.Display()

if __name__ == "__main__":
    main()



