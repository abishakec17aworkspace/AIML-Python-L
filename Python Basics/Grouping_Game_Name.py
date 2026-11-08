import pandas  as pd

df = pd.read_csv("newsetGameData.csv")

# print(df.describe())

# print(df.to_string())

# grouping the elements
game_group =df.groupby("game_name").count()
print(game_group.to_string)

# to find maximun downloaded data
maxdata = game_group["order_id"].idxmax()
max_download = game_group["order_id"].max()
print("-------------------------------")
print("max_Data :",maxdata)
print("max_Download :",max_download)
print("-------------------------------")

min_data_Name = game_group["order_id"].idxmin()
mindata = game_group["order_id"].min()
min_download = game_group[
    game_group["order_id"] == mindata
    ]
print("-------------------------------")
print("min_Data :",min_data_Name)
print(min_download.index.tolist())
print("-------------------------------")


min_paid_Name = game_group["revenue_usd"].idxmin()
mindata = game_group["revenue_usd"].min()
min_paid= game_group[
    game_group["revenue_usd"] == mindata
    ]
print("-------------------------------")
print("min_paid :",min_paid_Name)
print(min_paid.index.tolist())
print("-------------------------------")


max_paid_Name = game_group["revenue_usd"].idxmax()
maxdata = game_group["revenue_usd"].max()
max_paid= game_group[
    game_group["revenue_usd"] == maxdata
    ]
print("-------------------------------")
print("max_paid :",min_paid_Name)
print(max_paid.index.tolist())
print("-------------------------------")


# converting the Revenue_usd to proper data
df["revenue_usd"] = df["revenue_usd"].astype(str).str.replace("$","",regex=False).str.replace(",","",regex=False)
df["revenue_usd"] = pd.to_numeric(
    df["revenue_usd"],
    errors="coerce"
)
total_revenue = df["revenue_usd"].sum()
print("total :",total_revenue)


# new_nome = df[df["revenue_usd"].isna()]
# # print(new_nome)

print("data_before:",len(df["revenue_usd"]))
df = df.dropna(subset=["revenue_usd"])
print("data_after:",len(df["revenue_usd"]))

game_group.to_csv("Game_name_group.csv")
df.to_csv("cleaned_Data_50percent.csv",index=False)

df