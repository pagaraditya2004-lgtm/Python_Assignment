def Fact(Num):
    Total = 1
    for i in range(1, Num + 1):
        Total *= i
    return Total

def main():
    Num = int(input("Enter a number: "))
    ret = Fact(Num)
    print("The factorial of ",Num ,"is:",ret)

if __name__ == "__main__":
    main()