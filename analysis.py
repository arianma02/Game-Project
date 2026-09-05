import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/steam.csv")

total_ratings = df["positive_ratings"] + df["negative_ratings"]

df["rating_percent"] = (
    df["positive_ratings"] / total_ratings.where(total_ratings != 0) * 100
)

df["release_year"] = pd.to_datetime(df["release_date"]).dt.year

games_per_year = df.groupby("release_year").size()

games_per_year.plot()

plt.title("Steam Games Released by Year")
plt.xlabel("Year")
plt.ylabel("Number of Games")
plt.show()