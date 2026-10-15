import schedule
import time
import datetime

def DisplayDate():
    print("Current Date and Time : ",datetime.datetime.now())

def main():

    schedule.every(1).minutes.do(DisplayDate)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()