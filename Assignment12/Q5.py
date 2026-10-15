def PrintRevNumbers(Num):
    if Num <= 0:
        return False
    
    list = []
    for i in range(Num, 0, -1):
        list.append(i)
    return list

def main():
    Value = int(input("Enter a number: "))
    numbers = PrintRevNumbers(Value)
    if PrintRevNumbers(Value) == False:
        print("Please enter a positive number.")
    else:
        print("Numbers from", Value, "to 1 are:", numbers)

if __name__ == "__main__":
    main()