import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())
print("\nSummary Statistics:")
print(df.describe())
print("\nColumn Names:")
print(df.columns)
print("\nSales Visualization:")
print("\nSales Visualization:")

df.plot(kind="bar")

plt.title("Sales Data Analysis")
plt.xlabel("Index")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
