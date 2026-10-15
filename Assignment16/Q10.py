def CountLen(str):
    count = 0

    for i in str:
        count += 1
    
    print("Length of string is :",count)

def main():
    Value= input("Enter a string :")
    CountLen(Value)

if __name__ == "__main__":
    main()