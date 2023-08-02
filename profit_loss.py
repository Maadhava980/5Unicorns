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

#--------------- PART 3: Function to find the day with the highest increase in Net Profit --------------#

def find_highest_increase(data):
    max_increase_day, max_increase_amount = 0, 0
    prev_net_profit = data[0][1] # Set the initial previous net profit
    for day, net_profit in data[1:]:
        increase = net_profit - prev_net_profit
        if increase > max_increase_amount:
            max_increase_day, max_increase_amount = day, increase
        prev_net_profit = net_profit
    return max_increase_day, max_increase_amount

# Step 4: Find the day and amount of the highest increase when Net Profit is always increasing.
max_increase_day, max_increase_amount = find_highest_increase(netProfitRecords)

#--------------- PART 4: Function to find the largest net profit deficit --------------#

def find_largest_deficit(data):
    max_deficit_day, max_deficit_amount = 0, 0
    prev_net_profit = data[0][1] # Set the initial previous net profit
    for day, net_profit in data[1:]:
        deficit = prev_net_profit - net_profit
        if deficit > max_deficit_amount:
            max_deficit_day, max_deficit_amount = day, deficit
        prev_net_profit = net_profit
    return max_deficit_day, max_deficit_amount

# Step 5: Find the day and amount of the largest net profit deficit.
max_deficit_day, max_deficit_amount = find_largest_deficit(netProfitRecords)

#--------------- PART 5: Compare the highest increase with the largest deficit --------------#

if max_increase_amount > max_deficit_amount:
    print("\n[HIGHEST SURPLUS IS GREATER THAN LARGEST DEFICIT]")
    print(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    print(f"[HIGHEST NET PROFIT SURPLUS] DAY: {max_increase_day}, AMOUNT: USD {max_increase_amount:.2f}")
else:
    print("\n[LARGEST DEFICIT IS GREATER THAN HIGHEST SURPLUS]")
    print(f"[LARGEST NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN THE PREVIOUS DAY")
    print(f"[LARGEST NET PROFIT DEFICIT] DAY: {max_deficit_day}, AMOUNT: USD {max_deficit_amount:.2f}")

