import pandas as pd
import os

# Create a sample DataFrame with proper column names
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Example of adding new rows for dataset versioning (V2, V3)

#new_row_v2 = {'Name': 'V2', 'Age': 20, 'City': 'City1'}
#df.loc[len(df.index)] = new_row_v2

#new_row_v3 = {'Name': 'V3', 'Age': 30, 'City': 'City2'}
#df.loc[len(df.index)] = new_row_v3

# Ensure the "data" directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save DataFrame to CSV
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")
