import multiprocessing
import os

def SumEven(Num):

    Sum = 0

    
    for j in range(2, Num + 1,2):
         Sum = Sum + j

    return Sum

def main():
    Size = int(input("Enter No. of Elements u want in list :"))
    Arr = []

    print("Enter the Elements : ")
    for i in range(Size):
        Element = int(input())
        Arr.append(Element)

    Pobj = multiprocessing.Pool()

    ret = Pobj.map(SumEven, Arr)

    Pobj.close()
    Pobj.join()

    print(f"Process ID = {os.getpid()}")
    print(f"List of Even No = {Arr}")
    print(f"Sum of Even No = {ret}")

if __name__ == "__main__":
    main()