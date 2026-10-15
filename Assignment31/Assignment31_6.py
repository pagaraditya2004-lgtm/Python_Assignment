import time
import schedule


def start_weekly_goals():
    print("Start your weekly goals")


def review_weekly_progress():
    print("Review your weekly progress")


def complete_weekly_work():
    print("Weekly work completed")


def main():
    border = "-" * 40

    print(border)
    print(" Marvellous Automation Script : Weekly Scheduler ")
    print(border)

    schedule.every().monday.at("09:00").do(start_weekly_goals)

    schedule.every().wednesday.at("17:00").do(review_weekly_progress)

    schedule.every().friday.at("18:00").do(complete_weekly_work)

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