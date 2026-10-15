def AreaRectangle(Len,Wid):
    return Len * Wid

def main():
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    Area = AreaRectangle(length, width)
    print("The area of the rectangle is:", Area)

if __name__ == "__main__":
    main()