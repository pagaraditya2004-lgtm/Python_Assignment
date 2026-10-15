import pandas as pd

def main():
    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    result_counts = df["FinalResult"].value_counts()
    print("Value counts of FinalResult column:")
    print(result_counts)

    pass_percentage = (df["FinalResult"]== 1).sum() / len(df) * 100
    print("Percentage of students who passed the exam:", pass_percentage)

    fail_percentage = (df["FinalResult"]== 0).sum() / len(df) * 100
    print("Percentage of students who failed the exam:", fail_percentage)

if __name__ == "__main__":
    main()