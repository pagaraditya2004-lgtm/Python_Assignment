def IsPrime(Num):
    if Num <= 1:
        return False
    for i in range(2, int(Num**0.5) + 1):
        if Num % i == 0:
            return False
    return True

def main():
    Val = int(input("Enter a number: "))
    if IsPrime(Val):
        print(Val ,"is a prime number.")
    else:
        print(Val ,"is not a prime number.")

if __name__ == "__main__":
    main()