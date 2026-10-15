import pandas as pd
import matplotlib.pyplot as plt

def main():
    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    StudyHours = df["StudyHours"]
    PreviousScore = df["PreviousScore"]

    plt.scatter(
        StudyHours,
        PreviousScore,
        s = 100,
        marker="o",
        alpha=0.8,
        edgecolors="black",
        linewidths=1,
        label = "Students"
    )

    plt.title("studyHours vs previousScore")
    plt.xlabel("Studyhours")
    plt.ylabel("previousScore")
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    main()