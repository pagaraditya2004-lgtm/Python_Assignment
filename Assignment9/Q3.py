def Square(Num):
    return Num * Num

def main():
    Val = int(input("Enter first number: "))
    result = Square(Val)
    print("Square of", Val, "is", result)  

if __name__ == "__main__":
    main()