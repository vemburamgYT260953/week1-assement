
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
REPORTS = ROOT / "reports"

REPORTS.mkdir(exist_ok=True)

# PART A: NumPy
marks = np.array([
    [80, 75, 90],
    [65, 70, 72],
    [90, 85, 88],
    [78, 82, 80]
])

print("Shape:", marks.shape)
print("Student averages:", marks.mean(axis=1))
print("Subject averages:", marks.mean(axis=0))

grace_marks = marks + 5
print("Marks after grace:", grace_marks)

weights = np.array([0.4, 0.3, 0.3])
weighted_scores = np.dot(marks, weights)
print("Weighted scores:", weighted_scores)

# PART B: Pandas
df = pd.read_csv(DATA / "employees.csv")

print("\nData information:")
df.info()
print("\nStatistics:")
print(df.describe())

print("\nUsing loc:")
print(df.loc[0:2, ["name", "salary"]])

print("\nUsing iloc:")
print(df.iloc[0:3, 0:3])

print("\nEmployees earning above 50000:")
print(df[df["salary"] > 50000])

# Add two missing salaries and one duplicate row for cleaning practice
dirty_df = df.copy()
dirty_df.loc[0, "salary"] = np.nan
dirty_df.loc[2, "salary"] = np.nan
dirty_df = pd.concat(
    [dirty_df, dirty_df.iloc[[1]]],
    ignore_index=True
)

dirty_df["salary"] = pd.to_numeric(
    dirty_df["salary"], errors="coerce"
)

median_salary = dirty_df["salary"].median()
dirty_df["salary"] = dirty_df["salary"].fillna(median_salary)
dirty_df = dirty_df.drop_duplicates()

dirty_df["id"] = dirty_df["id"].astype(int)
dirty_df["salary"] = dirty_df["salary"].astype(float)

print("\nCleaned data:")
print(dirty_df)
print("Missing salaries filled with median:", median_salary)

# PART C: Department data
departments = pd.DataFrame([
    {"department": "Sales", "head": "Ravi", "budget": 200000},
    {"department": "HR", "head": "Lakshmi", "budget": 150000},
    {"department": "IT", "head": "Kumar", "budget": 500000},
    {"department": "Finance", "head": "Priya", "budget": 250000},
    {"department": "Marketing", "head": "Sanjay", "budget": 180000}
])

departments.to_csv(DATA / "departments.csv", index=False)

# Analyze the original employee data
summary = df.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
).reset_index()

print("\nDepartment summary:")
print(summary)

# Inner join
inner_join = pd.merge(df, departments, on="department", how="inner")
print("\nInner join:")
print(inner_join[["name", "department", "head"]])

# Left join
left_join = pd.merge(df, departments, on="department", how="left")
print("\nLeft join:")
print(left_join[["name", "department", "head"]])

# Outer join: includes departments without employees
outer_join = pd.merge(df, departments, on="department", how="outer")
print("\nOuter join:")
print(outer_join[["name", "department", "head"]])

employee_departments = set(df["department"])
empty_departments = [
    dept for dept in departments["department"]
    if dept not in employee_departments
]
print("Departments with no employees:", empty_departments)

# PART D: Four charts

# 1. Bar chart: average salary by department
avg_salary = df.groupby("department")["salary"].mean()

avg_salary.plot(kind="bar", label="Average salary")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig(REPORTS / "bar_chart.png")
plt.close()

print("Insight: Finance has the highest average salary.")

# 2. Histogram: salary distribution
df["salary"].plot(kind="hist", bins=5, label="Employees")
plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()
plt.savefig(REPORTS / "histogram.png")
plt.close()

print("Insight: Salaries vary across the employee group.")

# 3. Scatter chart: employee ID against salary
plt.scatter(df["id"], df["salary"], label="Employees")
plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig(REPORTS / "scatter_chart.png")
plt.close()

print("Insight: Employee ID does not represent salary rank.")

# 4. Line chart: salaries by employee ID
plt.plot(
    df["id"], df["salary"],
    marker="o", label="Salary"
)
plt.title("Salary by Employee ID")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig(REPORTS / "line_chart.png")
plt.close()

print("Insight: Salary changes from one employee record to another.")

# Save useful reports
summary.to_csv(REPORTS / "department_summary.csv", index=False)

print("\nAll four charts and department summary saved in reports/.")
