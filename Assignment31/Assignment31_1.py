import schedule
import time

def display_msg(msg):
     print(msg)


def main():
    Border = "-"*40
   
    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    message = input("Enter msg u want to show : ")
    timeInterval = int(input("Enter specific time Interval : "))

    
    schedule.every(timeInterval).seconds.do(display_msg,message)
            
    while True:
            schedule.run_pending()
            #time.sleep(10)
                    
   

    print(Border)
    print(" Thank you for using Marvellous Automation Script ")
    print(Border)

##########################################################
#
#   Starter of the automation script
#
##########################################################

if __name__ == "__main__":
    main()