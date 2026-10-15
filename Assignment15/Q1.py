def main():
    
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    squares = list(map(lambda num: num ** 2, numbers))

    print("Squares:", squares)


if __name__ == "__main__":
    main()