def main() -> None:
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    even_count = len(list(filter(lambda num: num % 2 == 0, numbers)))

    print("Count of Even Numbers:", even_count)


if __name__ == "__main__":
    main()