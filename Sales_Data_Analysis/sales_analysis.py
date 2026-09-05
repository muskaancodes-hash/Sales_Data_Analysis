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
# Part 5: Sales Summary

print("\nSales Summary:")

print("Total Sales:", df.select_dtypes(include="number").sum().sum())

print("\nAverage Values:")
print(df.select_dtypes(include="number").mean())
print("Total Sales:", df.select_dtypes(include="number").sum().sum())
# Part 6: Product-wise Sales Analysis

print("\nProduct-wise Sales:")

sales_by_product = df.groupby("Product")["Sales"].sum()

print(sales_by_product)

sales_by_product.plot(kind="bar")

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
# Part 7: Category-wise Sales Analysis

print("\nCategory-wise Sales:")

sales_by_category = df.groupby("Category")["Sales"].sum()

print(sales_by_category)

sales_by_category.plot(kind="bar")

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
# Part 8: Sales Insights

print("\nSales Insights:")

best_product = sales_by_product.idxmax()
best_product_sales = sales_by_product.max()

best_category = sales_by_category.idxmax()
best_category_sales = sales_by_category.max()

print("Best Selling Product:", best_product)
print("Best Product Sales:", best_product_sales)

print("Best Selling Category:", best_category)
print("Best Category Sales:", best_category_sales)