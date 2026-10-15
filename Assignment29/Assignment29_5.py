import os
import sys

def CkhFileContent(file1_name, String_name):
      fobj1 = open(file1_name,"r")

      count = 0

      for line in fobj1:
            words = line.split()
            for word in words:
                 if word == String_name:
                  count = count + 1

      fobj1.close()

      return count

    
def main():
    
        
        if (os.path.exists(sys.argv[1])):
            print("File is Present in Current Directory")
            
            ret = CkhFileContent(sys.argv[1], sys.argv[2])

            print("Counts = ",ret)
            
        else:
              print("There are no such file")

if __name__ == "__main__":
    main()



