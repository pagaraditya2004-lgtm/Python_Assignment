import os

def main():
    print("Enter file name : ")
    Fname = input()

    if(os.path.exists(Fname)):
        print(f"{Fname} exists")
    else:
        print(f"{Fname} not exists")

if __name__ == "__main__":
    main()