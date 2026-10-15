def MaxList(Arr):
    max_val = Arr[0]
    for i in Arr:
        if i > max_val:
            max_val = i

    return max_val

def main():
    Size = int(input("How many no. u want in list : "))
    items = []

    print("Enter the elements : ")
    for i in range(Size):
        no = int(input())
        items.append(no)

    ret = MaxList(items)

    print(f"Max in {items} is {ret}")



if __name__ == "__main__":
    main()