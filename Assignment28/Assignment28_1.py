import os

def CountLines(file_name):
      fobj = open(file_name,"r")

      count = 0

      for line in fobj:
            count = count+1
     
      fobj.close()
    
      return count  

def main():
        print("Enter file name :")
        Fname = input()
        
        if (os.path.exists(Fname)):
            print("File is Present in Current Directory")
            
            ret = CountLines(Fname)

            print("Total no. of lines in file : ",ret)
            
        else:
              print("There is no such file")

if __name__ == "__main__":
    main()



