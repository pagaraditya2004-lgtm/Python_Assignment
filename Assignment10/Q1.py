def Table(Num):
    for i in range(1, 11):
        print(Num, "*", i, "=" ,Num * i)

def main():
    Num = int(input("Enter a number: "))
    Table(Num)

if __name__ == "__main__":
    main()