import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

print("\n===== ORIGINAL DATA =====")
print(df)

# Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Cleaning data
df = df.drop_duplicates()

# Summary statistics
print("\n===== SUMMARY STATISTICS =====")
print(df.describe())

# Filter students with marks > 80
high_scorers = df[df["Marks"] > 80]

print("\n===== STUDENTS WITH MARKS > 80 =====")
print(high_scorers)

# Group by department
department_avg = df.groupby("Department")["Marks"].mean()

print("\n===== AVERAGE MARKS BY DEPARTMENT =====")
print(department_avg)

# Generate graph
department_avg.plot(kind="bar")

plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")

plt.savefig("graphs/average_marks.png")

print("\n✅ Graph saved in graphs folder")