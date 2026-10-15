###########################################################
#
#   File Name    : DuplicateFileRemoval.py
#   Description  : Remove Duplicate Files using MD5 Checksum
#   Author       : Aditya Pagar
#
###########################################################

import sys
import os
import hashlib
import schedule
import time
import datetime
import smtplib
from email.message import EmailMessage


###########################################################
#
#   Display Help
#
###########################################################

def DisplayHelp():

    print("---------------------------------------------------------")
    print("           Marvellous Duplicate File Remover")
    print("---------------------------------------------------------")
    print("This automation script removes duplicate files")
    print("from the specified directory using MD5 checksum.")
    print("")
    print("Usage :")
    print("python DuplicateFileRemoval.py Directory TimeInterval Email")
    print("")
    print("Example :")
    print("python DuplicateFileRemoval.py D:\\Demo 10 abc@gmail.com")
    print("---------------------------------------------------------")


###########################################################
#
#   Display Usage
#
###########################################################

def DisplayUsage():

    print("---------------------------------------------------------")
    print("Usage :")
    print("python DuplicateFileRemoval.py Directory TimeInterval Email")
    print("")
    print("Arguments :")
    print("Directory     : Absolute path of directory")
    print("TimeInterval  : Time in minutes")
    print("Email         : Receiver Email ID")
    print("---------------------------------------------------------")


###########################################################
#
#   Calculate MD5 Checksum
#
###########################################################

def CalculateChecksum(FileName):

    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):

        hobj.update(Buffer)

        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()


###########################################################
#
#   Find Duplicate Files
#
###########################################################

def FindDuplicate(DirectoryName):

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("ERROR : Invalid Path")
        return None

    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("ERROR : Path is not Directory")
        return None

    Duplicate = {}

    TotalFiles = 0

    print("Scanning Directory...")

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):

        for fname in FileName:

            fname = os.path.join(FolderName, fname)

            CheckSum = CalculateChecksum(fname)

            TotalFiles = TotalFiles + 1

            if(CheckSum in Duplicate):
                Duplicate[CheckSum].append(fname)

            else:
                Duplicate[CheckSum] = [fname]

    print("Total Files Scanned :", TotalFiles)

    return Duplicate


###########################################################
#
#   Validate Input
#
###########################################################

def ValidateInput():

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--help" or sys.argv[1] == "--h"):
            DisplayHelp()
            return False

        elif(sys.argv[1] == "--usage" or sys.argv[1] == "--u"):
            DisplayUsage()
            return False

    if(len(sys.argv) != 4):

        DisplayUsage()
        return False

    DirectoryName = sys.argv[1]

    if(os.path.exists(DirectoryName) == False):
        print("ERROR : Directory does not exist")
        return False

    if(os.path.isdir(DirectoryName) == False):
        print("ERROR : Invalid Directory")
        return False

    return True
###########################################################
#
#   Send Email with Log File Attachment
#
###########################################################
###########################################################
#
#   Create Log Directory
#
###########################################################

def CreateLogDirectory():

    DirectoryName = "Marvellous"

    if(os.path.exists(DirectoryName) == False):
        os.mkdir(DirectoryName)

    return DirectoryName


###########################################################
#
#   Create Log File
#
###########################################################

def CreateLogFile(LogData):

    DirectoryName = CreateLogDirectory()

    TimeStamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    FileName = os.path.join(DirectoryName,
                            "MarvellousLog_" + TimeStamp + ".log")

    fobj = open(FileName,"w")

    fobj.write("=====================================================\n")
    fobj.write("          Marvellous Infosystems Pvt. Ltd.\n")
    fobj.write("=====================================================\n\n")

    fobj.write(LogData)

    fobj.write("\n=====================================================\n")

    fobj.close()

    return FileName


###########################################################
#
#   Delete Duplicate Files
#
###########################################################

def DeleteDuplicate(DirectoryName):

    Duplicate = FindDuplicate(DirectoryName)

    if(Duplicate == None):
        return None,None

    Result = list(filter(lambda x : len(x) > 1 , Duplicate.values()))

    TotalDuplicate = 0
    TotalDeleted = 0

    LogData = ""

    LogData += "Execution Time : "
    LogData += str(datetime.datetime.now())
    LogData += "\n\n"

    LogData += "Directory : "
    LogData += DirectoryName
    LogData += "\n\n"

    LogData += "Duplicate Files\n"
    LogData += "-----------------------------\n\n"

    Count = 0

    for value in Result:

        TotalDuplicate = TotalDuplicate + (len(value)-1)

        for FileName in value:

            Count = Count + 1

            if(Count > 1):

                os.remove(FileName)

                TotalDeleted = TotalDeleted + 1

                LogData += "Deleted : "
                LogData += FileName
                LogData += "\n"

        Count = 0

    LogData += "\n-----------------------------\n"
    LogData += "Total Duplicate Files : "
    LogData += str(TotalDuplicate)
    LogData += "\n"

    LogData += "Total Deleted Files : "
    LogData += str(TotalDeleted)
    LogData += "\n"

    LogFileName = CreateLogFile(LogData)

    print("------------------------------------------")
    print("Duplicate Files :",TotalDuplicate)
    print("Deleted Files   :",TotalDeleted)
    print("Log File Created")
    print("------------------------------------------")

    return LogFileName,TotalDeleted


###########################################################
#
#   Process Directory
#
###########################################################

def ProcessDirectory():

    DirectoryName = sys.argv[1]

    LogFileName,DeletedFiles = DeleteDuplicate(DirectoryName)

    return LogFileName,DeletedFiles
def SendMail(LogFileName):

    SenderEmail = "YourEmail@gmail.com"
    SenderPassword = "YourAppPassword"

    ReceiverEmail = sys.argv[3]

    msg = EmailMessage()

    msg["Subject"] = "Duplicate File Removal Report"

    msg["From"] = SenderEmail

    msg["To"] = ReceiverEmail

    Body = ""
    Body += "Hello,\n\n"
    Body += "Duplicate File Removal Process Completed Successfully.\n\n"
    Body += "Please find the attached Log File.\n\n"
    Body += "Regards,\n"
    Body += "Marvellous Automation"

    msg.set_content(Body)

    fobj = open(LogFileName,"rb")

    FileData = fobj.read()

    fobj.close()

    FileName = os.path.basename(LogFileName)

    msg.add_attachment(FileData,
                       maintype="application",
                       subtype="octet-stream",
                       filename=FileName)

    Server = smtplib.SMTP("smtp.gmail.com",587)

    Server.starttls()

    Server.login(SenderEmail,SenderPassword)

    Server.send_message(msg)

    Server.quit()

    print("-----------------------------------------")
    print("Email Sent Successfully")
    print("-----------------------------------------")


###########################################################
#
#   Scheduler Function
#
###########################################################

def ScheduleProcess():

    print("-----------------------------------------")
    print("Duplicate File Removal Started")
    print("-----------------------------------------")

    LogFileName,DeletedFiles = ProcessDirectory()

    if(LogFileName != None):
        SendMail(LogFileName)


###########################################################
#
#   Start Scheduler
#
###########################################################

def StartScheduler():

    TimeInterval = int(sys.argv[2])

    ScheduleProcess()

    schedule.every(TimeInterval).minutes.do(ScheduleProcess)

    print("-----------------------------------------")
    print("Scheduler Started")
    print("Running every",TimeInterval,"minutes")
    print("-----------------------------------------")

    while(True):

        schedule.run_pending()

        time.sleep(1)
###########################################################
#
#   Main Function
#
###########################################################

def main():

    Border = "-" * 60

    print(Border)
    print("        Marvellous Duplicate File Remover")
    print(Border)

    Ret = ValidateInput()

    if(Ret == False):
        return

    DirectoryName = sys.argv[1]

    TimeInterval = sys.argv[2]

    EmailID = sys.argv[3]

    print("Directory      :",DirectoryName)
    print("Time Interval  :",TimeInterval,"Minutes")
    print("Receiver Email :",EmailID)

    print(Border)

    StartScheduler()


###########################################################
#
#   Starter
#
###########################################################

if __name__ == "__main__":
    main()