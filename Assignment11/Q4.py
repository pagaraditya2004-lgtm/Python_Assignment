def Reverse(Num):
    Rev = 0
    while Num > 0:
        Rev = Rev * 10 + Num % 10
        Num //= 10
    return Rev

def main():
    Val = int(input("Enter a number: "))
    ret = Reverse(Val)
    print("The reverse of", Val, "is", ret)

if __name__ == "__main__":
    main()