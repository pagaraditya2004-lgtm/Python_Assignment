def TotalCountDigit(Num):
    if Num == 0:
        return 1
    
    Count = 0
    while Num > 0:
        Count += 1
        Num //= 10
    return Count

def main():
    Val = int(input("Enter a number: "))
    ret = TotalCountDigit(Val)
    print("The number of digits in", Val, "is", ret)

if __name__ == "__main__":
    main()