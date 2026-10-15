def AreaCircle(R,PI=3.14):
    return PI * R ** 2

def main():
    radius = int(input("Enter the radius of the circle: "))
    Area = AreaCircle(radius)
    print("The area of the circle is:", Area)

if __name__ == "__main__":
    main()