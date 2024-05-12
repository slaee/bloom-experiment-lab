import csv
import random

# Path to the CSV file
csv_file = 'dataset_new.csv'

# Read the CSV file into a list of lists
with open(csv_file, 'r') as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)

# Shuffle the rows
random.shuffle(data)

# Write the shuffled data back to the CSV file
with open('shuffled_dataset_new.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(data)

print("Rows shuffled successfully in", csv_file)
