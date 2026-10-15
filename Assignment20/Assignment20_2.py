import threading

def EvenFactor(No1):
    Sum = 0
    for i in range(1,No1+1):
        if(No1%i == 0 and i % 2 == 0):
            Sum = Sum + i

    print(f"Sum of even factor = {Sum}")

def OddFactor(No2):
    Sum = 0
    for i in range(1,No2+1):
        if(No2%i == 0 and i % 2 != 0):
            Sum = Sum + i
            
    print(f"Sum of odd factor = {Sum}")
    

def main():

    No1 = int(input("Enter No1 : "))
    No2 = int(input("Enter No2 : "))

    t1 = threading.Thread(target=EvenFactor, args=(No1,))
    t2 = threading.Thread(target=OddFactor, args=(No2,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from Main")

if __name__ == "__main__":
    main()


    