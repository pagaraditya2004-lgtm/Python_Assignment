import sys
import psutil
import os
import time
import schedule

def ProcessInfo():
    
    ListProcess = []
    
    for proc in psutil.process_iter():
        try:
            info = {}
            info["name"] = proc.name()
            info["pid"] = proc.pid  
            info["username"] = proc.username()

            ListProcess.append(info)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return ListProcess  

    return ListProcess

def LogFile(FolderName):
    Border = "-"*50

    Ret = False

    Ret = os.path.exists(FolderName)

    if (Ret == True):
        Ret = os.path.isdir(FolderName)

        if (Ret == False):
            print("Enable to proceed as folder name is existing but it is not a directory")
    else:
        os.mkdir(FolderName)
        print("Directory is created with name : ", FolderName)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName, "MarvellousLog_" + timestamp + ".log")

    fobj = open(FileName, "w")

    print(f"Log file gets sucessfully created with name : {FileName}")

    fobj.write(Border + "\n")
    fobj.write("-----Process Information is as below : -----" + "\n")
    fobj.write("Log file created at : " + timestamp + "\n")
    fobj.write(Border + "\n")
    fobj.write(Border + "\n")
    fobj.write("-----Process Information : -----" + "\n")

    Data = ProcessInfo()

    for info in Data:
        fobj.write(f"Process Name : {info.get('name')} \n")
        fobj.write(f"Process ID : {info.get('pid')} \n")
        fobj.write(f"Username : {info.get('username')} \n")
        fobj.write(Border + "\n")


def main():
    Border = "-"*50
    print(Border)
    print("----Marvellous Platform Survillence System ----")
    print(Border)

    # --h & --u handling
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script is used to perform :")
            print("1 : It fetch the information of entered process name")
            print("2 : It maintains all records into log file")
    
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation Script as : ")
            print("python ProcInfo.py FolderName")
    
        #Actual project code
        else:
            schedule.every(1).minutes.do(LogFile, sys.argv[1])
                        
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
    