
import pandas as pd
df= pd.read_csv("movies.csv")
print("\n ---ilk 5 satır---")
print(df.head())

print("\n---bilgi---")
print(df.info())

print("\n---istatistikler---")
print(df.describe())

print("\n---ortalama puan---")
ortalama = df["rating"].mean()
print(ortalama)

print("\n---8.0 ve üzeri filmler---")
high_rated = df[df["rating"]>=8.0]
[["title","rating"]]
print(high_rated)

print("\n---Türlere göre ortalama puan---")
genre_avg = df.groupby("genre")["rating"].mean()
print(genrre_avg)

print("\n---en yüksek puanlı film---")
best = df.loc[df["rating"].idxmax(),["title","rating"]]
print(best)

print("\n---yıllara göre ortalama puan---")
year_avg=df.groupby("year")["rating"].mean()

print(year_avg)
