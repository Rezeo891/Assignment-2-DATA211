# Q5 - Create grade bands + grouped summary (student.csv)

import pandas as pd

def band(g: float) -> str:
    if g <= 9:
        return "Low"
    elif 10 <= g <= 14:
        return "Medium"
    else:
        return "High"

def main():
    df = pd.read_csv("student.csv")
    df["grade_band"] = df["grade"].apply(band)

    summary = (
        df.groupby("grade_band")
          .agg(
              num_students=("grade_band", "size"),
              avg_absences=("absences", "mean"),
              pct_internet=("internet", lambda s: 100 * s.mean())
          )
          .reset_index()
    )

    summary.to_csv("student_bands.csv", index=False)
    print(summary.to_string(index=False))

if __name__ == "__main__":
    main()