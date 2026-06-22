import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Data Cleaning
# Fill missing marks with average marks
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Remove duplicate rows
df = df.drop_duplicates()

# Filter students with marks above 75
high_scorers = df[df["Marks"] > 75]

print("\nStudents with Marks > 75:")
print(high_scorers)

# Group by Department
dept_stats = df.groupby("Department")["Marks"].agg(
    ["count", "mean", "max", "min"]
)

print("\nDepartment Statistics:")
print(dept_stats)

# Overall statistics
print("\nOverall Statistics:")
print(df["Marks"].describe())
