def main() -> None:
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    result = list(filter(lambda num: num % 3 == 0 and num % 5 == 0, numbers))

    print("Numbers Divisible by 3 and 5:", result)


if __name__ == "__main__":
    main()