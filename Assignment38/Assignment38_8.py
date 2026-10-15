import pandas as pd
import matplotlib.pyplot as plt

def main():
    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    Attendance = df["Attendance"]

    plt.boxplot(
        Attendance
    )

    plt.title("Attendance Box Plot")
    plt.xlabel("Previous Score")
    plt.show()

if __name__ == "__main__":
    main()