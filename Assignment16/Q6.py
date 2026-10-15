def ChkNum(No):
    if No == 0:
        print(f"{No} is Zero")

    elif No > 0:
        print(f"{No} is Positive")

    else:
        print(f"{No} is Negative")

def main():
    Value = int(input("Enter a Num : "))
    ChkNum(Value)

if __name__ == "__main__":
    main()