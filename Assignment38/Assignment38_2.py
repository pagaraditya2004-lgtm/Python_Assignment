import pandas as pd

def main():
    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    print("Total no. of students in the DataFrame:", len(df))

    dobj = pd.DataFrame(df)

    count = 0
    for i in range(len(dobj)):
        if(dobj["FinalResult"][i] == 1):
            count += 1

    print("Total no. of students who passed the exam:", count)

    count = 0
    for i in range(len(dobj)):
        if(dobj["FinalResult"][i] == 0):
            count += 1
    
    print("Total no. of students who failed the exam:", count)



if __name__ == "__main__":  
    main()