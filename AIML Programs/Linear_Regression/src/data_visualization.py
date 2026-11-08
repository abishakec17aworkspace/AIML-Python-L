
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(
    "dataset/student-mat.csv",
    sep=";"
)

sns.set_theme(style="whitegrid")


# ==================================
# 1. GRADE DISTRIBUTION
# ==================================

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="G3",
    bins=15,
    kde=True
)

plt.title("Distribution of Final Grades")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")

plt.show()


# ==================================
# 2. FIRST PERIOD vs FINAL GRADE
# ==================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="G1",
    y="G3"
)

plt.title("First Period Grade vs Final Grade")
plt.xlabel("G1")
plt.ylabel("G3")

plt.show()


# ==================================
# 3. SECOND PERIOD vs FINAL GRADE
# ==================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="G2",
    y="G3"
)

plt.title("Second Period Grade vs Final Grade")
plt.xlabel("G2")
plt.ylabel("G3")

plt.show()


# ==================================
# 4. STUDY TIME vs FINAL GRADE
# ==================================

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="studytime",
    y="G3"
)

plt.title("Study Time vs Final Grade")
plt.xlabel("Weekly Study Time Category")
plt.ylabel("Final Grade")

plt.show()


# ==================================
# 5. ABSENCES vs FINAL GRADE
# ==================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="absences",
    y="G3"
)

plt.title("School Absences vs Final Grade")
plt.xlabel("Absences")
plt.ylabel("Final Grade")

plt.show()


# ==================================
# 6. CORRELATION HEATMAP
# ==================================

numerical_columns = [
    "age",
    "Medu",
    "Fedu",
    "traveltime",
    "studytime",
    "failures",
    "absences",
    "G1",
    "G2",
    "G3"
]

correlation = df[numerical_columns].corr()

plt.figure(figsize=(11, 8))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Student Performance Correlation Heatmap")

plt.show()
