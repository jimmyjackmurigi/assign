import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map({i:name for i, name in enumerate(iris.target_names)})
    print("✅ Dataset loaded successfully.")
except Exception as e:
    print(f"❌ Error loading dataset: {e}")

print("\n🔎 First 5 rows:")
print(df.head())

print("\n🧱 Data Types & Nulls:")
print(df.info())

print("\n❓ Missing Values:")
print(df.isnull().sum())

df = df.dropna()
print("\n🧹 Cleaned dataset (after dropping missing values):")
print(df.head())

print("\n📊 Basic Statistics:")
print(df.describe())

grouped = df.groupby('species').mean()
print("\n📈 Mean of numeric features per species:")
print(grouped)

print("\n🧠 Observations:")
print("1. Setosa has the smallest petal and sepal measurements.")
print("2. Virginica has the largest petal length and width.")
print("3. Clear distinction between species in terms of petal size.")

sns.set(style="whitegrid")

df['index'] = range(len(df))
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='index', y='sepal length (cm)', hue='species')
plt.title('Line Chart: Sepal Length over Samples')
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length (cm)')
plt.legend(title='Species')
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='species', y='petal length (cm)', estimator=np.mean)
plt.title('Bar Chart: Avg Petal Length per Species')
plt.ylabel('Petal Length (cm)')
plt.xlabel('Species')
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df['sepal width (cm)'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram: Sepal Width Distribution')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title('Scatter Plot: Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()

