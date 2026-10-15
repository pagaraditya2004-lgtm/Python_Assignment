import datetime
import time
import schedule


def create_log_file():

    now = str(datetime.datetime.now())
    now = now.replace(" ","_")
    now = now.replace(":","_")
    
    filename_time = now
    filename = f"MarvellousLog_{filename_time}.txt"


    content_time = datetime.datetime.now()

    file_obj = open(filename, "w")
    file_obj.write("Log file created successfully.\n")
    file_obj.write(f"Creation Time: {content_time}\n")
    file_obj.close()

    print(f"[INFO] Created Log File: {filename}")
    print("-" * 40)


def main():
    border = "-" * 40

    print(border)
    print(" Marvellous Automation Script : Periodic Log Creator ")
    print(border)

    
    schedule.every(1).minutes.do(create_log_file)

    while True:
        schedule.run_pending()
        #time.sleep(1)


##########################################################
#
#   Starter of the automation script
#
##########################################################

if __name__ == "__main__":
    main()