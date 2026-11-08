import pandas as pd
df = pd.read_csv("gaming_data_messy_analytics.csv")

print(df.info())
print(df.describe())
print("------------------------------")
print(df.isnull().sum())
print("------------------------------")
duplicate_data = df[df.duplicated()]
print(duplicate_data)
df = df.drop_duplicates()
print(df.duplicated().sum())

df.columns = df.columns.str.strip().str.lower()
text_column = df.select_dtypes(include="str").columns
print(text_column)

Sample_data = df.select_dtypes(include="object").columns
for col in Sample_data:
    df[col] = df[col].str.strip()

# print(df.columns)
print("Row length before :",len(df))
df = df.drop_duplicates(subset="order_id", keep="first")
print("Row length after :",len(df))

print(df[df["game_name"].isna()])
df = df.dropna(subset="game_name")

# game_groups = df.groupby("game_name")
# print(game_groups)



# df["Game_Name"]=df["Game_Name"].replace("",pd.NA)
# print(df["Game_Name"])
# converting the Revenue_usd to proper data
df["revenue_usd"] = df["revenue_usd"].astype(str).str.replace("$","",regex=False).str.replace(",","",regex=False)
df["revenue_usd"] = pd.to_numeric(
    df["revenue_usd"],
    errors="coerce"
)

df.to_csv("newsetGameData.csv",index=False)



