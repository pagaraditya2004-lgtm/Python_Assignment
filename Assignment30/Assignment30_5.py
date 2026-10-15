import schedule
import time
import datetime

def FileWrite():
    fobj = open("Marvellous.txt","a")
    fobj.write(f"Task executed at : {datetime.datetime.now()}")

def main():

    schedule.every(1).minutes.do(FileWrite)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()