minimum = lambda a, b: a if a < b else b

def main():
    Value1 = int(input("Enter a number1 : "))
    Value2 = int(input("Enter a number2 : "))

    Ans = minimum(Value1, Value2)
    print(f"Minimum of {Value1} and {Value2} is {Ans}")


if __name__ == "__main__":
    main()