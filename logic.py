import pandas as pd

# calculate_stats function
def calculate_stats(df):
    if df.empty or "Grade" not in df.columns or df["Grade"].dropna().empty:
        return {
            "average": 0,
            "highest": 0,
            "lowest": 0
        }

    return {
        "average": df["Grade"].mean(),
        "highest": df["Grade"].max(),
        "lowest": df["Grade"].min()
    }

# get_grade_distribution function
def get_grade_distribution(df):
    if df.empty or "Grade" not in df.columns or df["Grade"].dropna().empty:
        return pd.Series(dtype=int)

    return df["Grade"].value_counts().sort_index()