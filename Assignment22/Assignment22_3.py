import multiprocessing

def CountPrime(Num):

    Count = 0

    if Num <= 1:
        isPrime = False
    else:
        for i in range(2, Num+1):
            isPrime = True

            for j in range(2, i):
                if i % j == 0:
                    isPrime = False
                    break

            if isPrime == True:
                Count = Count+1

    return Count

def main():
    Size = int(input("Enter No. of Elements u want in list :"))
    Arr = []

    print("Enter the Elements : ")
    for i in range(Size):
        Element = int(input())
        Arr.append(Element)

    Pobj = multiprocessing.Pool()

    ret = Pobj.map(CountPrime, Arr)

    Pobj.close()
    Pobj.join()

    print(f"Count of Prime No = {ret}")

if __name__ == "__main__":
    main()