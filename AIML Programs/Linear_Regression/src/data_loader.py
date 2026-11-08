
import pandas as pd

# =====================================
# 1. LOAD DATASET
# =====================================

df = pd.read_csv("dataset/student-mat.csv",sep=";")


# =====================================
# 2. DATASET INSPECTION
# =====================================

dataframe_head = df.head()

data_info = df.info()

data_shape = df.shape

data_stat = df.describe()

missing_value = df.isnull().sum()

duplicate_values = df.duplicated().sum()


# =====================================
# 3. DISPLAY RESULTS
# =====================================

print("\n========== DATASET HEAD ==========")
print(dataframe_head)

print("\n========== DATASET INFORMATION ==========")
df.info()

print("\n========== DATASET SHAPE ==========")
print(data_shape)

print("\n========== STATISTICAL SUMMARY ==========")
print(data_stat)

print("\n========== MISSING VALUES ==========")
print(missing_value)

print("\n========== DUPLICATE RECORDS ==========")
print(duplicate_values)
