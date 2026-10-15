def IsPrime(No):
    if No<=1:
        return False
    
    for i in range(2,No):
        if No % i == 0:
            return False
        else:
            return True

def main():
    Value = int(input("Enter a number :"))
    ret = IsPrime(Value)
    if ret == True:
        print(f"{Value} is Prime")
    else:
        print(f"{Value} is not Prime")

if __name__ == "__main__":
    main()
