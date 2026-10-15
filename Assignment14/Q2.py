Cube = lambda No : No ** 3

def main():
    Value = int(input("Enter a number : "))

    Ans = Cube(Value)
    print(f"Cube of {Value} is {Ans}")

if __name__ == "__main__":
    main()