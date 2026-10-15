def display_pattern(rows):
    for i in range(rows):
        for j in range(rows):
            print("*", end=" ")

        print()
        
def main():
    rows = int(input("Enter number of rows: "))
    display_pattern(rows)


if __name__ == "__main__":
    main()  