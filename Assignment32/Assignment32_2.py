import datetime
import os
import time
import schedule


def monitor_file_size(file_path):

    if not os.path.exists(file_path):
        print(f"[ERROR] Specified file does not exist: {file_path}")
        print("-" * 40)
        return

    file_size = os.path.getsize(file_path)

    now_obj = datetime.datetime.now()
    current_time = now_obj.time()

    # Append details into FileSizeLog.txt
    log_file = open("FileSizeLog.txt", "a")
    log_file.write(f"File path: {file_path}\n")
    log_file.write(f"File size in bytes: {file_size}\n")
    log_file.write(f"Date and time: {current_time}\n")
    log_file.write("-" * 40 + "\n")
    log_file.close()

    print(f"[INFO] Monitored File: {file_path}")
    print(f"File Size: {file_size} bytes")
    print(f"Log Updated At: {current_time}")
    print("-" * 40)


def main():
    border = "-" * 40

    print(border)
    print(" Marvellous Automation Script : File Size Monitor ")
    print(border)

    file_path = input("Enter target file path to monitor : ")

    schedule.every(30).seconds.do(monitor_file_size, file_path)

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