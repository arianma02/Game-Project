import pandas as pd
import sqlite3

df = pd.read_csv("data/steam.csv")
df = df.drop_duplicates()

total_ratings = df["positive_ratings"] + df["negative_ratings"]

df["rating_percent"] = (df["positive_ratings"] / total_ratings.where(total_ratings != 0) * 100)

connection = sqlite3.connect("games.db")

df.to_sql("games",
          connection, 
          if_exists = "replace", 
          index = False
)

connection.close()


print("Database created.")
