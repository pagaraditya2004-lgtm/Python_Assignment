import os

def Display(file_name):
      fobj = open(file_name,"r")
      
      print(fobj.read())

      fobj.close()
    
def main():
        print("Enter file name :")
        Fname = input()
        
        if (os.path.exists(Fname)):
            print("File is Present in Current Directory")
            
            Display(Fname)
            
        else:
              print("There is no such file")

if __name__ == "__main__":
    main()



