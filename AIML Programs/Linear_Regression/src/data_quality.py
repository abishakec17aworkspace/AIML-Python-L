
import pandas as pd

# Load dataset
df = pd.read_csv(
    "dataset/student-mat.csv",
    sep=";"
)

# =================================
# 1. MISSING VALUE ANALYSIS
# =================================

print("\n========== MISSING VALUES ==========")

missing_values = df.isnull().sum()

print(missing_values)

print("\nTotal Missing Values:")
print(missing_values.sum())


# =================================
# 2. DUPLICATE ANALYSIS
# =================================

print("\n========== DUPLICATE ANALYSIS ==========")

duplicate_count = df.duplicated().sum()

print("Duplicate Records:", duplicate_count)


# =================================
# 3. DATA TYPE ANALYSIS
# =================================

print("\n========== DATA TYPES ==========")

print(df.dtypes)


# =================================
# 4. CATEGORICAL VALUE ANALYSIS
# =================================

print("\n========== CATEGORICAL VALUES ==========")

categorical_columns = df.select_dtypes(
    include=["str"]
).columns

for column in categorical_columns:

    print(f"\nColumn: {column}")

    print(df[column].value_counts())


# =================================
# 5. NUMERICAL VALUE ANALYSIS
# =================================

print("\n========== NUMERICAL SUMMARY ==========")

print(df.describe())


# =================================
# 6. GRADE VALIDATION
# =================================

print("\n========== GRADE VALIDATION ==========")

grade_columns = ["G1", "G2", "G3"]

for column in grade_columns:

    invalid_grades = df[
        (df[column] < 0) |
        (df[column] > 20)
    ]

    print(
        f"{column} - Invalid Records:",
        len(invalid_grades)
    )


# =================================
# 7. ABSENCE VALIDATION
# =================================

print("\n========== ABSENCE VALIDATION ==========")

invalid_absences = df[df["absences"] < 0]

print("Invalid Absence Records:", len(invalid_absences))
