import datetime
import os
import time
import schedule


def directory_count_logger(dir_name):

    if not os.path.exists(dir_name):
        print(f"[ERROR] Directory does not exist: {dir_name}")
        return

    if not os.path.isdir(dir_name):
        print(f"[ERROR] Provided path is not a directory: {dir_name}")
        return

    file_count = 0

    for FolderName, SubFolder, FileName in os.walk(dir_name):
        file_count = file_count + len(FileName)

    
    log_time = datetime.datetime.now()

    log_file = open("DirectoryCountLog.txt", "a")
    log_file.write(f"Directory path : {dir_name}\n")
    log_file.write(f"Number of files: {file_count}\n")
    log_file.write(f"Date and time  : {log_time}\n")
    log_file.write("-" * 40 + "\n")
    log_file.close()

    print(f"[INFO] Audited: {dir_name}")
    print(f"Total Files Found: {file_count}")
    print(f"Logged At: {log_time}")
    print("-" * 40)


def main():
    border = "-" * 40

    print(border)
    print(" Marvellous Automation Script : Directory File Counter Logger ")
    print(border)

    dir_name = input("Enter directory path to count files : ")

    schedule.every(5).seconds.do(directory_count_logger, dir_name)

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