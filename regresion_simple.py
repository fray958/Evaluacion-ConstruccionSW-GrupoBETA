
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("Housing.csv")

correlaciones = df.corr(numeric_only=True)["price"].drop("price").abs()
mejor_variable = correlaciones.idxmax()
print(f"Variable seleccionada: {mejor_variable}")

X_simple = df[[mejor_variable]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X_simple, y, test_size=0.2, random_state=42)

modelo_simple = LinearRegression()
modelo_simple.fit(X_train, y_train)

y_pred_simple = modelo_simple.predict(X_test)
mse_simple = mean_squared_error(y_test, y_pred_simple)
r2_simple = r2_score(y_test, y_pred_simple)

print(f"MSE: {mse_simple:.2e}")
print(f"R2:  {r2_simple:.4f}")
