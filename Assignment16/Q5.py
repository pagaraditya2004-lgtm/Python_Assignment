def Reverse(No):
    list = []
    for i in range(No,0,-1):
        list.append(i)

    print(list)

def main():
    value= (int(input("Enter the No. upto which u want to print in reverse order :")))
    Reverse(value)

if __name__ == "__main__":
    main()