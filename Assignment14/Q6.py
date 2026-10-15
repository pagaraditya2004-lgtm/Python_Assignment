is_odd = lambda num: num % 2 != 0

def main():
    Value = int(input("Enter a number : "))

    is_odd(Value)
    
    if(is_odd(Value)):
        print(f"{Value} is Odd")

    else:
        print(f"{Value} is Even")

if __name__ == "__main__":
    main()