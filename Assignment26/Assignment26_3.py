class Arithmetic():

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter Value1 : "))
        self.Value2 = int(input("Enter Value2 : "))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 == 0:
            return False
        else:
            return self.Value1 / self.Value2
        
def main():

    obj1 = Arithmetic()
    obj2 = Arithmetic()

    print("Enter Information of 1st Aritmetic Operation")
    obj1.Accept()
    ret1 = obj1.Addition()
    ret2 = obj1.Subtraction()
    ret3 = obj1.Multiplication()
    ret4 = obj1.Division()

    print("Details Of 1st Arithmetic Operations ")
    print("Addition : ",ret1)
    print("Subtraction : ",ret2)
    print("Multiplication : ",ret3)
    if ret4 == False:
        print("Division Not Possible")
    else:
        print("Division : ",ret4)

    
    print("Enter Information of 2nd Aritmetic Operation")
    obj2.Accept()
    ret1 = obj2.Addition()
    ret2 = obj2.Subtraction()
    ret3 = obj2.Multiplication()
    ret4 = obj2.Division()

    print("Details Of 2nd Arithmetic Operations ")
    print("Addition : ",ret1)
    print("Subtraction : ",ret2)
    print("Multiplication : ",ret3)
    if ret4 == False:
        print("Division Not Possible")
    else:
        print("Division : ",ret4)
    
if __name__ == "__main__":
    main()

