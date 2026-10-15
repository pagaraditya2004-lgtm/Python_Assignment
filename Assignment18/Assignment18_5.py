import MarvellousNum

def ListPrime(Arr):
    Total = 0

    for element in Arr:
        Total = Total + element
    
    return Total
    

def main():
    Arr = []
    Size = int(input("Enter the No. of elements u want in : "))

    print("Enter the elements :")
    for i in range(Size):
        value = int(input())
        Arr.append(value)
    
    PrimeArrr = MarvellousNum.ChkPrime(Arr)

    ret = ListPrime(PrimeArrr)
    print(f"prime no in {Arr} is {PrimeArrr} and There Summation is = {ret}")

if __name__ == "__main__":
    main()