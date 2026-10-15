def ConvertToBinary(Num):
    return bin(Num)

def main():
    Number = int(input("Enter a number: "))
    Binary = ConvertToBinary(Number)
    print("The binary representation of", Number, "is:", Binary)

if __name__ == "__main__":
    main()