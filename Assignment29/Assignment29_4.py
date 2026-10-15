import os
import sys

def CkhFileContent(file1_name, file2_name):
      fobj1 = open(file1_name,"r")
      f1read = fobj1.read()

      fobj1.close()

      fobj2 = open(file2_name,"r")
      f2read = fobj2.read()

      fobj2.close()

      if f1read == f2read :
            return True
      else:
            return False
      

    
def main():
    
        
        if (os.path.exists(sys.argv[1])):
            print("File is Present in Current Directory")
            
            ret = CkhFileContent(sys.argv[1], sys.argv[2])

            if ret :
                  print("Success")
            else:
                  print("Failed")
            
        else:
              print("There are no such file")

if __name__ == "__main__":
    main()



