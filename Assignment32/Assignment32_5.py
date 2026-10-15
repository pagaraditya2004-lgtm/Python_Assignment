import os
import schedule
import time
import datetime


def delete_empty_files(dir_name):

    if not os.path.exists(dir_name):
        print("[ERROR] Directory does not exist.")
        return

    if not os.path.isdir(dir_name):
        print("[ERROR] Invalid directory.")
        return

    deleted_files = 0

    log_file = open("DeleteLog.txt", "a")

    log_file.write("-" * 50 + "\n")
    log_file.write(f"Execution Time : {datetime.datetime.now()}\n")
    log_file.write(f"Directory      : {dir_name}\n")

    for FolderName, SubFolder, FileName in os.walk(dir_name):

        for fname in FileName:

            file_path = os.path.join(FolderName, fname)

            if os.path.isfile(file_path):

                if os.path.getsize(file_path) == 0:

                    os.remove(file_path)

                    deleted_files += 1

                    log_file.write(f"Deleted : {file_path}\n")

    log_file.write(f"Total Empty Files Deleted : {deleted_files}\n")
    log_file.write("-" * 50 + "\n")

    log_file.close()

    print("Total Empty Files Deleted :", deleted_files)


def main():

    print("-" * 50)
    print("Marvellous Automation Script : Empty File Deleter")
    print("-" * 50)

    directory = input("Enter Directory : ")

    schedule.every(10).seconds.do(delete_empty_files, directory)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()