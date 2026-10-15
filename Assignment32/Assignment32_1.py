import datetime
import time
import schedule


def create_timestamp_file():

    now = str(datetime.datetime.now())
    now = now.replace(" ","_")
    now = now.replace(":","_")
        
    filename_time = now
    filename = f"MarvellousLog_{filename_time}.txt"

    
    creation_date = datetime.datetime.now()
    date = creation_date.date()
    creation_time = datetime.datetime.now()
    time = creation_time.time()

    file_obj = open(filename, "w")
    file_obj.write(f"Filename: {filename}\n")
    file_obj.write(f"Creation date: {date}\n")
    file_obj.write(f"Creation time: {time}\n")
    file_obj.close()

    print(f"[INFO] File Created Successfully: {filename}")
    print("-" * 40)


def main():
    border = "-" * 40

    print(border)
    print(" Marvellous Automation Script : Text File Creator ")
    print(border)

    schedule.every(1).minutes.do(create_timestamp_file)


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