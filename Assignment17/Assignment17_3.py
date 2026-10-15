def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact


def main():
    value = int(input("Enter a number: "))
    ret = factorial(value)
    print(f"Factorial of {value} is {ret}")

if __name__ == "__main__":
    main()