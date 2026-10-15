import pandas as pd
import matplotlib.pyplot as plt

def main():
    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    pass_percentage = df.groupby("SleepHours")["FinalResult"].mean()*100
    
    plt.bar(
        pass_percentage.index,                   # Values of X axis
        pass_percentage.values,                   # values of y axis
        width=0.6,                  # width of bars
        edgecolor = "black",        # border color of bars
        linewidth = 1,              # width of bar border
        alpha = 0.8,                # transparence 0.0 to 1.0
        label = "Pass_Percentage"          # legend text

    )

    plt.title("Scattered Plot")
    plt.xlabel("SleepHours")
    plt.ylabel("Pass Percentage")
    plt.grid(True)

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()