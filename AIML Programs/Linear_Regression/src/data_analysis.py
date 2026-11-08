import pandas as pd

# Load the real dataset
df = pd.read_csv(
    "dataset/student-mat.csv",
    sep=";"
)

# 1. Display first 10 records
print("\n========== FIRST 10 RECORDS ==========")
print(df.head(10))

# 2. Display dataset dimensions
print("\n========== DATASET SHAPE ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 3. Display column names
print("\n========== COLUMN NAMES ==========")
for column in df.columns:
    print(column)

# 4. Display data types
print("\n========== DATA TYPES ==========")
print(df.dtypes)

# 5. Display unique values in each column
print("\n========== UNIQUE VALUES ==========")
print(df.nunique())