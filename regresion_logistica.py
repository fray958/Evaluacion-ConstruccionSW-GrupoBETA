
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("healthcare_dataset.csv")
df = df.dropna()

df["Target"] = (df["Test Results"] == "Abnormal").astype(int)

df_model = df[["Age", "Gender", "Billing Amount", "Room Number", "Admission Type"]]
df_model = pd.get_dummies(df_model)

X = df_model
y = df["Target"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

modelo_log = LogisticRegression(class_weight="balanced", max_iter=1000)
modelo_log.fit(X_train, y_train)

y_pred = modelo_log.predict(X_test)

print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall:    {recall_score(y_test, y_pred):.4f}")
