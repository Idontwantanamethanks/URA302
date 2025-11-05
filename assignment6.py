import pandas as pd

# Q1.1 Importing Pandas and checking version
print("Q1.1: Pandas version:", pd.__version__)

# Q1.2 Creating a DataFrame
q1_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
q1_df = pd.DataFrame(q1_data)
print("\nQ1.2: DataFrame:\n", q1_df)

# Q2.1 Creating a Series
q2_s1 = pd.Series([100, 200, 300, 400, 500])
print("\nQ2.1: Series S1:\n", q2_s1)

# Q2.2 Accessing Elements in Series (second and fourth)
print("\nQ2.2: Second element:", q2_s1.iloc[1], "Fourth element:", q2_s1.iloc[3])

# Q2.3 Series Operations
q2_s2 = pd.Series([10, 20, 30, 40, 50])
q2_sum = q2_s1 + q2_s2
print("\nQ2.3: Element-wise addition S1 + S2:\n", q2_sum)

# Q3.1 Accessing columns 'Name' and 'City'
print("\nQ3.1: Name and City columns:\n", q1_df[['Name', 'City']])

# Q3.2 Adding a new column 'Salary'
q1_df['Salary'] = [50000, 60000, 70000]
print("\nQ3.2: Updated DataFrame with Salary:\n", q1_df)

# Q3.3 Basic statistics
avg_age = q1_df['Age'].mean()
sum_salary = q1_df['Salary'].sum()
print("\nQ3.3: Average Age:", avg_age, "Total Salary:", sum_salary)

# Q4.1 Conditional filtering (Age > 28)
q4_filtered = q1_df[q1_df['Age'] > 28]
print("\nQ4.1: Filtered DataFrame (Age>28):\n", q4_filtered)

# Q4.2 Setting and resetting index
q4_indexed = q1_df.set_index('Name')
print("\nQ4.2: DataFrame with 'Name' as index:\n", q4_indexed)
q4_reset = q4_indexed.reset_index()
print("\nQ4.2: Reset index DataFrame:\n", q4_reset)

# Q5.1 Reading a CSV file
employees_data = {
    'Name': ['John', 'Jane', 'Emily'],
    'Department': ['Sales', 'Marketing', 'HR'],
    'Salary': [50000, 60000, 55000]
}
employees_df = pd.DataFrame(employees_data)
print("\nQ5.1: Employees DataFrame:\n", employees_df)

# Q5.2 Filtering rows where Salary > 55000 and printing Name and Department
q5_filtered = employees_df[employees_df['Salary'] > 55000][['Name', 'Department']]
print("\nQ5.2: Filtered Employees (Salary>55000):\n", q5_filtered)

# Q6.1 Group by Department and calculate average Salary
q6_avg_salary = employees_df.groupby('Department')['Salary'].mean()
print("\nQ6.1: Average Salary by Department:\n", q6_avg_salary)

# Q6.2 Minimum and maximum Salary per Department
q6_min_max = employees_df.groupby('Department')['Salary'].agg(['min', 'max'])
print("\nQ6.2: Min and Max Salary per Department:\n", q6_min_max)

# Q7
df1 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Department': ['Sales', 'Marketing', 'HR']
})
df2 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Experience (Years)': [5, 7, 3]
})
q7_merged = pd.merge(df1, df2, on='Name')
print("\nQ7.1: Merged DataFrame:\n", q7_merged)

# Q8: Sorting
q8_sorted = q7_merged.sort_values(by='Experience (Years)', ascending=False)
print("\nQ8.1: DataFrame sorted by Experience (descending):\n", q8_sorted)
