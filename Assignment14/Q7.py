divisible_by_five = lambda num: num % 5 == 0

def main():
    Value = int(input("Enter a number : "))

    if(divisible_by_five(Value)):
        print(f"{Value} is divisible by 5")
    else:
        print(f"{Value} is not divisible by 5")

if __name__ == "__main__":
    main()