import pandas as pd
df=pd.read_csv("production.csv", sep=";", encoding="cp1251")

new1=[100, 200, 300]
new2=[110, 130, 240]
new3=[170, 250, 340]

df.loc[len(df)]=new1
df.loc[len(df)]=new2
df.loc[len(df)]=new3

df.to_csv("all.csv", sep=";", encoding="cp1251", index=False)