import pandas as pd

# Step 2: Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Step 3: Inspect the DataFrame
print(df.head())  # Display the first few rows
print(df.describe())  # Display summary statistics
print(df.info())  # Display info about the DataFrame

# Step 4: Select Data
print(df['Name'])  # Select the 'Name' column
print(df[['Name', 'Age']])  # Select the 'Name' and 'Age' columns
print(df.iloc[0])  # Select the first row
print(df.iloc[1:3])  # Select the second and third rows
print(df[df['Age'] > 25])  # Select rows where 'Age' > 25

# Step 5: Data Manipulation
df['Salary'] = [50000, 60000, 55000, 70000]  # Add a new column 'Salary'
print(df)
df['Age'] = df['Age'] + 1  # Increment 'Age' by 1
print(df)
df = df.drop('Salary', axis=1)  # Drop the 'Salary' column
print(df)
df = df.rename(columns={'Name': 'Full Name'})  # Rename 'Name' to 'Full Name'
print(df)

# Step 6: Handling Missing Data
df['Age'] = df['Age'].fillna(df['Age'].mean())  # Fill missing values in 'Age' with the mean
print(df)
df = df.dropna()  # Drop rows with missing values
print(df)

# Step 7: Grouping and Aggregation
grouped = df.groupby('City')['Age'].mean()  # Group by 'City' and calculate mean 'Age'
print(grouped)
grouped = df.groupby(['City', 'Age']).sum()  # Group by 'City' and 'Age' and calculate sum
print(grouped)

# Step 8: Exporting Data
df.to_csv('manipulated_data.csv', index=False)  # Export the DataFrame to a CSV file
