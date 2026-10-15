import os

def CountWords(file_name):
      fobj = open(file_name,"r")
      
      count = 0

      for line in fobj:
            words = line.split()
            count = count + len(words)

      fobj.close()
            
      return count
    
def main():
        print("Enter file name :")
        Fname = input()
        
        if (os.path.exists(Fname)):
            print("File is Present in Current Directory")
            
            ret = CountWords(Fname)

            print("Total no. of words in file : ",ret)
            
        else:
              print("There is no such file")

if __name__ == "__main__":
    main()



