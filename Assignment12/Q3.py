def Addition(No1, No2):
    Ans = No1 + No2
    return Ans

def Substraction(No1, No2):
    Ans = No1 - No2
    return Ans
    
def Multiplication(No1, No2):
    Ans = No1 * No2
    return Ans

def Division(No1, No2):
    Ans = No1 / No2
    return Ans         

def main():
    print("Enter first number")
    Value1 = int(input())

    print("Enter second number")
    Value2 = int(input())

    Ret = Addition(Value1, Value2)
    print("Addition is : ", Ret)

    Ret = Substraction(Value1, Value2)
    print("Substraction is : ", Ret)

    Ret = Multiplication(Value1, Value2)
    print("Multiplication is : ", Ret)

    Ret = Division(Value1, Value2)
    print("Division is : ", Ret)

if __name__ == "__main__": 
    main()  