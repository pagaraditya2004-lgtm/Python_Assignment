import pandas as pd

def main():
    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    print("First 5 rows of the DataFrame:")
    print(df.head())

    print("Last 5 rows of the DataFrame:")
    print(df.tail())

    print("Total No. of row and column in the DataFrame:")
    print(df.shape)

    print("List of all columns in the DataFrame:")
    print(list(df.columns))

    print("Data types of each column in the DataFrame:")
    print(df.dtypes)

if __name__ == "__main__":
    main()
