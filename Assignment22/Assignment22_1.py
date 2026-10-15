import multiprocessing

def SquareSum(Num):
    Sum = 0
    for i in range(1,Num+1):
        Sum = Sum + i * i
    return Sum


def main():
    Arr = []

    Size = int(input("Enter the No. of elements u want in list : "))

    for i in range(Size):
        Element = int(input())
        Arr.append(Element)

    Pobj = multiprocessing.Pool()

    ret = Pobj.map(SquareSum,Arr)

    Pobj.close()
    Pobj.join()

    print(f"Result = {ret}")

if __name__ == "__main__":
    main()

    