import datetime
import os
import time
import schedule


def scan_directory(dir_name):
    
    if not os.path.exists(dir_name):
        print(f"[ERROR] Directory does not exist: {dir_name}")
        return

    if not os.path.isdir(dir_name):
        print(f"[ERROR] Provided path is not a directory: {dir_name}")
        return

    files_count = 0
    subdirs_count = 0

    for FolderName, SubFolder, FileName in os.walk(dir_name):
        subdirs_count += len(SubFolder)
        files_count += len(FileName)
            

    scan_time = datetime.datetime.now()

    # Output details
    print(f"Directory Scanned: {dir_name}")
    print(f"Total Files: {files_count}")
    print(f"Total Subdirectories: {subdirs_count}")
    print(f"Scan Time: {scan_time}")
    print("-" * 40)


def main():
    border = "-" * 40

    print(border)
    print(" Marvellous Automation Script : Directory Scanner ")
    print(border)

    dir_name = input("Enter directory path to scan : ")

    schedule.every(1).minutes.do(scan_directory, dir_name)

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