from pathlib import Path
import csv

def find_highest_overhead_category(csv_file_path):
    # read the csv file to append overhead category codes from the csv.
    with csv_file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        # initialize variables with the first category and its overhead value
        first_row = next(reader)
        highest_overhead_category = first_row[0]
        highest_overhead_value = float(first_row[1])
        print(f'this is highest overhead value : {highest_overhead_value}')

        # iterate through the remaining rows and find the category with the highest overhead
        for row in reader:
            category = row[0]
            overhead = float(row[1])
            print(f'overhead value:{overhead}')
            if overhead > highest_overhead_value:
                highest_overhead_category = category
                highest_overhead_value = overhead
            print(f'after compare this is highest overhead value : {highest_overhead_value}')
    return highest_overhead_category, highest_overhead_value

# Modify the file path to the desired "Overheads csv" file
csv_file_path = Path("C:/Overheads PFB Group Project/overheads-day-90.csv")

# Call the function to find the highest overhead category and value
highest_category, highest_value = find_highest_overhead_category(csv_file_path)

# Print the final message
print(f"[ HIGHEST OVERHEAD ] {highest_category} : {highest_value}%")
