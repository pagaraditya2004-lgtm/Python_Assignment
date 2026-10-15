def Add(A, B):
    Ans = A+B
    return Ans

def main():
    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))

    ret = Add(No1, No2)

    print(f"Addition of {No1} and {No2} is : {ret}")

if __name__ == "__main__":
    main()