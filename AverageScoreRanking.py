import pandas as pd

# Data
data = "C:/Users/user/Downloads/average_scores.csv"

# Load the CSV file into a DataFrame
df = pd.read_csv(data)

# Sort by each metric in descending order
sorted_by_P10 = df[['system', 'P@10']].sort_values(by='P@10', ascending=False)
sorted_by_P100 = df[['system', 'P@100']].sort_values(by='P@100', ascending=False)
sorted_by_MAP100 = df[['system', 'MAP@100']].sort_values(by='MAP@100', ascending=False)
sorted_by_MAP10 = df[['system', 'MAP@10']].sort_values(by='MAP@10', ascending=False)

# Display the sorted DataFrames
print("Sorted by P@10:")
print(sorted_by_P10)
print("\nSorted by P@100:")
print(sorted_by_P100)
print("\nSorted by MAP@100:")
print(sorted_by_MAP100)
print("\nSorted by MAP@10:")
print(sorted_by_MAP10)

