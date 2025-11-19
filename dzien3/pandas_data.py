import pandas as pd

df = pd.read_table('dane/users.txt',sep=',',encoding='utf-8')
print(df)
print("_"*70)
over_40 = df[df["Age"]>40]
print(over_40)

print("_"*70)
print(df.sort_values(by="Age",ascending=True))

print("_"*70)

df["AgePlus10"] = df["Age"]+10
print(df)

df.to_csv("dane/users_plus_10.csv",index=False)
df.to_excel("dane/users_plus_10.xlsx",index=False)
df.to_json("dane/users_plus_10.json",orient="records")
df.to_html("dane/users_plus_10.html",index=False)
