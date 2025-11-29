import pandas as pd
months=("March", "April", "May", "June")

values=[]

for m in months:
    x=input("Введіть кількість плит за місяць:" + m + ": ")
    values.append(int(x))

s=pd.Series(values, index=months)
s.to_json("beton.json")

