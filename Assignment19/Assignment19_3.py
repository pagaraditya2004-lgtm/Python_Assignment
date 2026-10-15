from functools import reduce 

FilterNumber = lambda x : 70 <= x <=90
MapNumber = lambda x : x + 10
ReduceNumber = lambda X, y : X*y

def main():
    Size = int(input("Enter how many No. u want in list : "))

    Arr = []

    for i in range(Size):
        Element = int(input())
        Arr.append(Element)

    FilterList = list(filter(FilterNumber, Arr))
    MapList = list(map(MapNumber, FilterList))
    Reduce = int(reduce(ReduceNumber,MapList))

    print(f"input list is {Arr}")
    print(f"List After filter = {FilterList}")
    print(f"List after Map = {MapList}")
    print(f"Output of reduce = {Reduce}")

if __name__ == "__main__":
    main()