import schedule
import time
import shutil
import os
import sys
import datetime

def Backup(FilePath, DirectoryPath):

    ret = False
    ret = os.path.exists(FilePath)

    if(ret == False):
        print("Error : There is No such Path with name ",FilePath)
        return

    ret = False
    ret = os.path.isdir(DirectoryPath)
    
    if(ret == False):
        print("Error : There is No such Directory with name ",DirectoryPath)
        return

    current_time = time.ctime()
    current_time = current_time.replace(" ","_")
    current_time = current_time.replace(":","_")

    BaseName = os.path.basename(FilePath)

    name, extension = os.path.splitext(BaseName)

    file_name = name+"_"+current_time+extension

    fname = os.path.join(DirectoryPath, file_name)

    shutil.copy(FilePath,fname)

    print("Back up file created : ",file_name)

    log = open("backup_log.txt","a")

    log.write("Backup completed successfully at ")
    log.write(str(datetime.datetime.now()))
    log.write("\n")

    log.close()



def main():
    Border = "-"*40
   
    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)
    
    if(len(sys.argv) == 2):
        
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to take Backup of file and put it in Directory")
            print("For better usage please check --u flag")
        
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the scipt as ")
            print("python FileName.py FileName DirectoryName")
            print("DirectoryName should be absolute path")
        
    elif(len(sys.argv)==3):
        schedule.every(1).hour.do(Backup,sys.argv[1],sys.argv[2])
            
        while True:
            schedule.run_pending()
            time.sleep(10)
                    
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

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