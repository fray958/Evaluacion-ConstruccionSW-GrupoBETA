
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("Housing.csv")

X_poly = df[["area"]]
y = df["price"]

poly = PolynomialFeatures(degree=2)
X_poly_transformed = poly.fit_transform(X_poly)

X_train, X_test, y_train, y_test = train_test_split(X_poly_transformed, y, test_size=0.2, random_state=42)

modelo_poly = LinearRegression()
modelo_poly.fit(X_train, y_train)

y_pred_poly = modelo_poly.predict(X_test)
mse_poly = mean_squared_error(y_test, y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)

print(f"MSE: {mse_poly:.2e}")
print(f"R2:  {r2_poly:.4f}")
