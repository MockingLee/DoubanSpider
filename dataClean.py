import pandas as pd
import numpy as np


def clean(file):
    data = pd.read_csv(file)
    print(data)
    data = data.dropna()
    data = data[data.rate != "date"]
    print(data["rate"].unique())
    data = data[~data["user_name"].str.contains("'")]
    data = data[~data["movie_name"].str.contains("'")]
    data.loc[data.rate == "很差", "rate"] = 1
    data.loc[data.rate == "较差", "rate"] = 2
    data.loc[data.rate == "还行", "rate"] = 3
    data.loc[data.rate == "推荐", "rate"] = 4
    data.loc[data.rate == "力荐", "rate"] = 5

    data.loc[data.rate == "rating1-t", "rate"] = 1
    data.loc[data.rate == "rating2-t", "rate"] = 2
    data.loc[data.rate == "rating3-t", "rate"] = 3
    data.loc[data.rate == "rating4-t", "rate"] = 4
    data.loc[data.rate == "rating5-t", "rate"] = 5
    print(data["rate"].unique())
    return data








