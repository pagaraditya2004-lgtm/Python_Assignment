import threading


def find_maximum(numbers):

    print("Maximum Element :", max(numbers))


def find_minimum(numbers):

    print("Minimum Element :", min(numbers))


def main():

    Size = int(input("Enter how many No. u want in list : "))

    Arr = []

    for i in range(Size):
        Element = int(input())
        Arr.append(Element)

    thread1 = threading.Thread(target=find_maximum, args=(Arr,))
    thread2 = threading.Thread(target=find_minimum, args=(Arr,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()