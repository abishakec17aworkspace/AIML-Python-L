import pandas  as pd

df = pd.read_csv("newsetGameData.csv")

# print(df.describe())

game_groups = df.groupby("game_name")
df

# for datacount,indexes in data.items():
#     print("data :",datacount,"indexes :",len(indexes))

# df["gamename"]= df["game_name"]
# df["totalcount"]=df.groupby("gamename")["game_name"].transform("count")

# print(df[["gamename","totalcount"]])
# # df["newColumn"]=data
# # print(df["newColumn"])
# print(data)