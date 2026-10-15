import os

def CopyFile(file1_name, file2_name):
      fobj1 = open(file1_name,"r")
      fread = fobj1.read()

      fobj1.close()

      fobj2 = open(file2_name,"w")
      fobj2.write(fread)

    
def main():
        print("Enter file name to read :")
        F1name = input()

        print("Enter file name to copy in :")
        F2name = input()
        
        if (os.path.exists(F1name)):
            print("File is Present in Current Directory")
            
            CopyFile(F1name, F2name)
            
        else:
              print("There are no such file")

if __name__ == "__main__":
    main()



