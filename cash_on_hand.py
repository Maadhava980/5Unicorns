from pathlib import Path
import csv

#--------------- PART 1: This part of the program is completed for you --------------#

# Modify the file path to cash_on_hand.csv
fp = Path("C:/PFB Group Project/cash_on_hand.csv.csv")

# read the csv file to append Day and CashOnHand from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list to store cash on hand records
    cashOnHandRecords = []

    # append Day and CashOnHand records into the cashOnHandRecords list
    for row in reader:
        cashOnHandRecords.append([int(row[0]), float(row[1])])

# Print cashOnHandRecords to check if the data is being read correctly
print(cashOnHandRecords)

#--------------- PART 2: Function to compute the difference in Cash-on-Hand --------------#

def compute_cash_on_hand_difference(data):
    differences = []
    prev_cash_on_hand = data[0][1] # Set the initial previous cash on hand
    for day, cash_on_hand in data[1:]:
        if cash_on_hand < prev_cash_on_hand:
            difference = cash_on_hand - prev_cash_on_hand
            differences.append((day, difference))
        prev_cash_on_hand = cash_on_hand
    return differences

# Step 2: Calculate the differences in Cash-on-Hand only if it's lower than the previous day.
differences = compute_cash_on_hand_difference(cashOnHandRecords)
for day, amount in differences:
    print(f"[ CASH DEFICIT ] DAY: {day:3}, AMOUNT: USD {amount:.2f}")

#--------------- PART 3: Function to find the day with the highest increase in Cash-on-Hand --------------#

def find_highest_increase(data):
    max_increase_day, max_increase_amount = 0, 0
    prev_cash_on_hand = data[0][1] # Set the initial previous cash on hand
    for day, cash_on_hand in data[1:]:
        increase = cash_on_hand - prev_cash_on_hand
        if increase > max_increase_amount:
            max_increase_day, max_increase_amount = day, increase
        prev_cash_on_hand = cash_on_hand
    return max_increase_day, max_increase_amount

# Step 4: Find the day and amount of the highest increase when Cash-on-Hand is always increasing.
max_increase_day, max_increase_amount = find_highest_increase(cashOnHandRecords)
# Print the highest increase in Cash-on-Hand in the desired format.
print("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
print(f"[HIGHEST CASH SURPLUS] DAY: {max_increase_day}, AMOUNT: USD {max_increase_amount:.2f}")

#--------------- PART 4: Function to find the largest cash-on-hand deficit --------------#

def find_largest_deficit(data):
    max_deficit_day, max_deficit_amount = 0, 0
    prev_cash_on_hand = data[0][1] # Set the initial previous cash on hand
    for day, cash_on_hand in data[1:]:
        deficit = prev_cash_on_hand - cash_on_hand
        if deficit > max_deficit_amount:
            max_deficit_day, max_deficit_amount = day, deficit
        prev_cash_on_hand = cash_on_hand
    return max_deficit_day, max_deficit_amount

# Step 5: Find the day and amount of the largest cash-on-hand deficit.
max_deficit_day, max_deficit_amount = find_largest_deficit(cashOnHandRecords)

if max_increase_amount > max_deficit_amount:
    print("\n[HIGHEST SURPLUS IS GREATER THAN LARGEST DEFICIT]")
    print("[CASH SURPLUS] CASH ON HAND ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    print(f"[HIGHEST CASH SURPLUS] DAY: {max_increase_day}, AMOUNT: USD {max_increase_amount:.2f}")
else:
    print("\n[LARGEST DEFICIT IS GREATER THAN HIGHEST SURPLUS]")
    print("[CASH DEFICIT] CASH ON HAND ON EACH DAY IS LOWER THAN THE PREVIOUS DAY")
    print(f"[LARGEST CASH DEFICIT] DAY: {max_deficit_day}, AMOUNT: USD -{max_deficit_amount:.2f}")
