import schedule
import time

def Display():
    print("Coding kar..!")

def main():

    schedule.every(30).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(600)

if __name__ == "__main__":
    main()