import pandas as pd
from sklearn.model_selection import train_test_split

df =pd.read_csv("dataset/student-mat.csv",sep=";")

feature_columns = [
    "G1",
    "G2",
    "studytime",
    "absences",
    "failures",
    "age"
]

X = df[feature_columns]
Y = df["G3"]

X_train,X_test,y_train,y_test = train_test_split(
    X,Y,test_size=0.2,random_state=42
)

# Display results
print("Training Features:", X_train.shape)
print("Testing Features:", X_test.shape)

print("Training Target:", y_train.shape)
print("Testing Target:", y_test.shape)

print("Total Training Records:", len(X_train))
print("Total Testing Records:", len(X_test))