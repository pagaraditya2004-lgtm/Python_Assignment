largest = lambda a, b, c: a if a >= b and a >= c else (b if b >= c else c)

def main():
    Value1 = int(input("Enter a number1 : "))
    Value2 = int(input("Enter a number2 : "))
    value3 = int(input("Enter a number3 : "))

    Ans = largest(Value1, Value2, value3)
    print(f"Largest of {Value1}, {Value2} and {value3} is {Ans}")


if __name__ == "__main__":
    main()