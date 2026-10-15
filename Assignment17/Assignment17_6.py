def display_pattern(rows):
    for i in range(rows,0,-1):
        for j in range(i):
            print("*", end=" ")
        print()


def main():
    no = int(input("Enter number of rows: "))
    display_pattern(no)


if __name__ == "__main__":
    main()