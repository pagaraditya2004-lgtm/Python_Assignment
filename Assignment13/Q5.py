def get_grade(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    else:
        return "Fail"


def main():
    marks = float(input("Enter marks: "))

    if 0 <= marks <= 100:
        print("Grade:", get_grade(marks))
    else:
        print("Invalid marks! Enter marks between 0 and 100.")


if __name__ == "__main__":
    main()