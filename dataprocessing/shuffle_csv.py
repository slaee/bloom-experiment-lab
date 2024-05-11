import pandas as pd

# Path to the CSV file
csv_file = 'shuffled_dataset.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Separate the header row
header = df.iloc[0]
data = df.iloc[1:]

# Shuffle the data rows
shuffled_data = data.sample(frac=1).reset_index(drop=True)

# Concatenate the header row and shuffled data
shuffled_df = pd.concat([header.to_frame().T, shuffled_data], ignore_index=True)

# Path to the output CSV file
output_csv = 'shuffled_dataset_new.csv'

# Save the shuffled DataFrame to a new CSV file
shuffled_df.to_csv(output_csv, index=False)

print("Data shuffled successfully and saved to", output_csv)
