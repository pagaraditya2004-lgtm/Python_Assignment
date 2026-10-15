def SumDigit(Num):
    Count = 0
    while Num > 0:
        Count += Num % 10
        Num //= 10
    return Count

def main():
    Val = int(input("Enter a number: "))
    ret = SumDigit(Val)
    print("The sum of digits in", Val, "is", ret)

if __name__ == "__main__":
    main()