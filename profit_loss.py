from pathlib import Path
import csv

#--------------- PART 1: This part of the program is completed for you --------------#

# Modify the file path to the "Profit & Loss csv" file
fp = Path("C:/Profit and Loss PFB Group Project/profit-and-loss.csv")

# read the csv file to append Day and Net Profit from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list to store net profit records
    netProfitRecords = []

    # append Day and Net Profit records into the netProfitRecords list
    for row in reader:
        netProfitRecords.append([int(row[0]), float(row[4])])

# Print netProfitRecords to check if the data is being read correctly
print(netProfitRecords)

#--------------- PART 2: Function to compute the difference in Net Profit --------------#

def compute_net_profit_difference(data):
    differences = []
    prev_net_profit = data[0][1] # Set the initial previous net profit
    for day, net_profit in data[1:]:
        if net_profit < prev_net_profit:
            difference = net_profit - prev_net_profit
            differences.append((day, difference))
        prev_net_profit = net_profit
    return differences

# Step 2: Calculate the differences in Net Profit only if it's lower than the previous day.
differences = compute_net_profit_difference(netProfitRecords)
for day, amount in differences:
    print(f"[ NET PROFIT DEFICIT ] DAY: {day:3}, AMOUNT: USD {amount:.2f}")
