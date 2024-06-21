# Sample data
data = [
    {'Name': 'Harry Kane', 'Age': 25, 'City': 'New York'},
    {'Name': 'Phil Foden', 'Age': 30, 'City': 'Los Angeles'},
    {'Name': 'C.Eriksen', 'Age': 35, 'City': 'Chicago'}
]

# Filtering data where age is greater than 25
filtered_data = [record for record in data if record['Age'] > 25]
print("Filtered Data:")
print(filtered_data)

# Sorting data by age
sorted_data = sorted(data, key=lambda x: x['Age'])
print("\nSorted Data:")
print(sorted_data)

# Grouping data by city
grouped_data = {}
for record in data:
    city = record['City']
    if city in grouped_data:
        grouped_data[city].append(record)
    else:
        grouped_data[city] = [record]

print("\nGrouped Data:")
for city, records in grouped_data.items():
    print(city + ":")
    for record in records:
        print(record)
    print()
