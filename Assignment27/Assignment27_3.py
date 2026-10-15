class Number():

    def __init__(self):
        self.Value = int(input("Enter a Num  : "))

    def ChkPrime(self):

        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False

        return True

    def ChkPerfect(self):
        Sum = 0

        if self.Value < 1:
            return False

        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum += i

        if Sum == self.Value:
            return True
        else:
            return False

    def Factors(self):
        FList = []
        for i in range(1,self.Value+1):
            if self.Value % i == 0:
                FList.append(i)

        return FList
    
    def SumFactors(self):
        Sum = 0
        for i in range(1,self.Value+1):
            if self.Value % i == 0:
                Sum += i
        
        return Sum
    
def main():
    Obj1 = Number()
    Obj2 = Number()

    print("-"*10)

    print("operations On Value1")
    ret1 = Obj1.ChkPrime()
    if ret1 == False:
        print("Not prime")
    else:
        print("prime")

    ret2 = Obj1.ChkPerfect()
    if ret2 == False:
        print("Not perfect")
    else:
        print("perfect")

    ret3 = Obj1.Factors()
    print("Factors = ",ret3)

    ret4 = Obj1.SumFactors()
    print("Sum of Factors = ",ret4)

    print("-"*10)

    print("operations On Value2")
    ret1 = Obj2.ChkPrime()
    if ret1 == False:
        print("Not prime")
    else:
        print("prime")

    ret2 = Obj2.ChkPerfect()
    if ret2 == False:
        print("Not perfect")
    else:
        print("perfect")

    ret3 = Obj2.Factors()
    print("Factors = ",ret3)

    ret4 = Obj2.SumFactors()
    print("Sum of Factors = ",ret4)


if __name__ == "__main__":
    main()
