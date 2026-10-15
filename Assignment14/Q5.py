is_even = lambda num: num % 2 == 0

def main():
    Value = int(input("Enter a number : "))

    is_even(Value)
    
    if(is_even(Value)):
        print(f"{Value} is Even")

    else:
        print(f"{Value} is Odd")

if __name__ == "__main__":
    main()