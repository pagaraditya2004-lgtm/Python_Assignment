import threading


def is_prime(number):

    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def display_prime(numbers):

    print("Prime Numbers:")

    for number in numbers:
        if is_prime(number):
            print(number, end=" ")

    print()


def display_non_prime(numbers):

    print("Non Prime Numbers:")

    for number in numbers:
        if not is_prime(number):
            print(number, end=" ")

    print()


def main():

    Size = int(input("Enter how many No. u want in list : "))

    Arr = []

    for i in range(Size):
        Element = int(input())
        Arr.append(Element)

    thread1 = threading.Thread(target=display_prime, args=(Arr,))
    thread2 = threading.Thread(target=display_non_prime, args=(Arr,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()