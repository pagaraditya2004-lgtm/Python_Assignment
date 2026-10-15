import multiprocessing
import os

def CountOdd(Num):

    Count = 0

    
    for i in range(1, Num + 1,2):
         Count = Count + 1

    return Count

def main():
    Size = int(input("Enter No. of Elements u want in list :"))
    Arr = []

    print("Enter the Elements : ")
    for i in range(Size):
        Element = int(input())
        Arr.append(Element)

    Pobj = multiprocessing.Pool()

    ret = Pobj.map(CountOdd, Arr)

    Pobj.close()
    Pobj.join()

    print(f"Process ID = {os.getpid()}")
    print(f"List of Odd No = {Arr}")
    print(f"Count of Odd No = {ret}")

if __name__ == "__main__":
    main()