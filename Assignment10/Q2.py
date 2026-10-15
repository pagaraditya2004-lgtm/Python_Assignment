def Sum(Num):
    Total = 0
    for i in range(1, Num + 1):
        Total += i
    return Total

def main():
    Num = int(input("Enter a number: "))
    ret = Sum(Num)
    print("The sum of numbers from 1 to ",Num ,"is:",ret)

if __name__ == "__main__":
    main()