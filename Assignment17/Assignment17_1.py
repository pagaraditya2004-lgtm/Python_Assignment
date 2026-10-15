import Arithmetic

def main():
    Value1 = int(input("Enter a first number : "))
    Value2 = int(input("Enter a second number : "))

    Addition = Arithmetic.Add(Value1,Value2)
    Subtraction = Arithmetic.Sub(Value1,Value2)
    Multiplication = Arithmetic.Multi(Value1,Value2)
    Division = Arithmetic.Div(float(Value1),float(Value2))

    print("Addition is : ",Addition)
    print("Subtraction is : ",Subtraction)
    print("Multiplication is : ",Multiplication)
    print("Division is : ",Division)

if __name__ == "__main__":
    main()
