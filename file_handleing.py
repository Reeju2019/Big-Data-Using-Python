import csv

class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, newline='')  # Added `newline=''` for CSV compatibility
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

# Reading from a CSV file and writing its content to a new CSV file
input_file = 'organizations-1000.csv'
output_file = 'output.csv'

# Read the content of the input CSV
with FileManager(input_file, 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)  # Store rows in a list

# Write the content to the output CSV
with FileManager(output_file, 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(rows)

print("CSV content copied successfully.")