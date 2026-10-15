class Circle():

    PI = 3.14

    def __init__(self):
        self.r = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.r = float(input("Enter Radius : "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.r * self.r

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.r

    def Display(self):
        print("Radius of Circle : ",self.r)
        print("Area of Circle : ",self.Area)
        print("Circumference of Circle : ",self.Circumference)

def main():
    obj1 = Circle()
    obj2 = Circle()

    print("Information of Circle1")
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    print("Circle 1 Details")
    obj1.Display()

    print("Information of Circle2")
    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    print("Circle 2 Details")
    obj2.Display()

if __name__ == "__main__":
    main()