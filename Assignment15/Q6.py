from functools import reduce


def main() -> None:
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    minimum = reduce(lambda x, y: x if x < y else y, numbers)

    print("Minimum Element:", minimum)


if __name__ == "__main__":
    main()