def AllEven(Num):
    list = []
    for i in range(1, Num + 1):
        if i % 2 == 0:
            list.append(i)
    return list

def main():
    Val = int(input("Enter a number: "))
    result = AllEven(Val)
    print("The even numbers from 1 to", Val, "is:", result)

if __name__ == "__main__":
    main()