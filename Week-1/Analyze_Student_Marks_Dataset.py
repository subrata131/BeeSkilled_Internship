import pandas as pd
import numpy as np

df = pd.read_csv("StudentsPerformance.csv")

print(df.head())

print("Shape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("Missing Values:")
print(df.isnull().sum())


numeric_columns = df.select_dtypes(include=np.number).columns

df[numeric_columns] = df[numeric_columns].fillna(
    df[numeric_columns].mean()
)


categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

print("Missing Values After Cleaning:")
print(df.isnull().sum())


print("Average Math Score:", df["math score"].mean())
print("Average Reading Score:", df["reading score"].mean())
print("Average Writing Score:", df["writing score"].mean())

print("Maximum Math Score:", df["math score"].max())
print("Maximum Reading Score:", df["reading score"].max())
print("Maximum Writing Score:", df["writing score"].max())

print("Minimum Math Score:", df["math score"].min())
print("Minimum Reading Score:", df["reading score"].min())
print("Minimum Writing Score:", df["writing score"].min())

score_columns = [
    "math score",
    "reading score",
    "writing score"
]

print("Mean:")
print(df[score_columns].mean())

print("\nMedian:")
print(df[score_columns].median())

print("\nMode:")
print(df[score_columns].mode().iloc[0])

print("===== STUDENT MARKS ANALYSIS =====")

print("\nAverage Scores:")
print(df[score_columns].mean())

print("\nMaximum Scores:")
print(df[score_columns].max())

print("\nMinimum Scores:")
print(df[score_columns].min())

print("\nMedian Scores:")
print(df[score_columns].median())

print("\nMode Scores:")
print(df[score_columns].mode().iloc[0])
