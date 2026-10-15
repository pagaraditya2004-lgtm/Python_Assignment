def ChkPerfect(No):
    Sum = 0
    for i in range(1, No):
        if (No % i == 0):
            Sum += i
    if (Sum == No):
        return True
    else:
        return False

def main():
    Num = int(input("Enter a number: "))
    if ChkPerfect(Num):
        print(Num, "is a perfect number.")      
    else:
        print(Num, "is not a perfect number.")

if __name__ == "__main__":
    main()