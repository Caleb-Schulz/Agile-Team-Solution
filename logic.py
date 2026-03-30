import pandas as pd

# calculate_stats function
def calculate_stats(df):
    if df.empty or "grade" not in df.columns or df["grade"].dropna().empty:
        return {
            "average": 0,
            "highest": 0,
            "lowest": 0
        }

    return {
        "average": df["grade"].mean(),
        "highest": df["grade"].max(),
        "lowest": df["grade"].min()
    }

# get_grade_distribution function
def get_grade_distribution(df):
    if df.empty or "grade" not in df.columns or df["grade"].dropna().empty:
        return pd.Series(dtype=int)

    return df["grade"].value_counts().sort_index()