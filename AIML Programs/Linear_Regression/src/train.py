import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

df = pd.read_csv("dataset/student-mat.csv",sep=";")

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

X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train,y_train)

print("Model Intercept : ",model.intercept_)

print("\nLearned Coefficients:")

for feature, coefficient in zip(
    feature_columns,
    model.coef_
):
    print(feature, ":", coefficient)

prediction = model.predict(X_test)
print("\nFirst 10 Predictions:")
print("First 10 Prediction :",prediction[:10])
print("\nFirst 10 Actual Values:")

print(y_test.iloc[:10].values)

# =================================
# 8. MODEL EVALUATION
# =================================

mae = mean_absolute_error(y_test, prediction)

mse = mean_squared_error(y_test, prediction)

rmse = mse ** 0.5

r2 = r2_score(y_test, prediction)


print("\n========== MODEL EVALUATION ==========")

print("MAE:", mae)

print("MSE:", mse)

print("RMSE:", rmse)

print("R2 Score:", r2)