
import pandas as pd

# =====================================
# 1. LOAD DATASET
# =====================================

df = pd.read_csv(
    "dataset/student-mat.csv",
    sep=";"
)


# =====================================
# 2. SELECT INPUT FEATURES
# =====================================

feature_columns = [
    "G1",
    "G2",
    "studytime",
    "absences",
    "failures",
    "age"
]

X = df[feature_columns]


# =====================================
# 3. SELECT TARGET VARIABLE
# =====================================

y = df["G3"]


# =====================================
# 4. INSPECT FEATURE DATA
# =====================================

print("\n========== INPUT FEATURES (X) ==========")

print(X.head())

print("\nFeature Shape:")
print(X.shape)


# =====================================
# 5. INSPECT TARGET DATA
# =====================================

print("\n========== TARGET VARIABLE (y) ==========")

print(y.head())

print("\nTarget Shape:")
print(y.shape)


# =====================================
# 6. CHECK FEATURE-TARGET CORRELATION
# =====================================

print("\n========== FEATURE CORRELATION WITH G3 ==========")

correlation = df[feature_columns + ["G3"]].corr()

print(
    correlation["G3"]
    .sort_values(ascending=False)
)


# =====================================
# 7. VERIFY DATA
# =====================================

print("\n========== DATA VALIDATION ==========")

print("Input rows:", len(X))
print("Target rows:", len(y))

print("Missing values in X:", X.isnull().sum().sum())
print("Missing values in y:", y.isnull().sum())
