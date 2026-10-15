def CheckDivisiblity(No):
    if (No % 3 == 0 and No % 5 == 0):
        return True
    else:
        return False

def main():
    Value = int(input("Enter a No. :"))

    Ret = CheckDivisiblity(Value)

    if(Ret == True):
        print("It is divisible by both 3 and 5.")
    else:
        print("It is not divisible by both 3 and 5.")

if __name__ == "__main__":
    main()