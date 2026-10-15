import os
import sys

def CopyFile(file1_name, file2_name):
      fobj1 = open(file1_name,"r")
      fread = fobj1.read()

      fobj1.close()

      fobj2 = open(file2_name,"w")
      fobj2.write(fread)

      fobj2.close()

    
def main():
    
        
        if (os.path.exists(sys.argv[1])):
            print("File is Present in Current Directory")
            
            CopyFile(sys.argv[1], sys.argv[2])
            
        else:
              print("There are no such file")

if __name__ == "__main__":
    main()



