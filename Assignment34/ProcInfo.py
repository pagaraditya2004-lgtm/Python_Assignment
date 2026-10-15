import sys
import psutil
import schedule
import time

def ProcessDisplay():
    Border = "-"*50
    print(Border)
    print("-----Process Information is as below : -----")
    print(Border)
    print(Border)
    print("-----Info : -----")
    print(Border)

    for proc in psutil.process_iter():
        try:
            pName = proc.name()
            pId = proc.pid
            Username = proc.username()

            print(f"Process Name : {pName}")
            print(f"Process ID : {pId}")
            print(f"Username : {Username}")

            print(Border)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def main():
    Border = "-"*50
    print(Border)
    print("----Marvellous Platform Survillence System ----")
    print(Border)

    # --h & --u handling
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script is used to perform :")
            print("1 : It fetch the information of running process")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation Script as : ")
            print("python ProcInfo.py")

        else:
            print("Enable to proceed as there no matching arguments")
            print("Please use --h or --u flag for getting more details")

    #Actual project code
    elif(len(sys.argv)==1):
        schedule.every(1).minutes.do(ProcessDisplay)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid numbers of Arguments")
        print("Enable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more details")

    print(Border)
    print("--ThankYou for using our Automation System--")
    print(Border)

if __name__ == "__main__":
    main()
    