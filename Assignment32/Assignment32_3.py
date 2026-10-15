import os
import time
import schedule


def read_file_contents(file_path):
    
    if not os.path.exists(file_path):
        print("[ERROR] File does not exist.")
        print("-" * 40)
        return

    if os.path.getsize(file_path) == 0:
        print("[WARNING] File is empty.")
        print("-" * 40)
        return

    file_obj = open(file_path, "r")
    content = file_obj.read()
    file_obj.close()

    print("--- File Content Start ---")
    print(content)
    print("--- File Content End ---")
    print("-" * 40)


def main():
    border = "-" * 40

    print(border)
    print(" Marvellous Automation Script : Periodic File Content Reader ")
    print(border)

    file_path = input("Enter file path to read : ")

    schedule.every(5).seconds.do(read_file_contents, file_path)


    while True:
        schedule.run_pending()
        time.sleep(1)


##########################################################
#
#   Starter of the automation script
#
##########################################################

if __name__ == "__main__":
    main()