import os

def FindWord(file_name,File_word):
      fobj = open(file_name,"r")

      fread = fobj.read()

      for word in fread:
            if word == File_word:
                  return True
            else:
                  return False
                  
      fobj.close()
    
def main():
        print("Enter file name :")
        Fname = input()
        print("Enter Word to ckh whether it is present in file or not : ")
        Fword = input()
        
        if (os.path.exists(Fname)):
            print("File is Present in Current Directory")
            
            ret = FindWord(Fname,Fword)
            if True:
                  print(f"{Fword} is Present")
            else:
                  print(f"{Fword} is Not Present")
                  
            
        else:
              print("There is no such file")

if __name__ == "__main__":
    main()



