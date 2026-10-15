def ChkFrequency(Arr,No):
    Count = 0
    for a in Arr:
        if No == a:
            Count = Count+1
    return Count

def main():
    Arr = []
    Size = int(input("Total No. u want in list : "))

    print("Enter the Elements : ")
    for i in range(Size):
        value = int(input()) 
        Arr.append(value)

    No = int(input("Enter the no. to check its frequency : "))
        
    ret = ChkFrequency(Arr,No)

    print(f"Count of {No} in {Arr} is {ret}")

if __name__ == "__main__":
    main()