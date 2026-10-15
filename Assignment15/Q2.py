def main():
  
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    even_numbers = list(filter(lambda num: num % 2 == 0, numbers))

    print("Even Numbers:", even_numbers)


if __name__ == "__main__":
    main()