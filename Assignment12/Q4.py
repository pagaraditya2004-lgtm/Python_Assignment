def PrintNumbers(Num):
    if Num <= 0:
        return False
    
    list = []
    for i in range(1, Num + 1):
        list.append(i)
    return list

def main():
    Value = int(input("Enter a number: "))
    numbers = PrintNumbers(Value)
    if PrintNumbers(Value) == False:
        print("Please enter a positive number.")
    else:
        print("Numbers from 1 to", Value, "are:", numbers)

if __name__ == "__main__":
    main()