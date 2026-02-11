# Q4 - Filter high engagement students (student.csv)

import pandas as pd

def main():
    df = pd.read_csv("student.csv")

    filtered = df[(df["studytime"] >= 3) & (df["internet"] == 1) & (df["absences"] <= 5)]
    filtered.to_csv("high_engagement.csv", index=False)

    print(f"Saved students: {len(filtered)}")
    if len(filtered) > 0:
        print(f"Average grade: {filtered['grade'].mean():.3f}")
    else:
        print("Average grade: N/A")

if __name__ == "__main__":
    main()