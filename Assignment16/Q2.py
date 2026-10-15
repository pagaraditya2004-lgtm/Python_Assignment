def ChkNum(Num):
    if Num % 2 == 0:
        print(f"{Num} is Even")
    
    else:
        print(f"{Num} is Odd")

def main():
    Value = int(input("Enter a Num :"))

    ChkNum(Value)

if __name__ == "__main__":
    main()