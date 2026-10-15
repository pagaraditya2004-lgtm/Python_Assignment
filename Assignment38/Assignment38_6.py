import pandas as pd
import matplotlib.pyplot as plt

def main():
    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    StudyHours = df["StudyHours"]
    

    plt.hist(
        StudyHours,
        bins = 5,
        color = "blue",
        edgecolor = "black",
        label = "Students"
        
    )

    plt.title("Histogram of StudyHours")
    plt.xlabel("StudyHours")
    plt.ylabel("Frequency")

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()