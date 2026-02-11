# Q6 - Crime risk category + compare unemployment rates (crime.csv)

import pandas as pd

def main():
    df = pd.read_csv("crime.csv")
    df["risk"] = df["ViolentCrimesPerPop"].apply(lambda x: "HighCrime" if x >= 0.50 else "LowCrime")

    avg_unemp = df.groupby("risk")["PctUnemployed"].mean()

    for risk in ["HighCrime", "LowCrime"]:
        if risk in avg_unemp.index:
            print(f"{risk} average PctUnemployed: {avg_unemp.loc[risk]:.4f}")
        else:
            print(f"{risk} average PctUnemployed: N/A")

if __name__ == "__main__":
    main()