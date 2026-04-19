
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("Housing.csv")

X_multiple = df[["area", "bathrooms", "stories"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X_multiple, y, test_size=0.2, random_state=42)

modelo_multiple = LinearRegression()
modelo_multiple.fit(X_train, y_train)

y_pred_multiple = modelo_multiple.predict(X_test)
mse_multiple = mean_squared_error(y_test, y_pred_multiple)
r2_multiple = r2_score(y_test, y_pred_multiple)

print(f"MSE: {mse_multiple:.2e}")
print(f"R2:  {r2_multiple:.4f}")
for var, coef in zip(["area","bathrooms","stories"], modelo_multiple.coef_):
    print(f"  {var}: {coef:.2f}")
