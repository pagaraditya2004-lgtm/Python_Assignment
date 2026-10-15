import threading


def display_forward() -> None:
    print("Thread1 Started")

    for number in range(1, 51):
        print(number)

    print("Thread1 Completed")


def display_reverse() -> None:
    print("Thread2 Started")

    for number in range(50, 0, -1):
        print(number)

    print("Thread2 Completed")


def main() -> None:
    thread1 = threading.Thread(target=display_forward,)

    thread2 = threading.Thread(target=display_reverse,)

    thread1.start()

    thread1.join()

    thread2.start()

    thread2.join()

    print("Exit from Main")


if __name__ == "__main__":
    main()