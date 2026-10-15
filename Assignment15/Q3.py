def main() -> None:
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    odd_numbers = list(filter(lambda num: num % 2 != 0, numbers))

    print("Odd Numbers:", odd_numbers)


if __name__ == "__main__":
    main()