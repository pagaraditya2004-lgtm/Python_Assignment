import multiprocessing
import time

def SumPower(Num):

    Sum = 0

    for i in range (1,Num+1):
        Sum = Sum + (i ** 5)

    return Sum 

   

def main():
    Size = int(input("Enter No. of Elements u want in list :"))
    Arr = []

    print("Enter the Elements : ")
    for i in range(Size):
        Element = int(input())
        Arr.append(Element)

    start_time = time.perf_counter()

    Pobj = multiprocessing.Pool()

    ret = Pobj.map(SumPower, Arr)

    Pobj.close()
    Pobj.join()

    end_time = time.perf_counter()

    print(f"Sum of Power 5 from 1 to N  = {ret}")

    print(f"Execution time : {end_time - start_time:.4f} Seconds")

if __name__ == "__main__":
    main()