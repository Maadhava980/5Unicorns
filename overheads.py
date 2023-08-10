def overhead_func():
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

            # iterate through the remaining rows and find the category with the highest overhead
            for row in reader:
                category = row[0]
                overhead = float(row[1])
                if overhead > highest_overhead_value:
                    highest_overhead_category = category
                    highest_overhead_value = overhead
        return highest_overhead_category, highest_overhead_value

    csv_file_path = Path("PFBGP", "csv_reports", "Overheads.csv")
    highest_category, highest_value = find_highest_overhead_category(csv_file_path)

    result = f"[ HIGHEST OVERHEAD ] {highest_category} : {highest_value}%"
    
    # Create the txt file
    filepath = Path.cwd() / "Summary_report.txt"
    
    # Open the file to write on it
    with filepath.open(mode="w", encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([result])  # Write the result to the txt file

    return result

# Call the overhead_func() and capture its result
overhead_result = overhead_func()

# Print the result
print(overhead_result)


