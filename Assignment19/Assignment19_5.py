from functools import reduce 

def FilterNumber(Number):

    if Number <= 1:
         return False
    
    for i in range(2,Number):
            if Number % i == 0:
                 return False
            
    return True


MapNumber = lambda x : x * 2
ReduceNumber = lambda x, y : x if x > y else y

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