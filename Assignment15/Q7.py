def main() -> None:
    words = input("Enter words separated by space: ").split()

    result = list(filter(lambda word: len(word) > 5, words))

    print("Filtered Strings:", result)


if __name__ == "__main__":
    main()