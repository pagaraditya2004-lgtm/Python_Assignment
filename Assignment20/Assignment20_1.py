import threading

def DisplayEven():
    Arr = []
    for i in range(2,21,2):
        Arr.append(i)

    print(f"Even list = {Arr}")

def DisplayOdd():
    Arr = []
    for i in range(1,21,2):
        Arr.append(i)

    print(f"Odd list = {Arr}")

def main():

    t1 = threading.Thread(target=DisplayEven)
    t2 = threading.Thread(target=DisplayOdd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()


    