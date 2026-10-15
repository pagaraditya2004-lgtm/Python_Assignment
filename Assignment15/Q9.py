from functools import reduce


def main() -> None:
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    product = reduce(lambda x, y: x * y, numbers)

    print("Product:", product)


if __name__ == "__main__":
    main()