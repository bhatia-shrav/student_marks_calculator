# Student Marks Calculator
# A beginner-friendly Python project.

def get_valid_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid whole number.")


def main():
    print("=== Student Marks Calculator ===")

    subject_count = get_valid_number("Enter the number of subjects: ")
    marks = []

    for i in range(subject_count):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i + 1} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks)
    maximum = subject_count * 100
    percentage = (total / maximum) * 100

    print("\n=== Result ===")
    print(f"Total marks: {total:g} / {maximum}")
    print(f"Percentage: {percentage:.2f}%")


if __name__ == "__main__":
    main()
