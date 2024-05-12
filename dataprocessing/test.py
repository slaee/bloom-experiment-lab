import csv
import random

# Function to read CSV file and return list of rows
def read_csv(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data

# Function to write combined data to a new CSV file
def write_csv(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

# Paths to your CSV files
csv_files = ["combined.csv", "error_data_prototype_pollution.csv", "error_data_prototype_pollution_random.csv"]

# Read data from each CSV file
data = []
first_file_data = None  # To hold the data from the first CSV file

for i, file in enumerate(csv_files):
    file_data = read_csv(file)
    if i == 0:
        first_file_data = [row[:1] + row[1:] for row in file_data]  # Exclude shuffling the first column
    else:
        data.extend(file_data)

# Shuffle the combined data from error_data_legit.csv and error_data_2.csv randomly
random.shuffle(data)

# Combine the shuffled data with the data from clean_output.csv
data = first_file_data + data

# Write the combined data to a new CSV file
output_file = "new_combined.csv"
write_csv(data, output_file)
