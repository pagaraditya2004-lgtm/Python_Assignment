def SummationList(List):
    add = 0
    for no in List:
        add = add + no
    return add

def main():
    Size = int(input("How many no. u want in list : "))
    list = []

    print("Enter the elements : ")
    for i in range(Size):
        no = int(input())
        list.append(no)

    ret = SummationList(list)

    print(f"Summation of {list} is {ret}")



if __name__ == "__main__":
    main()