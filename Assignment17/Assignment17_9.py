def NumCount(No):
    No = abs(No)

    if No == 0:
        return False

    count = 0
    while No > 0:
        count = count+1
        No = int(No/10)

    return count    

def main():
    value = int(input("Enter a Number :"))
    ret = NumCount(value)
    print("Count is : ",ret)

if __name__ == "__main__":
    main()