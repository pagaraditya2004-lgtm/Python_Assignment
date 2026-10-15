import pandas as pd

def main():
    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    dobj = pd.DataFrame(df)

    Average = dobj["StudyHours"].mean()
    print("Average of StudyHours column:", Average)

    Average = dobj["Attendance"].mean()
    print("Average of Attendance column:", Average)

    max_previous_score = dobj["PreviousScore"].max()
    print("Maximum of PreviousScore column:", max_previous_score)

    min_sleep_hours = dobj["SleepHours"].min()
    print("Minimum of SleepHours column:", min_sleep_hours)

if __name__ == "__main__":
    main()