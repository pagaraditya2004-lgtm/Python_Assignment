import threading


def count_small(text: str) -> None:
    count = 0

    for character in text:
        if character.islower():
            count += 1

    print("Thread ID   :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Lowercase Characters :", count)
    print()


def count_capital(text: str) -> None:
    count = 0

    for character in text:
        if character.isupper():
            count += 1

    print("Thread ID   :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Uppercase Characters :", count)
    print()


def count_digits(text: str) -> None:
    count = 0

    for character in text:
        if character.isdigit():
            count += 1

    print("Thread ID   :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digits :", count)
    print()


def main() -> None:
    text = input("Enter a string: ")

    small_thread = threading.Thread(target=count_small,args=(text,))

    capital_thread = threading.Thread(target=count_capital,args=(text,))

    digit_thread = threading.Thread(target=count_digits,args=(text,))

    small_thread.start()
    capital_thread.start()
    digit_thread.start()

    small_thread.join()
    capital_thread.join()
    digit_thread.join()

    print("Exit from Main")


if __name__ == "__main__":
    main()