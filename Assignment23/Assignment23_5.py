import multiprocessing
import os

def Factorials(Num):
    Fact = 1
    for i in range(1,Num+1):
        Fact = Fact * i
    return Fact

def main():
    Size = int(input("Enter No. of Elements u want in list :"))
    Arr = []

    print("Enter the Elements : ")
    for i in range(Size):
        Element = int(input())
        Arr.append(Element)

    Pobj = multiprocessing.Pool()

    ret = Pobj.map(Factorials, Arr)

    Pobj.close()
    Pobj.join()

    print(f"Process ID = {os.getpid()}")
    print(f"List = {Arr}")
    print(f"Factorial = {ret}")

if __name__ == "__main__":
    main()