from functools import reduce


def main() -> None:
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    total = reduce(lambda x, y: x + y, numbers)

    print("Sum:", total)


if __name__ == "__main__":
    main()