def SumDigits(No):
    No = abs(No)

    if No == 0:
        return False

    Sum = 0
    while No > 0:
        div = No%10
        Sum = Sum + div
        No = int(No/10)

    return Sum   

def main():
    value = int(input("Enter a Number :"))
    ret = SumDigits(value)
    print("Sum is : ",ret)

if __name__ == "__main__":
    main()