def ChkVowel(char):
    if char in 'aeiouAEIOU':
        return True
    else:
        return False

def main():
    char = input("Enter a character: ")
    if len(char) != 1:
        print("Please enter a single character.")
        return

    if ChkVowel(char):
        print(char," is a vowel.")
    else:
        print(char," is not a vowel.")

if __name__ == "__main__":
    main()