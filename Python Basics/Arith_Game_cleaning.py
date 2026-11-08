import pandas as pd

df = pd.read_csv("cleaned_Data_50percent.csv")

max_saled_unit = df["units_sold"].max()
print(max_saled_unit)

min_saled_unit = df["units_sold"].min()
print(min_saled_unit)


# df["discount_percent"] =pd.to_numeric(df["discount_percent"])


# df = df.info()
selected_col=print(df[["units_sold","discount_percent","revenue_usd"]])
df["discount_percent"]=df["discount_percent"].astype(str).str.strip().str.replace("%","",regex=False)

df["discount_percent"] = pd.to_numeric(
    df["discount_percent"],
    errors="coerce"
)

print("total discount percentage :",df["discount_percent"].sum())
print("total unit_sold :",df["units_sold"].sum())
print("total revenue_usd :",df["revenue_usd"].sum())

# negative_values= df[df["units_sold"]<0]
# print(negative_values)

df =df[df["units_sold"]>0]
print("min_ value :" ,df["units_sold"].min())

selected_col