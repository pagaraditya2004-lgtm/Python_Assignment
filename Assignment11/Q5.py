from Q4 import Reverse

def IsPalindrome(Num):
    Rev = Reverse(Num)
    if Num == Rev:
        return True
    else:
        return False

def main():
    Val = int(input("Enter a number: "))
    ret = IsPalindrome(Val)
    if ret:
        print("The number", Val, "is a palindrome.")
    else:
        print("The number", Val, "is not a palindrome.")

if __name__ == "__main__":
    main()