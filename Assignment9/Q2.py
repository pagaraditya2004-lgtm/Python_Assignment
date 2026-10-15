def ChkGreater(Num1, Num2):
    if Num1 > Num2:
        print(Num1 ,"is greater")
    elif Num2 > Num1:
        print(Num2 ,"is greater")
    else:
        print("Both numbers are equal")

def main():
    Val1 = int(input("Enter first number: "))
    Val2 = int(input("Enter second number: "))
    ChkGreater(Val1, Val2)

if __name__ == "__main__":
    main()