def FactorsAdd(No):
    Sum = 0
    for i in range(1,No):
        if No % i == 0:
            Sum = Sum + i
    return Sum

def main():
    Value = int(input("Enter a number :"))
    ret = FactorsAdd(Value)
    print(f"Addition of Factors of {Value} is {ret}")

if __name__ == "__main__":
    main()
