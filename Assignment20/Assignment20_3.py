import threading

def EvenListSum(Arr):
    EvenList = []
    Sum = 0

    for A in Arr:
        if A%2==0:
            EvenList.append(A)
            Sum = Sum+A
        
    print(f"EvenList = {EvenList}")
    print(f"Sum of Even number = {Sum}")

def OddListSum(Arr):
    OddList = []
    Sum = 0

    for A in Arr:
        if A%2!=0:
            OddList.append(A)
            Sum = Sum+A
        
    print(f"OddList = {OddList}")
    print(f"Sum of Odd number = {Sum}")
    

def main():

    Size = int(input("Enter Size of list : "))
    Arr = []
    for i in range(Size):
        No = int(input())
        Arr.append(No)
        
    print(f"Actual list : {Arr}")
    

    t1 = threading.Thread(target=EvenListSum, args=(Arr,))
    t2 = threading.Thread(target=OddListSum, args=(Arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from Main")

if __name__ == "__main__":
    main()


    