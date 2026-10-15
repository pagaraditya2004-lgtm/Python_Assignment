import os
import shutil
import schedule
import time
import datetime


def copy_text_files(source_dir, destination_dir):

    if not os.path.exists(source_dir):
        print("[ERROR] Source directory does not exist.")
        return

    if not os.path.isdir(source_dir):
        print("[ERROR] Source path is not a directory.")
        return

    if not os.path.exists(destination_dir):
        print("[ERROR] Destination directory does not exist.")
        return

    if not os.path.isdir(destination_dir):
        print("[ERROR] Destination path is not a directory.")
        return

    copied_files = 0

    log_file = open("CopyLog.txt", "a")

    log_file.write("-" * 50 + "\n")
    log_file.write(f"Copy Time : {datetime.datetime.now()}\n")
    log_file.write(f"Source    : {source_dir}\n")
    log_file.write(f"Destination : {destination_dir}\n")

    for FolderName, SubFolder, FileName in os.walk(source_dir):

        for fname in FileName:

            if fname.endswith(".txt"):

                source_path = os.path.join(FolderName, fname)
                destination_path = os.path.join(destination_dir, fname)

                if os.path.isfile(source_path):

                    shutil.copy(source_path, destination_path)

                    copied_files += 1

                    log_file.write(f"Copied : {source_path}\n")

    log_file.write("Total Files Copied : {copied_files}\n")
    log_file.write("-" * 50 + "\n")

    log_file.close()

    print("Total TXT Files Copied :", copied_files)


def main():

    print("-" * 50)
    print("Marvellous Automation Script : TXT File Copier")
    print("-" * 50)

    source = input("Enter Source Directory      : ")
    destination = input("Enter Destination Directory : ")

    schedule.every(10).minutes.do(copy_text_files, source, destination)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()