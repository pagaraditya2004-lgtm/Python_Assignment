import os
import multiprocessing

def Factorials(Num):
    Fact = 1
    for i in range(1,Num+1):
        Fact = Fact * i
    return Fact

def main():
    Arr = []
    Size = int(input("Enter No. of Elements u want in list : "))

    for i in range(Size):
        Element = int(input())
        Arr.append(Element)

    print(f"Original List = {Arr}")

    print(f"Processing Id = {os.getpid()}")

    Pobj = multiprocessing.Pool()

    ret = Pobj.map(Factorials, Arr)

    Pobj.close()
    Pobj.join()

    print(f"Factorial = {ret}")

if __name__ == "__main__":
    main()