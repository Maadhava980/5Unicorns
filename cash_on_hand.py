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
