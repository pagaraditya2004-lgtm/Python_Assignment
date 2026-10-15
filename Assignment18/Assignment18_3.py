def MinList(Arr):
    min_val = Arr[0]
    for i in Arr:
        if i < min_val:
            min_val = i

    return min_val

def main():
    Size = int(input("How many no. u want in list : "))
    items = []

    print("Enter the elements : ")
    for i in range(Size):
        no = int(input())
        items.append(no)

    ret = MinList(items)

    print(f"Min in {items} is {ret}")



if __name__ == "__main__":
    main()