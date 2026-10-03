import pandas as pd
import csv
df =  pd.read_csv("gaming_sales_100_rows.csv")
# print(df[["Game","Genre","Gender"]])
# column_title = df.columns.tolist()
# for i in column_title:
#     print(i)

# print(df.info())    
# print(df.describe())
# high_value = df[df["Revenue_USD"]>500]
# print(high_value)

df["Result"] = df["Revenue_USD"].apply(
    lambda revenue: "Pass" if revenue>500 else "Fail"
)

df["Ratings"]=df["Result"].apply(
    lambda rate: 100 if rate.lower() == "pass" else 50
)

# print(df[["Game","Genre","Year","Revenue_USD","Result","Ratings"]])

table_100 = df[(df["Ratings"]==100) & (df["Year"]==2024)] 
table_50 = df[df["Ratings"]==50]

print("-------------------------------")
print(table_100)
print("-------------------------------")
# print()
# print(table_50)

