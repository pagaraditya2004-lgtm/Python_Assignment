def Factors(Num):
    if Num <= 0:
        return False
    list = []
    for i in range(1, Num + 1):
        if Num % i == 0:
            list.append(i)
    return list

def main():
    Value = int(input("Enter a number: "))
    factors = Factors(Value)
    if Factors(Value) == False:
        print("Please enter a positive number.")
    else:
        print("Factors of", Value, "are:", factors)

if __name__ == "__main__":
    main()  