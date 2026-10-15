def Cube(Num):
    return Num * Num * Num

def main():
    Val = int(input("Enter first number: "))
    result = Cube(Val)
    print("Cube of", Val, "is", result)  

if __name__ == "__main__":
    main()